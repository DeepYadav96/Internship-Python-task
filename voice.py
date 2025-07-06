import streamlit as st
from twilio.rest import Client
import base64
import os
# Load environment variables
from dotenv import load_dotenv

load_dotenv()

def set_bg(image_file):
    with open(image_file, "rb") as img_file:
        img_bytes = img_file.read()
        encoded = base64.b64encode(img_bytes).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpg;base64,{encoded}');
            background-size: cover;
        }}
        </style>
    """, unsafe_allow_html=True)

set_bg("Gmail.jpg")

st.title("Twilio Voice Call App")

from_number = st.text_input("Enter your Twilio phone number (with country code)")
to_number = st.text_input("Enter the number you want to call (with country code)")

if st.button("Make Voice Call"):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")  
    auth_token = os.getenv("TWILIO_AUTH_TOKEN") 
    client = Client(account_sid, auth_token)
    if not from_number or not to_number:
        st.warning("Please enter both phone numbers.")
    else:
        try:
            call = client.calls.create(
                to=to_number,
                from_=from_number,
                twiml='<Response><Say>This is a test voice call from Python using Twilio.</Say></Response>'
            )
            st.success(f"Call initiated. SID: {call.sid}")
        except Exception as e:
            st.error(f"Error: {e}")