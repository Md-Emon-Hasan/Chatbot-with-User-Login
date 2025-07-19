import streamlit as st
from db import register_user, login_user
from langchain_gemini import ask_gemini, get_user_memory

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

st.title("🤖 Gemini QA Chatbot (LangChain + XAMPP + Memory)")

if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])
    with tab1:
        uname = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.button("Login"):
            if login_user(uname, pw):
                st.session_state.logged_in = True
                st.session_state.username = uname
                st.success("✅ Login Successful")
            else:
                st.error("❌ Invalid credentials!")

    with tab2:
        uname = st.text_input("New Username")
        pw = st.text_input("New Password", type="password")
        if st.button("Register"):
            if register_user(uname, pw):
                st.success("✅ Registration Successful")
            else:
                st.error("⚠️ Username already exists")
else:
    st.subheader(f"Welcome, {st.session_state.username} 👋")
    memory = get_user_memory(st.session_state.username)
    
    user_input = st.text_input("Ask me anything...")
    if user_input:
        response = ask_gemini(user_input, memory)
        st.markdown(f"**🤖 Gemini:** {response}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
