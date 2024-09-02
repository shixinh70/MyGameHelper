
import sys
from pynput import keyboard as keyboard_module
import threading
from windowcaputre import WindowCapture, quit_event

def on_press(key):
    try:
        if key.char == 'q':  
            print("Quit bot")
            quit_event.set()
            return False  
            
    except AttributeError:
        pass

    
def start_listener():
    with keyboard_module.Listener(on_press=on_press) as listener:
        listener.join()

def main():
    if len(sys.argv) != 3:
        print("Usage: screenshoper.py window_name screen_rate (sec)")
        sys.exit(1)
    print("Press 'q' to quit...")
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()
    window_name = sys.argv[1]
    screen_rate = float(sys.argv[2])
    wincap = WindowCapture(window_name)
    wincap.generate_image_dataset(screen_rate)
     



if __name__ == "__main__":
     main()