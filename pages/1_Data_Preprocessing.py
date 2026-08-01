import streamlit as st
import pandas as pd
import plotly.express as px
import os


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Data Preprocessing | GestureVision AI",
    page_icon="📊",
    layout="wide"
)


# ==========================
# LOAD CSS
# ==========================

css_path = "style.css"

if os.path.exists(css_path):

    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# ==========================
# TITLE
# ==========================

st.markdown("""
<div class="hero">

<div class="hero-title">

📊 Data Preprocessing

</div>

<div class="hero-sub">

Dataset analysis and preparation for AI gesture recognition

</div>

</div>
""",
unsafe_allow_html=True)


# ==========================
# LOAD DATA
# ==========================

train_path = "datasets/sign_mnist_train.csv"
test_path = "datasets/sign_mnist_test.csv"


@st.cache_data
def load_data():

    train = pd.read_csv(train_path)

    test = pd.read_csv(test_path)

    return train,test



train_df,test_df = load_data()



# ==========================
# DATASET SELECTION
# ==========================

st.sidebar.markdown("## 📂 Dataset")

dataset_choice = st.sidebar.selectbox(
    "Select Dataset",
    [
        "Training Dataset",
        "Testing Dataset"
    ]
)


if dataset_choice=="Training Dataset":

    df=train_df

else:

    df=test_df



# ==========================
# KPI CARDS
# ==========================

st.markdown("<br>",unsafe_allow_html=True)


c1,c2,c3,c4=st.columns(4)


cards=[

    (
        "Rows",
        f"{df.shape[0]:,}"
    ),

    (
        "Columns",
        df.shape[1]
    ),

    (
        "Missing Values",
        df.isnull().sum().sum()
    ),

    (
        "Duplicate Rows",
        df.duplicated().sum()
    )

]


for col,(title,value) in zip(
    [c1,c2,c3,c4],
    cards
):

    with col:

        st.markdown(f"""

        <div class="metric">

        <div class="metric-number">

        {value}

        </div>


        <div class="metric-text">

        {title}

        </div>


        </div>

        """,
        unsafe_allow_html=True)



# ==========================
# DATA PREVIEW
# ==========================


st.markdown("<br>",unsafe_allow_html=True)


st.markdown("""
<div class="card">

<div class="title">

📋 Dataset Preview

</div>

</div>
""",
unsafe_allow_html=True)



st.dataframe(
    df.head(20),
    use_container_width=True
)



# ==========================
# DATA INFORMATION
# ==========================


st.markdown("""
<div class="card">

<div class="title">

🔍 Dataset Information

</div>

</div>
""",
unsafe_allow_html=True)



info_col1,info_col2=st.columns(2)


with info_col1:


    st.markdown(
        "<h3 style='color:#22D3EE'>Column Details</h3>",
        unsafe_allow_html=True
    )


    column_info=pd.DataFrame({

        "Column":df.columns,

        "Data Type":[
            str(x)
            for x in df.dtypes
        ]

    })


    st.dataframe(
        column_info,
        use_container_width=True
    )



with info_col2:


    st.markdown(
        "<h3 style='color:#22D3EE'>Statistics</h3>",
        unsafe_allow_html=True
    )


    st.dataframe(

        df.describe(),

        use_container_width=True

    )



# ==========================
# MISSING VALUES ANALYSIS
# ==========================


st.markdown("<br>",unsafe_allow_html=True)


st.markdown("""
<div class="card">

<div class="title">

📈 Missing Value Analysis

</div>

</div>
""",
unsafe_allow_html=True)



missing = pd.DataFrame({

"Column":df.columns,

"Missing Values":
df.isnull().sum()

})


missing = missing[
    missing["Missing Values"]>0
]



if len(missing)>0:


    fig=px.bar(

        missing,

        x="Column",

        y="Missing Values",

        title="Missing Values"

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


else:


    st.success(
        "✅ No missing values found in dataset"
    )



# ==========================
# LABEL DISTRIBUTION
# ==========================


st.markdown("<br>",unsafe_allow_html=True)


st.markdown("""
<div class="card">

<div class="title">

🎯 Gesture Class Distribution

</div>

</div>
""",
unsafe_allow_html=True)



if "label" in df.columns:


    label_count=df["label"].value_counts().reset_index()

    label_count.columns=[
        "Gesture",
        "Count"
    ]


    fig=px.bar(

        label_count,

        x="Gesture",

        y="Count",

        color="Gesture",

        height=450

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
# DOWNLOAD
# ==========================


st.markdown("<br>",unsafe_allow_html=True)


st.markdown("""
<div class="card">

<div class="title">

⬇ Download Dataset

</div>

</div>
""",
unsafe_allow_html=True)



csv=df.to_csv(index=False)


st.download_button(

    "Download CSV",

    csv,

    "processed_gesture_dataset.csv",

    "text/csv"

)


st.success(
    "✅ Data preprocessing completed successfully"
)