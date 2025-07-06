import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

# Function to set background from image file
# 'image_file' is the filename of the background image (e.g., 'Gmail.jpg')
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{encoded}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background using image file (Gmail.jpg)
set_bg("Gmail.jpg")

st.title("Send Email with Python (Streamlit App)")

with st.form("email_form"):
    sender_email = st.text_input("Your Gmail address")
    password = st.text_input("App Password", type="password")
    receiver_email = st.text_input("Recipient's Email")
    subject = st.text_input("Subject", value="Test Email from Python")
    body = st.text_area("Message", value="Hello,\n\nThis is a test email sent from a Python Streamlit app!\n\nBest regards.")
    submitted = st.form_submit_button("Send Email")

if submitted:
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")