# YOLO Game helper
This is a game assistant project based on object detection. It first captures images using OpenCV and then performs object detection with YOLOv4-tiny. After that, it uses pynput to carry out some in-game operations.
## Dependancy
pywin32, numpy ,Pillow ,opencv-python, pynput

## How to start
### Installation
1. Clone this repository
2. Install dependacy
```
pip install pywin32 numpy Pillow opencv-python pynput
```
### Train your custom YOLO model
#### Create training data set
1. Run the [shuffleimg.py](./screenshoper.py) script to start gathering window screenshop.
   The screenshop will store in the ./images directory
```
Usage: screenshoper <Window_name> <Rate>
```
2. Shuffle the screenshop images by running [shuffleimg.py](./shuffleimg.py)
   The shuffled screenshop will store in the ./shuffleimages directory
4. Label the images. For example [Makesense.ai](https://www.makesense.ai/)
5. Copy the 
