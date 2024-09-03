from time import sleep
import cv2 as cv
from imageprocessor import ImageProcessor
from windowcaputre import WindowCapture
import threading
from pynput import keyboard as keyboard_module
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
keyboard= KeyboardController()
mouse = MouseController()

window_name = "Ragnarok"
cfg_file_name = "./yolov4-tiny/yolov4-tiny-custom.cfg" 
weights_file_name = "yolov4-tiny-custom_last.weights"
wincap = WindowCapture(window_name)
improc = ImageProcessor(wincap.get_window_size(), cfg_file_name, weights_file_name)

start_event = threading.Event()
quit_event = threading.Event()


def click_thread():
    while not quit_event.is_set():
        if start_event.is_set():
            if len(coordinates) == 0:
                keyboard.press('r')
                sleep(0.05)
                keyboard.release('r')
                sleep(2)
                continue

            screen_center_x = wincap.get_window_size()[0] // 2
            screen_center_y = wincap.get_window_size()[1] // 2
            fruit_to_hit = min(coordinates, key=lambda c: (c['x'] - screen_center_x)**2 + (c['y'] - screen_center_y)**2)
            
            # keyboard.press('w')
            # sleep(0.05)
            # keyboard.release('w')
            # sleep(0.05)


            mouse.position = (fruit_to_hit['x'] + fruit_to_hit['h']//2, fruit_to_hit['y'] + fruit_to_hit['w']//2)
            sleep(0.05)
            mouse.press(Button.left)
            sleep(0.01)
            mouse.release(Button.left)
            sleep(0.05)
            mouse.position = (screen_center_x, screen_center_y)
            sleep(0.01)
        else:
            start_event.wait()
        sleep(1.5)

def skill_set_240():
    keyboard.press('t')
    sleep(0.05)
    keyboard.release('t')


def skill_thread():
    sec_60 = 60
    sec_90 = 90
    sec_240  = 240
    while not quit_event.is_set():
        if start_event.is_set():
            sec_240 += 30
            if(sec_240 >= 240):
                skill_set_240()
                sec_240 = 0
            sleep(30)                
        else:
            start_event.wait()

    

def bot_thread_function():
    skill_thread_instance = threading.Thread(target=skill_thread)
    skill_thread_instance.start()
    click_thread_instance = threading.Thread(target=click_thread)
    click_thread_instance.start()
    

    click_thread_instance.join()
    skill_thread_instance.join()
        


def on_press(key):
    try:
        if key.char == 's': 
            start_event.set()
            print("Start bot")
        elif key.char == 'p':  
            start_event.clear()
            print("Pause bot")
        elif key.char == 'q':  
            print("Quit bot")
            quit_event.set()
            start_event.set() 
            return False
            
    except AttributeError:
        pass
    
def start_listener():
    with keyboard_module.Listener(on_press=on_press) as listener:
        listener.join()

bot_thread = threading.Thread(target=bot_thread_function)
bot_thread.start()
listener_thread = threading.Thread(target=start_listener)
listener_thread.start()

sleep(4)

while(True):
    
    ss = wincap.get_screenshot()
    cv.waitKey(1)
    if quit_event.is_set():
        cv.destroyAllWindows()
        break
    desired_classes = ["Les"]
    coordinates = improc.proccess_image(ss)
    coordinates = [c for c in coordinates if c["class_name"] in desired_classes ]

    sleep(0.016)
    

bot_thread.join()
print('Finished.')
