import streamlit as st

def main():
    st.title("TalentScout Hiring Assistant")
    st.write("Welcome! Let's get this chatbot running.")

    # Simple sidebar
    st.sidebar.title("Options")
    
    # Input area
    user_input = st.text_input("Say hello:")
    if user_input:
        st.write(f"You said: {user_input}")

if __name__ == "__main__":
    main()