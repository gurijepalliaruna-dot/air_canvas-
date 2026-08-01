import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import os
import numpy as np


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="EDA | GestureVision AI",
    page_icon="📈",
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

📈 Exploratory Data Analysis

</div>

<div class="hero-sub">

Visual analysis of Sign Language Gesture Dataset

</div>

</div>
""",
unsafe_allow_html=True)



# ==========================
# LOAD DATA
# ==========================

@st.cache_data
def load_data():

    train=pd.read_csv(
        "datasets/sign_mnist_train.csv"
    )

    return train



df=load_data()



# ==========================
# SUMMARY CARDS
# ==========================

st.write("")


c1,c2,c3,c4=st.columns(4)


summary=[

("Total Samples",f"{len(df):,}"),

("Features",df.shape[1]-1),

("Gesture Classes",df["label"].nunique()),

("Pixel Features","784")

]


for col,(name,value) in zip(
    [c1,c2,c3,c4],
    summary
):

    with col:

        st.markdown(f"""

<div class="metric">

<div class="metric-number">

{value}

</div>

<div class="metric-text">

{name}

</div>

</div>

""",
unsafe_allow_html=True)



# ==========================
# LABEL DISTRIBUTION
# ==========================


st.markdown("<br>",unsafe_allow_html=True)


st.markdown("""
<div class="title">
🎯 Gesture Class Distribution
</div>
""",
unsafe_allow_html=True)



class_count=df["label"].value_counts().reset_index()

class_count.columns=[
    "Gesture",
    "Count"
]


fig=px.bar(

    class_count,

    x="Gesture",

    y="Count",

    color="Count",

    text="Count",

    height=450

)


fig.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font_color="white",

    xaxis_title="Gesture Label",

    yaxis_title="Number of Images"

)


st.plotly_chart(
    fig,
    use_container_width=True
)



# ==========================
# SAMPLE IMAGES
# ==========================


st.markdown("<br>",unsafe_allow_html=True)


st.markdown("""
<div class="title">
✋ Sample Hand Gesture Images
</div>
""",
unsafe_allow_html=True)



sample=df.sample(12)



cols=st.columns(6)


for col,(_,row) in zip(
    cols*2,
    sample.iterrows()
):

    with col:

        image=row.drop("label").values

        image=image.reshape(28,28)


        st.image(
            image,
            caption=f"Gesture {row['label']}",
            width=120
        )



# ==========================
# PIXEL DISTRIBUTION
# ==========================


st.markdown("<br>",unsafe_allow_html=True)


st.markdown("""
<div class="title">
📊 Pixel Intensity Distribution
</div>
""",
unsafe_allow_html=True)



pixels=df.drop(
    "label",
    axis=1
).values.flatten()



pixel_df=pd.DataFrame({

"Pixel Value":pixels

})


fig=px.histogram(

    pixel_df,

    x="Pixel Value",

    nbins=50,

    height=400

)


fig.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font_color="white"

)


st.plotly_chart(
    fig,
    use_container_width=True
)



# ==========================
# CORRELATION HEATMAP
# ==========================


st.markdown("<br>",unsafe_allow_html=True)


st.markdown("""
<div class="title">
🔥 Feature Correlation Analysis
</div>
""",
unsafe_allow_html=True)



sample_corr=df.sample(500)


corr=sample_corr.corr()



fig=px.imshow(

    corr,

    height=650,

    color_continuous_scale="Viridis"

)


fig.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    font_color="white"

)



st.plotly_chart(
    fig,
    use_container_width=True
)



# ==========================
# INSIGHTS
# ==========================


st.markdown("<br>",unsafe_allow_html=True)


st.markdown("""
<div class="card">

<div class="title">
💡 EDA Insights
</div>


<div class="text">

✔ Dataset contains multiple hand gesture classes.

<br>

✔ Each image is represented using 784 pixel features.

<br>

✔ Data distribution is analysed before model training.

<br>

✔ Visualization helps understand gesture patterns.

<br>

✔ Clean and balanced data improves AI model performance.

</div>

</div>

""",
unsafe_allow_html=True)