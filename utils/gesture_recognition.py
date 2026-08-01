import math


class GestureRecognition:

    def __init__(self):
        pass

    def distance(self, p1, p2):
        return math.sqrt(
            (p1[0] - p2[0]) ** 2 +
            (p1[1] - p2[1]) ** 2
        )

    def finger_up(self, landmarks, tip, pip):
        return landmarks[tip][1] < landmarks[pip][1]

    def thumb_up(self, landmarks):
        return landmarks[4][1] < landmarks[3][1]

    def thumb_down(self, landmarks):
        return landmarks[4][1] > landmarks[3][1]

    def detect(self, landmarks):

        if len(landmarks) < 21:
            return "No Hand"

        thumb = self.thumb_up(landmarks)

        index = self.finger_up(
            landmarks,
            8,
            6
        )

        middle = self.finger_up(
            landmarks,
            12,
            10
        )

        ring = self.finger_up(
            landmarks,
            16,
            14
        )

        pinky = self.finger_up(
            landmarks,
            20,
            18
        )

        thumb_tip = landmarks[4]
        index_tip = landmarks[8]

        ok_distance = self.distance(
            thumb_tip,
            index_tip
        )

        # -----------------------
        # OK
        # -----------------------

        if ok_distance < 35:
            return "OK"

        # -----------------------
        # POINTER
        # -----------------------

        if index and not middle and not ring and not pinky:
            return "Pointer"

        # -----------------------
        # VICTORY
        # -----------------------

        if index and middle and not ring and not pinky:
            return "Victory"

        # -----------------------
        # ROCK
        # -----------------------

        if index and pinky and not middle and not ring:
            return "Rock"

        # -----------------------
        # OPEN
        # -----------------------

        if thumb and index and middle and ring and pinky:
            return "Open"

        # -----------------------
        # CLOSE
        # -----------------------

        if (not index and
            not middle and
            not ring and
            not pinky):
            return "Close"
                # -----------------------
        # THUMBS UP
        # -----------------------

        if (thumb and
            not index and
            not middle and
            not ring and
            not pinky):
            return "Thumbs Up"

        # -----------------------
        # THUMBS DOWN
        # -----------------------

        if (self.thumb_down(landmarks)
            and
            not index
            and
            not middle
            and
            not ring
            and
            not pinky):
            return "Thumbs Down"

        # -----------------------
        # HELLO
        # -----------------------

        if thumb and index and middle and ring and pinky:
            return "Hello"

        # -----------------------
        # STOP
        # -----------------------

        if index and middle and ring and pinky:
            return "Stop"

        return "Unknown"