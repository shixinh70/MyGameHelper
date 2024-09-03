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
1. Run the [screenshoper](./screenshoper.py) script to start gathering window screenshop.
```
Usage: screenshoper <Window_name> <Rate>
```

