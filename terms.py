import streamlit as st

def show_terms_and_conditions():
    """Displays a modal-like terms and conditions agreement."""
    st.markdown("""
    # 📋 Terms and Conditions
    
    Welcome to the **TalentScout Hiring Assistant**. Before we begin, please review the following terms regarding your data and this interaction.

    ### 1. Purpose
    This chatbot is an automated hiring assistant designed to screen candidates for technology roles. It uses Artificial Intelligence to generate questions and process your responses.

    ### 2. Data Collection
    We will collect the following information during this session:
    * Full Name, Email, and Phone Number
    * Professional Experience and Tech Stack
    * Responses to technical screening questions

    ### 3. Data Privacy
    * Your data is processed locally on this secure server.
    * We do not share your personal details with third parties without your consent.
    * This session is recorded for recruitment purposes only.

    ### 4. AI Disclaimer
    * The interviewer is an AI, not a human.
    * While we strive for accuracy, AI models can occasionally make errors.
    * A human recruiter will review your final application and conversation log.

    ---
    **By clicking "I Accept", you agree to participate in this automated screening and consent to the data practices described above.**
    """)
    
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("I Accept ✅", type="primary"):
            st.session_state.accepted_terms = True
            st.rerun()  # Reload the app to show the chat interface
    with col2:
        st.write("*Clicking accept will start the interview.*")