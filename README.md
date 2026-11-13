A Python-based computer vision application that enables touchless screen brightness adjustment through hand gestures.

Using OpenCV and MediaPipe, the application tracks the thumb and index finger through a webcam. Their distance is mapped to screen brightness (0–100%) using NumPy interpolation, with exponential smoothing for stable adjustments.
