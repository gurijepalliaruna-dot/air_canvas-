import cv2
import mediapipe as mp


class HandTracker:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = mp.solutions.drawing_utils


    def detect(self, image):

        rgb = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

        results = self.hands.process(rgb)

        landmarks = []


        if results.multi_hand_landmarks:

            hand = results.multi_hand_landmarks[0]


            self.drawer.draw_landmarks(
                image,
                hand,
                self.mpHands.HAND_CONNECTIONS
            )


            height, width, _ = image.shape


            for lm in hand.landmark:

                x = int(lm.x * width)
                y = int(lm.y * height)

                landmarks.append((x, y))


        return image, landmarks



    def index_finger_position(self, landmarks):

        if len(landmarks) > 8:

            # Index finger tip landmark = 8
            return landmarks[8]

        return None