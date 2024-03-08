import base64
import streamlit as st
import google.generativeai as genai

# Replace "YOUR_API_KEY" with your actual API key
genai.configure(api_key="AIzaSyBbk9sTnlsOR_qC2PNPzftt_QKvskLJYnI")

# Call set_page_config() at the beginning
st.set_page_config(page_title="BOT by Tahseen!")

# Function to read image file and convert to base64
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image.jpeg")

# Background image and styling
page_bg_img = f"""
<style>
/* Set background image for the main content area */
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://images.unsplash.com/photo-1589859762194-eaae75c61f64?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: 250%;
    background-attachment: local;
}}

/* Set background image for the sidebar */
[data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-attachment: fixed;
}}

/* Set background color and text color for the header, toolbar, and sidebar */
[data-testid="stHeader"],
[data-testid="stToolbar"],
.sidebar-content {{
    background-color: rgba(0, 0, 0, 0);
    color: white;
}}
</style>
"""

# Apply background image and styling
st.markdown(page_bg_img, unsafe_allow_html=True)

# App content
st.title("An LLM based bot by Tahseen....😉")

# Sidebar content
st.sidebar.header("About me!")
st.sidebar.markdown(
    """
    I'm Tahseen Raza, a data scientist and a language chain developer. 
    I'm passionate about building AI-powered solutions and exploring new technologies.
    """
)

# Initialize the generative model
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

# Function to get response from the generative model
def get_gemini_response(question):
    response = chat.send_message(question)
    return response.text

# Get user input
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("  Ask Anything?🤔", key="input")

# Button to submit the input
button_container = st.container()
with button_container:
    submit_button = st.button("Get Answer✅")

# Process input and get response
if submit_button and input_text:
    response = get_gemini_response(input_text)
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader(">>>")
    st.write(response)
    st.session_state['chat_history'].append(("Bot", response))

# Features of this bot
st.markdown("### Features of this bot")
st.markdown("""
- You can ask anything, and you will get an answer on any topic.
- Provides guidance for studies and interview questions.
- Continuously evolving with more features added over time.
""")

# GitHub and LinkedIn buttons
github_button = '<a href="https://github.com/mdtahseenraza?tab=repositories"><button style="background-color: green; color: white; padding: 10px 15px; border-radius: 5px; border: none; margin-top: 20px; margin-left: 10px;">GitHub</button></a>'
st.markdown(github_button, unsafe_allow_html=True)

linkedin_button = '<a href="https://www.linkedin.com/in/md-tahseen-raza-47726625b/"><button style="background-color: #0077B5; color: white; padding: 10px 15px; border-radius: 5px; border: none; margin-top: 20px; margin-left: 10px;">LinkedIn</button></a>'
st.markdown(linkedin_button, unsafe_allow_html=True)
