import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "credit risk.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "credit_risk_dataset.csv")

st.title("Dashboard - Credit risk Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

loan_intent = st.selectbox("Select the Loan intent:", df['loan_intent'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['loan_intent'] == loan_intent], x="loan_amnt")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['loan_intent'] == loan_intent], y="loan_amnt")
col2.plotly_chart(fig_2, use_container_width=True)