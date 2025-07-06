import requests
import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="LinkedIn Post Bot", layout="centered")

background_image = Path(__file__).parent / "Gmail.jpg"
if background_image.exists():
    with open(background_image, "rb") as img_file:
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

st.title("Post a Message to LinkedIn")

access_token = st.text_input("Enter your LinkedIn Access Token:", type="password")
user_urn = st.text_input("Enter your LinkedIn User URN (e.g., urn:li:person:xxxx):")
content = st.text_area("Content to post on LinkedIn:", "Hello, LinkedIn! This is an automated post from Python.")

if st.button("Post to LinkedIn"):
    if not access_token or not user_urn or not content:
        st.error("Please fill in all fields.")
    else:
        url = 'https://api.linkedin.com/v2/ugcPosts'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-Restli-Protocol-Version': '2.0.0',
            'Content-Type': 'application/json',
        }
        post_data = {
            "author": user_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": content
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        response = requests.post(url, headers=headers, json=post_data)
        if response.status_code == 201:
            st.success("Post created successfully!")
        else:
            st.error(f"Failed to create post: {response.status_code}")
            st.code(response.text)
