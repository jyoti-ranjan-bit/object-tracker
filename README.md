# Ball Tracking Device with Raspberry Pi Zero

## Overview
This project involves creating a ball-tracking device using Raspberry Pi Zero. The system detects and tracks a ball based on its color and moves a car to follow the ball. It integrates computer vision with motor control to achieve real-time tracking and movement. The project demonstrates the practical application of robotics and computer vision for autonomous systems.

---

## Features
- **Color-based Ball Tracking**: Tracks a ball of a specific color using OpenCV.
- **Real-time Movement**: Controls a car to move in the direction of the ball.
- **GPIO Integration**: Uses Raspberry Pi GPIO pins to control motors.
- **Customizable Parameters**: The ball's color range and movement thresholds can be adjusted.

---

## Components Required
1. **Hardware**:
   - Raspberry Pi Zero
   - Laptop with camera
   - L298N Motor Driver
   - DC Motors (2 or 4 depending on the design)
   - Car Chassis
   - Wheels
   - Battery Pack (for motor power)
   - Jumper Wires

2. **Software**:
   - Python 3
   - OpenCV
   - NumPy
   - RPi.GPIO

---

## Circuit Connections
1. **Motor Driver to Raspberry Pi GPIO**:
   - `IN1` -> GPIO 17
   - `IN2` -> GPIO 18
   - `IN3` -> GPIO 22
   - `IN4` -> GPIO 23
2. **Motor Driver to Motors**:
   - `OUT1` and `OUT2` -> Motor 1
   - `OUT3` and `OUT4` -> Motor 2
3. **Power Connections**:
   - Connect battery pack to the `VCC` and `GND` of the motor driver.
   - Ensure Raspberry Pi and motor driver share a common ground.

---

## Installation
1. **Install Required Libraries**:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install opencv-python numpy RPi.GPIO
   ```
2. **Prepare the Raspberry Pi**:
   - Set up Raspberry Pi Zero with Raspbian OS.
   - Enable GPIO and Python support.

---

## Usage
1. **Run the Script**:
   ```bash
   python3 ball_tracking.py
   ```
2. **Adjust Color Range**:
   - Modify the `lower_color` and `upper_color` arrays in the script to match the ball's color.
3. **Control the Car**:
   - The car will move forward, backward, or stop based on the ball's position in the camera feed.

---

## How It Works
1. The camera captures live video frames.
2. Frames are processed in HSV color space to detect the ball.
3. The position of the ball is determined using contour detection.
4. Raspberry Pi controls the motors to move the car in the direction of the ball.
5. If the ball is not detected, the car stops.

---

## Challenges and Solutions
1. **Color Detection Issues**:
   - **Problem**: Variations in lighting affect color detection.
   - **Solution**: Use dynamic thresholding or test the system under various lighting conditions.
2. **Motor Control Precision**:
   - **Problem**: Motors may not respond precisely.
   - **Solution**: Use a motor driver for stable control and calibrate movement thresholds.
3. **Hardware Limitations**:
   - **Problem**: Raspberry Pi Zero's limited processing power.
   - **Solution**: Optimize OpenCV code for real-time performance.


---

## Contributors
-  Rajdeep Mohanty, Sourav Agrawal, Jyoti Ranjan Padhi

---

## Acknowledgments
- OpenCV community for image processing tutorials.
- Raspberry Pi Foundation for providing GPIO support.
- Online forums for debugging and optimization tips.

--- 

## [Youtube Video Link](https://youtu.be/kaP4tWOSB0I?si=Na0xXMoKOxjftX80)


