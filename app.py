import streamlit as st

st.title("Data App by Usha sree yadav")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader(":blue[You clicked me]:sunglasses:")
    st.balloons()