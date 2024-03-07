import streamlit as st
import requests
import google.generativeai as genai
from PIL import Image

# Replace "YOUR_API_KEY" with your actual API key
genai.configure(api_key="AIzaSyBIO2eJcGH7cfq1Wunw3aG-nndFX9sTm2Q")

model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question)
    return response.text

st.set_page_config(page_title="BOT by Tahseen")

# Inserting background image with gradient purple and white shading
st.markdown(
    """
    <style>
    body {
        background-image: linear-gradient(to bottom right, purple, white);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Styling the text color to be bold and purple
st.markdown(
    "<h1 style='text-align: center; color: purple; font-family: Arial; font-weight: bold;'>An Large language model project by Tahseen Raza</h1>",
    unsafe_allow_html=True
)

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("  Ask Anything?🤔", key="input")

button_container = st.container()

with button_container:
    submit_button = st.button("Get Answer✅")

if submit_button and input_text:
    response = get_gemini_response(input_text)
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader(">>>")
    st.write(response)
    st.session_state['chat_history'].append(("Bot", response))

github_button = '<a href="https://github.com/mdtahseenraza?tab=repositories"><button style="background-color: green; color: white; padding: 10px 15px; border-radius: 5px; border: none; margin-top: 20px; margin-left: 10px;">GitHub</button></a>'
st.markdown(github_button, unsafe_allow_html=True)

linkedin_button = '<a href="https://www.linkedin.com/in/md-tahseen-raza-47726625b/"><button style="background-color: #0077B5; color: white; padding: 10px 15px; border-radius: 5px; border: none; margin-top: 20px; margin-left: 10px;">LinkedIn</button></a>'
st.markdown(linkedin_button, unsafe_allow_html=True)
    
