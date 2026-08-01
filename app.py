import streamlit as st

# ======================================
# PAGE CONFIGURATION
# ======================================

st.set_page_config(
    page_title="GestureVision AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================
# CUSTOM CSS
# ======================================

st.markdown("""
<style>

/* Hide only Streamlit menu and footer */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* DO NOT HIDE HEADER */
/* header{
    visibility:hidden;
} */

/* Background */
.stApp{
background:linear-gradient(135deg,#020617,#0f172a,#1e293b);
}

/* Sidebar */

section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#020617,#111827);
}

section[data-testid="stSidebar"] *{
color:white !important;
}

/* Hero Section */

.hero{
background:linear-gradient(135deg,#1e293b,#0f172a);
padding:45px;
border-radius:20px;
text-align:center;
border:1px solid rgba(255,255,255,.12);
margin-bottom:35px;
}

.badge{
display:inline-block;
padding:10px 22px;
background:#2563eb;
color:white;
font-size:14px;
font-weight:bold;
border-radius:30px;
margin-bottom:20px;
}

.hero-title{
font-size:60px;
font-weight:900;
color:#38bdf8;
}

.hero-subtitle{
font-size:22px;
color:#e2e8f0;
margin-top:15px;
}

/* Feature Cards */

.feature-card{
background:rgba(255,255,255,.08);
backdrop-filter:blur(12px);
border:1px solid rgba(255,255,255,.1);
border-radius:20px;
padding:25px;
height:240px;
transition:.3s;
}

.feature-card:hover{
transform:translateY(-6px);
}

.feature-card h3{
color:#38bdf8;
}

.feature-card p{
color:#f1f5f9;
font-size:17px;
line-height:1.7;
}

/* Information Cards */

.info-card{
background:rgba(255,255,255,.08);
padding:30px;
border-radius:20px;
border:1px solid rgba(255,255,255,.1);
margin-top:30px;
}

.info-card h2{
color:#38bdf8;
}

.info-card p{
color:white;
font-size:18px;
line-height:1.8;
}

/* Metric Cards */

div[data-testid="metric-container"]{
background:rgba(255,255,255,.08);
border-radius:15px;
padding:15px;
}

</style>
""", unsafe_allow_html=True)

# ======================================
# SIDEBAR
# ======================================

st.sidebar.title("🤖 GestureVision AI")

st.sidebar.markdown("""
### Navigation

🏠 Home Dashboard

📊 Data Preprocessing

📈 Exploratory Data Analysis

🧠 Model Training

🎥 Live Gesture Recognition

🎨 AI Air Canvas

---

### Technologies

🐍 Python

🎥 OpenCV

✋ MediaPipe

🧠 TensorFlow Lite

🌐 Streamlit
""")
# ======================================
# HERO SECTION
# ======================================

st.markdown("""
<div class="hero">

<div class="badge">
🚀 AI Powered Computer Vision Platform
</div>

<div class="hero-title">
🤖 GestureVision AI
</div>

<div class="hero-subtitle">
Hand Gesture Recognition & Interactive AI Air Canvas
</div>

</div>
""", unsafe_allow_html=True)

st.write("")

# ======================================
# PROJECT STATISTICS
# ======================================

st.markdown("""
<h2 style="
color:#38bdf8;
font-size:42px;
font-weight:800;
margin-bottom:25px;
">
📊 Project Statistics
</h2>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card" style="height:170px;text-align:center;">
        <h3 style="color:white;">🎯 Accuracy</h3>
        <h1 style="color:white;font-size:50px;">98%</h1>
        <p style="color:#22c55e;font-size:20px;">⬆ High</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card" style="height:170px;text-align:center;">
        <h3 style="color:white;">✋ Gestures</h3>
        <h1 style="color:white;font-size:50px;">10+</h1>
        <p style="color:#22c55e;font-size:20px;">⬆ Supported</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card" style="height:170px;text-align:center;">
        <h3 style="color:white;">⚡ Speed</h3>
        <h1 style="color:white;font-size:50px;">30 FPS</h1>
        <p style="color:#22c55e;font-size:20px;">⬆ Realtime</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card" style="height:170px;text-align:center;">
        <h3 style="color:white;">📷 Webcam</h3>
        <h1 style="color:white;font-size:50px;">Live</h1>
        <p style="color:#22c55e;font-size:20px;">⬆ Enabled</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ======================================
# WELCOME MESSAGE
# ======================================

st.markdown("""
<div class="info-card">

<h2>👋 Welcome to GestureVision AI</h2>

<p>

GestureVision AI is an advanced Computer Vision project that
recognizes hand gestures in real time and enables users to draw
on a virtual Air Canvas without touching the screen.

This project combines Artificial Intelligence, Machine Learning,
MediaPipe, OpenCV, TensorFlow Lite and Streamlit to provide
a smooth and interactive user experience.

</p>

</div>
""", unsafe_allow_html=True)

st.write("")
# ======================================
# FEATURE CARDS
# ======================================

st.markdown("""
<h2 style="
color:#38bdf8;
font-size:42px;
font-weight:800;
margin-top:25px;
margin-bottom:25px;
">
🚀 Core Features
</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">

    <h3>✋ Hand Tracking</h3>

    <p>
    Detects 21 hand landmarks in real time using
    Google's MediaPipe framework for accurate
    hand movement tracking.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">

    <h3>🧠 AI Recognition</h3>

    <p>
    Uses TensorFlow Lite and Machine Learning
    to recognize hand gestures accurately
    with real-time prediction.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">

    <h3>🎨 AI Air Canvas</h3>

    <p>
    Draw naturally in the air using
    finger movements without touching
    the computer screen.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ======================================
# PROJECT OVERVIEW
# ======================================

st.markdown("""
<div class="info-card">

<h2>🚀 Project Overview</h2>

<p>

GestureVision AI is an AI-powered computer vision application
that enables users to interact with a computer using only hand gestures.

The system captures live video through a webcam, detects hand landmarks
using MediaPipe, recognizes gestures using a TensorFlow Lite model,
and allows users to draw on an interactive Air Canvas.

The project demonstrates how Artificial Intelligence and Computer Vision
can provide a touch-free and natural human-computer interaction experience.

</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ======================================
# TECHNOLOGY STACK
# ======================================

st.markdown("""
<div class="info-card">

<h2>🛠 Technology Stack</h2>

<p>

🐍 <b>Python</b> – Main programming language<br><br>

🎥 <b>OpenCV</b> – Webcam video capture and image processing<br><br>

✋ <b>MediaPipe</b> – Real-time hand landmark detection<br><br>

🧠 <b>TensorFlow Lite</b> – Gesture recognition model<br><br>

🌐 <b>Streamlit</b> – Interactive web application interface<br><br>

📊 <b>Machine Learning</b> – Hand gesture classification

</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ======================================
# PROJECT OBJECTIVES
# ======================================

st.markdown("""
<div class="info-card">

<h2>🎯 Project Objectives</h2>

<p>

✅ Develop a touch-free drawing system using hand gestures.<br><br>

✅ Recognize sign language gestures in real time.<br><br>

✅ Improve human-computer interaction using AI.<br><br>

✅ Build a simple, interactive, and user-friendly interface.<br><br>

✅ Demonstrate the applications of Computer Vision in daily life.

</p>

</div>
""", unsafe_allow_html=True)
# ======================================
# PROFESSIONAL FOOTER
# ======================================

st.write("")
st.write("")
st.markdown("---")

st.markdown("""
<style>

.footer{
    text-align:center;
    padding:25px;
    margin-top:20px;
    color:#cbd5e1;
    font-size:16px;
    line-height:1.8;
}

.footer-title{
    color:#38bdf8;
    font-size:22px;
    font-weight:bold;
    margin-bottom:10px;
}

.footer-credit{
    color:#94a3b8;
    font-size:15px;
}

.footer-tech{
    color:#f8fafc;
    font-size:15px;
}

</style>

<div class="footer">

<div class="footer-title">
🤖 GestureVision AI
</div>

<div class="footer-tech">
Built with ❤️ using <b>Python</b> • <b>OpenCV</b> • <b>MediaPipe</b> • <b>TensorFlow Lite</b> • <b>Streamlit</b>
</div>

<br>

<div class="footer-credit">
© 2026 GestureVision AI. All Rights Reserved.
</div>

<div class="footer-credit">
Designed & Developed for AI Hand Gesture Recognition and Air Canvas Project.
</div>

</div>
""", unsafe_allow_html=True)