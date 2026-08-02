import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import av
import cv2
import numpy as np
import os
import sys

# Project path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from utils.handtracking import HandTracker
from utils.gesture_recognition import GestureRecognition

st.set_page_config(
    page_title="Live Gesture Prediction",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Live Gesture Recognition + Air Canvas")
st.write("Browser Webcam Version")

rtc_configuration = RTCConfiguration(
    {
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)
class VideoProcessor(VideoProcessorBase):

    def __init__(self):

        self.tracker = HandTracker()

        self.recognizer = GestureRecognition()

        self.canvas = np.zeros((480,640,3),dtype=np.uint8)

        self.previous_point = None

        self.brush = 5

        self.color = (0,255,0)

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        img = cv2.flip(img,1)

        img, landmarks = self.tracker.detect(img)

        gesture = "No Hand"

        if landmarks:

            gesture = self.recognizer.detect(landmarks)

            if gesture == "Pointer":

                point = self.tracker.index_finger_position(
                    landmarks
                )

                if point:

                    if self.previous_point:

                        cv2.line(
                            self.canvas,
                            self.previous_point,
                            point,
                            self.color,
                            self.brush
                        )

                    self.previous_point = point

            elif gesture == "Open":

                self.canvas = np.zeros(
                    (480,640,3),
                    dtype=np.uint8
                )

                self.previous_point = None

            else:

                self.previous_point = None

        output = cv2.addWeighted(
            img,
            0.6,
            self.canvas,
            0.4,
            0
        )

        cv2.putText(
            output,
            gesture,
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        return av.VideoFrame.from_ndarray(
            output,
            format="bgr24"
        )
# ==========================
# WEBRTC STREAM
# ==========================

ctx = webrtc_streamer(
    key="gesture-ai",
    rtc_configuration=rtc_configuration,
    video_processor_factory=VideoProcessor,
    media_stream_constraints={
        "video": True,
        "audio": False
    },
    async_processing=True,
)
# ==========================
# CONTROLS
# ==========================

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    brush = st.slider(
        "Brush Size",
        2,
        20,
        5
    )

with col2:
    color = st.color_picker(
        "Drawing Color",
        "#00FF00"
    )

with col3:
    if st.button("🗑 Clear Canvas"):

        if ctx.video_processor:

            ctx.video_processor.canvas = np.zeros(
                (480,640,3),
                dtype=np.uint8
            )

rgb = tuple(
    int(color[i:i+2],16)
    for i in (1,3,5)
)

draw_color = (
    rgb[2],
    rgb[1],
    rgb[0]
)

if ctx.video_processor:

    ctx.video_processor.brush = brush

    ctx.video_processor.color = draw_color
# ==========================
# SHOW CANVAS
# ==========================

st.markdown("---")

st.subheader("🎨 Air Canvas")

if ctx.video_processor:

    canvas = cv2.cvtColor(
        ctx.video_processor.canvas,
        cv2.COLOR_BGR2RGB
    )

    st.image(
        canvas,
        channels="RGB"
    )
