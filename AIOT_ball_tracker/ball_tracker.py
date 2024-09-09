from gpiozero import OutputDevice
from time import sleep
import cv2
import numpy as np

# Define GPIO pins
 = OutputDevice(23)

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Define track color (in BGR format)
track_color = np.uint8([[[0, 0, 255]]])  # Red color in BGR format

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for track color in HSV
    lower_bound = np.array([0, 100, 100])
    upper_bound = np.array([10, 255, 255])

    # Threshold the HSV image to get only the desired color
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Get the largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        (x, y), _ = cv2.minEnclosingCircle(largest_contour)
        x = int(x)
        y = int(y)

        # Draw a circle at the tracked pixel
        cv2.circle(frame, (x, y), 16, (0, 0, 255), 4)

        # Perform GPIO operations based on tracked pixel position
        if x < 140:
            pin17.on()
            pin18.on()
            pin22.on()
            pin23.off()
            sleep(0.01)
            pin17.on()
            pin18.on()
            pin22.on()
            pin23.on()
            print("Turn Right")
        elif x > 200:
            pin17.on()
            pin18.off()
            pin22.on()
            pin23.on()
            sleep(0.01)
            pin17.on()
            pin18.on()
            pin22.on()
            pin23.on()
            print("Turn Left")
        elif y < 170:
            pin17.on()
            pin18.off()
            pin22.on()
            pin23.off()
            sleep(0.01)
            pin17.on()
            pin18.on()
            pin22.on()
            pin23.on()
            print("Go Forward")
        else:
            pin17.on()
            pin18.on()
            pin22.on()
            pin23.on()
    else:
        pin17.on()
        pin18.on()
        pin22.on()
        pin23.on()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
