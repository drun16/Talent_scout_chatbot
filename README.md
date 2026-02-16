
# 🤖 TalentScout Hiring Assistant (Local LLM Powered)

**TalentScout** is an intelligent, automated hiring assistant designed to streamline the initial screening process for technology roles. Built with **Streamlit** and powered entirely by a **local Large Language Model (LLM) using Ollama**, it conducts privacy-first, conversational candidate screenings without relying on any external APIs.

This project demonstrates modern AI integration while ensuring **data security, offline capability, and GDPR-friendly design**.

---

## 🚀 Features

* **Interactive Chat Interface**  
  A clean, recruiter-style chat UI built using Streamlit.

* **Automated Candidate Screening**  
  Collects candidate details such as:
  - Name  
  - Years of experience  
  - Tech stack  
  - Role interest  

* **Dynamic Technical Questioning**  
  Generates contextual, role-specific technical questions based on the candidate’s declared tech stack.

* **100% Local AI Processing**  
  Uses **Ollama** with models like **Llama 3 / Mistral**, ensuring no candidate data leaves the local machine.

* **Privacy & Compliance Ready**  
  Includes a mandatory **Terms & Conditions acceptance screen** before the interview begins.

* **Dark Mode / Light Mode Support**  
  Improves accessibility and user experience.

---

## 🛠️ Tech Stack

* **Language:** Python  
* **Frontend:** Streamlit  
* **AI Engine:** Ollama (Local LLM)
  - Llama 3  
  - Mistral  
* **Other Tools:**  
  - `requests` (local model communication)
  - Streamlit session state for chat memory

---

## ⚙️ Installation & Setup

### Prerequisites

* Python **3.8+**
* **Ollama** installed and running  
  👉 https://ollama.com/

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/TalentScout-Chatbot.git
cd TalentScout-Chatbot
````

---

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set Up the Local LLM (Ollama)

1. Install Ollama from:
   👉 [https://ollama.com/](https://ollama.com/)

2. Pull a supported model (example: Llama 3):

```bash
ollama run llama3
```

3. Keep Ollama running in the background.
   The application will automatically communicate with it locally.

✅ **No API keys. No cloud services. No internet dependency.**

---

### 5. Run the Application

```bash
streamlit run app.py
```

Open your browser at:
👉 `http://localhost:8501`

---

## 📖 Usage Guide

1. **Accept Terms & Conditions**
   Mandatory privacy acknowledgment before starting.

2. **Introduction Phase**
   The assistant introduces itself and asks for basic candidate details.

3. **Screening Phase**
   The bot gathers:

   * Experience
   * Technology stack
   * Preferred role

4. **Technical Round**
   Context-aware conceptual questions are generated based on the provided stack.

5. **Exit**
   Type **“Goodbye”** to end the session gracefully.

---

## 🧠 Architectural Decisions

### Why Streamlit?

Streamlit enables:

* Rapid UI development
* Stateful chat handling
* Clean recruiter-friendly interfaces

Its session state management is ideal for conversational AI workflows.

---

### Prompt Engineering Strategy

The system prompt enforces a **recruiter persona** with a controlled interview flow:

1. Greeting
2. Information collection
3. Technical assessment
4. Professional closing

**Constraints applied:**

* No coding challenges
* No irrelevant questions
* High-level conceptual assessment only

---

### Why Ollama (Local LLM)?

Using **Ollama** allows:

* Complete **data privacy**
* Offline execution
* Zero API costs
* Compliance with enterprise & academic privacy expectations

This makes TalentScout suitable for:

* Colleges
* Internal HR tools
* Secure environments

---

## 📂 Project Structure

```text
TalentScout/
│
├── app.py           # Streamlit UI and session handling
├── utils.py         # LLM prompt logic & Ollama interaction
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

## 🚧 Challenges & Solutions

### 🔹 Maintaining Conversation Context

**Problem:**
LLM forgetting earlier responses.

**Solution:**
All messages are stored in `st.session_state.messages` and sent back to the model each turn.

---

### 🔹 Preventing Hallucinations

**Problem:**
Occasional irrelevant or out-of-scope questions.

**Solution:**
Strict role-based system prompt with step-by-step interview flow and negative constraints.

---

## 🤝 Future Enhancements

* Resume PDF upload & parsing
* Candidate scoring & feedback summary
* Database integration for HR dashboards
* Voice-based interview support
* Multi-role hiring workflows

---

## 📌 Key Highlight (For Recruiters)

> 🔐 **TalentScout runs entirely on a local LLM using Ollama — no cloud APIs, no data leakage, and no recurring costs.**

---

**Built with ❤️ by Dharun Prashob M M**

```
