
import cv2
import numpy as np
import math

from handDetector import HandDetector
from brightnessController import BrightnessController


def main():

    detector = HandDetector(
        max_hands=1,
        detection_confidence=0.75,
        tracking_confidence=0.75
    )

    brightness_controller = BrightnessController()

    cap = cv2.VideoCapture(0)    # Open webcam

    if not cap.isOpened():
        print("Error: Could not access webcam.")
        detector.close()
        return

    # Brightness mapping limits
    min_distance = 30
    max_distance = 200

    # Smoothing configuration
    smoothing_factor = 0.2
    smoothed_brightness = None

    print("Hand Gesture Brightness Control started.")
    print("Move your thumb and index finger to adjust brightness.")
    print("Press ESC to exit.")

    try:

        while True:

            success, frame = cap.read()

            if not success:
                print("Error: Could not read webcam frame.")
                break

            # Flip frame for mirror-like interaction
            frame = cv2.flip(frame, 1)

            # Detect hands
            frame = detector.find_hands(frame)

            # Extract hand landmarks
            landmark_list = detector.find_position(frame)

            # Process detected hand
            if landmark_list:

                # Thumb tip: landmark 4
                x1, y1 = landmark_list[4][1], landmark_list[4][2]

                # Index finger tip: landmark 8
                x2, y2 = landmark_list[8][1], landmark_list[8][2]

                # Draw circles on fingertips
                cv2.circle(frame, (x1, y1), 10, (0, 255, 0), cv2.FILLED)
                cv2.circle(frame, (x2, y2), 10, (0, 255, 0), cv2.FILLED)

                # Draw line between fingertips
                cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # Calculate Euclidean distance
                distance = math.hypot(x2 - x1, y2 - y1)

                # Map distance to brightness (0-100)
                brightness = np.interp(
                    distance,
                    [min_distance, max_distance],
                    [0, 100]
                )

                # Apply exponential smoothing
                if smoothed_brightness is None:
                    smoothed_brightness = brightness
                else:
                    smoothed_brightness = (
                        smoothing_factor * brightness
                        + (1 - smoothing_factor) * smoothed_brightness
                    )

                brightness = int(round(smoothed_brightness))

                # Update screen brightness
                brightness_controller.set_brightness(brightness)

                # Display distance and brightness
                cv2.putText(
                    frame,
                    f"Distance: {int(distance)} px",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                )

                cv2.putText(
                    frame,
                    f"Brightness: {brightness}%",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

            else:

                cv2.putText(
                    frame,
                    "No hand detected",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )

            # Display webcam feed
            cv2.imshow("Hand Gesture Brightness Control", frame)

            # Exit when ESC is pressed
            if cv2.waitKey(1) & 0xFF == 27:
                break

    finally:

        # Release resources
        cap.release()
        detector.close()
        cv2.destroyAllWindows()

        print("Application stopped.")


if __name__ == "__main__":
    main()
