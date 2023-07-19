import streamlit as st
from PIL import Image

col1, col2 = st.columns(2)
with col1:
    st.image('naruto.jpg')

with col2:
    st.title('Ha Tran Van')
    st.text('I am Ha Tran Van. I am 20 years old. \n'
            'I am a Python Developer, programmer,\n'
            ' a students as Economic University, major: E-commerce.\n'
            'I want to become a Professor Python Developer\n'
            'and Data Analytics.I really like working with data.\n'
            'I built some project.')
