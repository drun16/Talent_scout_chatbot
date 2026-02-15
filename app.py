
import streamlit as st
from utils import get_ai_response


def main():
    st.set_page_config(page_title="TalentScout AI", page_icon="🤖")
    st.title("🤖 TalentScout Hiring Assistant")
    st.markdown("Welcome! I am here to help you with your initial screening.")
    # 1. Initialize Chat History
    # We check if 'messages' exists in session_state. If not, we create it.
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "assistant", "content": "Hello! I am your Local Hiring Assistant. What is your name?"})
    # 2. Display Chat History
    # This loop draws the previous messages every time the app refreshes
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("Type here..."):
        with st.chat_message("user"):
    # B. Save User Message to History        
            st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Processing locally... (may take a few seconds)"):
            ai_reply = get_ai_response(st.session_state.messages)
    # D. Display AI Message
        with st.chat_message("assistant"):
            st.markdown(ai_reply)

        # E. Save AI Message to History
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})

if __name__ =="__main__":
    main()
