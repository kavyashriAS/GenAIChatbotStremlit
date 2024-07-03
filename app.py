import streamlit as st
from hugging import get_chat_response

# Set up Streamlit interface
st.set_page_config(page_title="Hugging Face Chatbot", layout="wide")

# Login page
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":  # Simple auth check
            st.session_state.logged_in = True
        else:
            st.error("Invalid credentials")

if not st.session_state.logged_in:
    st.title("Login")
    login()
else:
    st.sidebar.title("Chatbot Settings")
    st.title("Hugging Face Chatbot")

    # Chatbot UI
    user_input = st.text_input("You: ", "Hello, how are you?")
    if st.button("Send"):
        response = get_chat_response(user_input)
        st.write(f"Bot: {response}")
