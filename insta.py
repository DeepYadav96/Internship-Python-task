import streamlit as st
from instagrapi import Client
import os
import base64

# Set background image using custom CSS
GMAIL_IMAGE = "Gmail.jpg"
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

if os.path.exists(GMAIL_IMAGE):
    set_bg(GMAIL_IMAGE)

st.title("Instagram Photo Uploader")

username = st.text_input("Instagram Username")
password = st.text_input("Instagram Password", type="password")
caption = st.text_area("Caption", "This post is by using Python! ")
image_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if st.button("Upload to Instagram"):
    if not username or not password or not image_file:
        st.error("Please provide all required fields.")
    else:
        # Save uploaded file to disk
        image_path = os.path.join("temp_" + image_file.name)
        with open(image_path, "wb") as f:
            f.write(image_file.getbuffer())
        try:
            cl = Client()
            cl.login(username, password)
            cl.photo_upload(image_path, caption)
            st.success("Post uploaded successfully.")
        except Exception as e:
            st.error(f"Failed to upload: {e}")
        finally:
            if os.path.exists(image_path):
                os.remove(image_path)