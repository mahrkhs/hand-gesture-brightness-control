import cv2
import mediapipe as mp



class HandDetector:

    def __init__(
        self,
        max_hands=1,
        detection_confidence=0.75,
        tracking_confidence=0.75
    ):
        self.max_hands = max_hands

        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            model_complexity=1,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )

    def find_hands(self, frame, draw=True):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        self.results = self.hands.process(rgb_frame)

        if self.results.multi_hand_landmarks:

            for hand_landmarks in self.results.multi_hand_landmarks:

                if draw:
                    self.mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )

        return frame

    def find_position(self, frame, hand_index=0):

        landmark_list = []

        if (
            self.results.multi_hand_landmarks
            and len(self.results.multi_hand_landmarks) > hand_index
        ):

            hand_landmarks = (
                self.results.multi_hand_landmarks[hand_index]
            )

            height, width, _ = frame.shape

            for landmark_id, landmark in enumerate(
                hand_landmarks.landmark
            ):

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                landmark_list.append((landmark_id, x, y))

        return landmark_list

    def close(self):
        self.hands.close()
