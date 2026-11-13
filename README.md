Hand Gesture-Based Screen Brightness Control

A real-time computer vision application for controlling screen brightness through hand gestures. The system tracks the thumb and index finger using a webcam and adjusts display brightness according to the distance between their fingertips.

Overview

The application uses MediaPipe for hand landmark detection and OpenCV for webcam acquisition and image processing. The distance between the thumb tip and index finger tip is calculated for each frame and mapped to a brightness range of 0–100%.

The project is implemented in Python using a modular structure, separating hand detection from display brightness control.

Methodology

The application follows the steps below:

Video acquisition: Capture live video frames from the system webcam using OpenCV.

Hand detection: Process the video frames using MediaPipe Hands to identify hand landmarks.

Landmark extraction: Extract the pixel coordinates of the thumb tip (landmark 4) and index finger tip (landmark 8).

Distance calculation: Calculate the Euclidean distance between the two fingertips.

Brightness mapping: Map the measured distance to a brightness range of 0–100% using NumPy interpolation.

Brightness adjustment: Apply the calculated brightness value to the display using the Screen Brightness Control library.

Working Principle

The distance between the thumb and index finger is calculated using the Euclidean distance formula:

[
d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
]

The resulting distance is mapped to the desired brightness range using linear interpolation:

[
B = \operatorname{interp}(d,[d_{\min},d_{\max}],[0,100])
]

An exponential smoothing filter is applied to the brightness values to reduce fluctuations caused by small hand movements.

The smoothed brightness value is then passed to the brightness controller.