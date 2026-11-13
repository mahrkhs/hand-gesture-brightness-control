A Python-based computer vision application that enables touchless screen brightness adjustment through hand gestures.
Using OpenCV and MediaPipe, the application tracks the thumb and index finger through a webcam. Their distance is mapped to screen brightness (0–100%) using NumPy interpolation, with exponential smoothing for stable adjustments. The processing pipeline involves webcam acquisition, hand landmark detection, fingertip coordinate extraction and Euclidean distance calculation. The measured distance is mapped to the brightness range using NumPy interpolation:

$$
d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
$$

$$
B = \operatorname{interp}(d,[d_{\min},d_{\max}],[0,100])
$$

An exponential smoothing filter is used to stabilise brightness adjustments before applying them to the display.

<p align="center">
    <img width="500" height="500" alt="output" src="https://github.com/user-attachments/assets/059d9e02-5d78-451e-9a2f-63ebc60960a4" />

</p>
