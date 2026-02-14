import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
# Ensure you have OPENAI_API_KEY in your .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# THE SYSTEM PROMPT
# This is where we define the AI's personality and rules.
SYSTEM_PROMPT = """
You are the "TalentScout" Hiring Assistant. Your goal is to screen candidates for technology roles.
Maintain a professional, friendly, and encouraging tone.

YOUR PROCESS:
1. GREETING: Briefly greet the candidate and explain you are here to gather their details and assess their technical skills.

2. INFO GATHERING: You must collect the following details. Do NOT ask for all of them at once. Ask for 1 or 2 items at a time to keep the conversation natural:
   - Full Name
   - Email Address
   - Phone Number
   - Years of Experience
   - Desired Position
   - Current Location
   - Tech Stack (Languages, Frameworks, Tools)

3. TECH SCREENING: Once the user provides their Tech Stack:
   - Generate 3-5 conceptual technical questions based *specifically* on the tools they listed.
   - Do not ask for code snippets, just conceptual understanding.
   - Wait for their answer before moving to the next question or topic.

4. CLOSING: If the user says "Goodbye" or indicates they are done:
   - Thank them for their time.
   - Inform them that a human recruiter will review their profile and contact them.
   - Stop asking questions.

CONSTRAINTS:
- If the user asks irrelevant questions (e.g., "What is the weather?"), politely steer them back to the interview.
- Keep responses concise.
"""

def get_ai_response(messages_history):
    """
    Sends the message history to the LLM and gets a response.
    messages_history format: [{"role": "user", "content": "hi"}, ...]
    """
    try:
        # We prepend the system prompt to the history to ensure the bot knows its role
        full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages_history
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # You can use "gpt-4" if you have access and budget
            messages=full_messages,
            temperature=0.7 # Controls creativity (0.7 is a good balance)
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"