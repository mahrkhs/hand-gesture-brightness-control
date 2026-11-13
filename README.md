A Python-based computer vision application that enables touchless screen brightness adjustment through hand gestures.
Using OpenCV and MediaPipe, the application tracks the thumb and index finger through a webcam. Their distance is mapped to screen brightness (0–100%) using NumPy interpolation, with exponential smoothing for stable adjustments. 
The processing pipeline involves webcam acquisition, hand landmark detection, fingertip coordinate extraction and Euclidean distance calculation. The distance between the fingertips is calculated as:

$$
d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
$$

The measured distance is mapped to the brightness range using linear interpolation:

$$
B = 100 \times \frac{d-d_{\min}}{d_{\max}-d_{\min}}
$$

The calculated brightness is constrained to the range of 0–100%, followed by exponential smoothing to minimise fluctuations during hand movement.

<p align="center">
    <img width="500" height="500" alt="output" src="https://github.com/user-attachments/assets/059d9e02-5d78-451e-9a2f-63ebc60960a4" />

</p>
