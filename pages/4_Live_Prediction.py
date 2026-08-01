import streamlit as st
import cv2
import numpy as np
import os
import sys
import csv

# Project path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from utils.handtracking import HandTracker
from utils.gesture_recognition import GestureRecognition


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Live Prediction | GestureVision AI",
    page_icon="🎯",
    layout="wide"
)


# ==========================
# LOAD CSS
# ==========================

if os.path.exists("style.css"):

    with open("style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# ==========================
# HEADER
# ==========================

st.markdown("""
<div class="hero">

<div class="hero-title">

🎯 Live Gesture Prediction

</div>

<div class="hero-sub">

Real-Time Hand Gesture Recognition + Air Canvas

</div>

</div>
""",
unsafe_allow_html=True)



# ==========================
# INITIALIZE
# ==========================

tracker = HandTracker()

recognizer = GestureRecognition()



if "canvas" not in st.session_state:

    st.session_state.canvas = np.zeros(
        (480,640,3),
        dtype=np.uint8
    )



# ==========================
# CONTROLS
# ==========================

col1,col2,col3=st.columns(3)


with col1:

    start=st.toggle(
        "📷 Start Camera"
    )


with col2:

    brush=st.slider(
        "Brush Size",
        2,
        20,
        5
    )


with col3:

    color=st.color_picker(
        "Drawing Color",
        "#00FF00"
    )



rgb=tuple(
    int(color[i:i+2],16)
    for i in (1,3,5)
)


draw_color=(
    rgb[2],
    rgb[1],
    rgb[0]
)



if st.button("🗑 Clear Canvas"):

    st.session_state.canvas=np.zeros(
        (480,640,3),
        dtype=np.uint8
    )



camera_box=st.empty()

info_box=st.empty()



# ==========================
# CAMERA
# ==========================

if start:


    cap=cv2.VideoCapture(0)


    previous_point=None


    while True:


        success,frame=cap.read()


        if not success:

            st.error(
                "Camera not detected"
            )

            break



        frame=cv2.flip(
            frame,
            1
        )



        frame,landmarks=tracker.detect(
            frame
        )



        gesture="No Hand"



        if landmarks:


            gesture=recognizer.detect(
                landmarks
            )



        cv2.putText(

            frame,

            gesture,

            (20,50),

            cv2.FONT_HERSHEY_SIMPLEX,

            1.5,

            (0,255,0),

            3

        )



        # =====================
        # DRAW MODE
        # =====================


        if gesture=="Pointer":


            point=tracker.index_finger_position(
                landmarks
            )


            if point:


                x,y=point


                if previous_point:


                    cv2.line(

                        st.session_state.canvas,

                        previous_point,

                        (x,y),

                        draw_color,

                        brush

                    )


                previous_point=(x,y)



        # =====================
        # ERASE MODE
        # =====================


        elif gesture=="Open":


            st.session_state.canvas=np.zeros(

                (480,640,3),

                dtype=np.uint8

            )


            previous_point=None



        else:

            previous_point=None




        # Combine camera + canvas

        output=cv2.addWeighted(

            frame,

            0.5,

            st.session_state.canvas,

            0.5,

            0

        )


        output=cv2.cvtColor(

            output,

            cv2.COLOR_BGR2RGB

        )


        camera_box.image(

            output,

            channels="RGB"

        )


        info_box.success(

            f"Detected Gesture : {gesture}"

        )



    cap.release()



# ==========================
# FINAL CANVAS
# ==========================


st.markdown("""
<div class="title">

🎨 Air Canvas Output

</div>
""",
unsafe_allow_html=True)



canvas=cv2.cvtColor(

    st.session_state.canvas,

    cv2.COLOR_BGR2RGB

)


st.image(

    canvas,

    use_container_width=True

)