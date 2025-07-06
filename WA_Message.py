import pywhatkit
import time
import pyautogui
import streamlit as st
import base64

# Set background image using local Gmail.jpg
with open("Gmail.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpg;base64,{encoded_string}');
            background-size: cover;
        }}
        </style>
    """, unsafe_allow_html=True)

st.title("WhatsApp Message Sender")

phone = st.text_input("Enter phone number (with country code):", value="+91")
message = st.text_area("Enter your message:", value="Hello, this is a test message!")
hour = st.number_input("Hour (24-hour format):", min_value=0, max_value=23, value=4)
minute = st.number_input("Minute:", min_value=0, max_value=59, value=50)

if st.button("Send Message"):
    try:
        pywhatkit.sendwhatmsg(phone, message, int(hour), int(minute))
        st.success("Message scheduled! Please wait for the browser to open and send the message.")
        time.sleep(10)
        pyautogui.hotkey('ctrl', 'w')
        st.info("WhatsApp Web tab closed.")
    except Exception as e:
        st.error(f"An error occurred: {e}")