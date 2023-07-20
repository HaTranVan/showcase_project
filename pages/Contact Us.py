import streamlit as st
import send_email

st.header('Contact Me')

with st.form(key='emails_form'):
    email_add = st.text_input('Your email address')
    message = st.text_area('Your message')
    button = st.form_submit_button('Submit')
    content = f"""\
Subject: Portfolio Contact Form

Email User: {email_add}
{message}
"""
    if button:
        send_email.send_email(content)
