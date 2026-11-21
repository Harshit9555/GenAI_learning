# 1.  Basics Streamlit App 
import streamlit as st
st.title("Welcome to  Streamlit !")
text = st.text_input("Enter your name:")
st.write(text)
if st.button("Greet Me"):
    st.write("Hello !")
