# YOLO Game helper
This is a game assistant project based on object detection. It first captures images using OpenCV and then performs object detection with YOLOv4-tiny. After that, it uses pynput to carry out some in-game operations.
## Dependancy
pywin32
numpy
Pillow
opencv-python
pynput

## How to start
### Installation
1. Clone this repository
2. Install dependacy
```
pip install pywin32 numpy Pillow opencv-python pynput
```
### Train your custom YOLO model
#### Create training data set
1. Run the [screenshoper.py.py](./screenshoper.py) script to start gathering window screenshop.
   The screenshop will store in the ./images directory
```
Usage: screenshoper <Window_name> <Rate>
```
2. Shuffle the screenshop images by running [shuffleimg.py](./shuffleimg.py)  
   (The shuffled screenshop will store in the ./shuffle_images directory)
4. Label the images. For example [Makesense.ai](https://www.makesense.ai/)
5. Copy the images and label into the folder ./shuffle_images
6. Run the [labelimgszipper.py](./labelimgszipper.py) zip the final training data.  
   (The training data will be move to yolov4-tiny folder)
8. Set the object detection classes in the [yoloconfig.py](./labelimgszipper.py).  
   (Then run the [yoloconfig.py](./labelimgszipper.py) to set up the YOLO configuration.)
10. Upload the yolov4-tiny folder onto the Goole Drive.
11. Training model with this [Colab notebook](https://colab.research.google.com/drive/1GacwLZuQrk2dDTuvxuGX3Tn5i8Z4X13c#scrollTo=UcHcVVfHRqx5)
12. Download the yolov4-tiny-custom_last.weights and move to the ./YOLO-Game-Helper folder

#### Start the assist program
1. Modify the [automation.py](./automation.py) to fit your own game automation logic,
   and set the window_name to your game.
2. Run the [automation.py](./automation.py)  
   You can start and pause the bot thread by pressing the 's' and 'p'.  
   Or quit the automation program by pressing the 'q'.
