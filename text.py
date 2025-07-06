import streamlit as st
from twilio.rest import Client
import base64

# Set page config
st.set_page_config(page_title="Send SMS via Twilio", layout="centered")

# Set background image using local file
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

st.title("Send SMS using Twilio")

TWILIO_ACCOUNT_SID = st.text_input("Twilio Account SID", type="password")
TWILIO_AUTH_TOKEN = st.text_input("Twilio Auth Token", type="password")
FROM_NUMBER = st.text_input("From Number")
TO_NUMBER = st.text_input("To Number")
MESSAGE_BODY = st.text_area("Message")

if st.button("Send SMS"):
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, FROM_NUMBER, TO_NUMBER, MESSAGE_BODY]):
        st.error("Please fill in all fields.")
    else:
        try:
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                body=MESSAGE_BODY,
                from_=FROM_NUMBER,
                to=TO_NUMBER
            )
            st.success(f"SMS sent successfully using Twilio! SID: {message.sid}")
        except Exception as e:
            st.error(f"Failed to send SMS using Twilio: {e}")