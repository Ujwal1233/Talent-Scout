🤖 TalentScout – AI Hiring Assistant Chatbot

An intelligent Hiring Assistant chatbot built using Python + Streamlit + LLM API that helps screen candidates for technical roles.

This chatbot simulates the initial hiring round for TalentScout, a fictional recruitment agency specializing in technology placements.

📌 Project Overview

The Hiring Assistant chatbot:

1. Greets candidates professionally

2. Collects essential candidate information

3. Asks candidates to declare their tech stack

4. Generates 3–5 technical questions based on their technologies

5. Maintains conversational context

6. Handles fallback responses

7. Ends conversation gracefully

This project demonstrates:

1. Prompt engineering skills

2. Context-aware LLM interactions

3. Clean UI development using Streamlit

4. Secure and structured data handling

🏗️ Project Structure
TalentScout-Hiring-Assistant/
│
├── app.py          
├── text_api.py     
└── README.md


⚙️ Tech Stack

1. Python 3.9+

2. Streamlit – Frontend UI

3. OpenAI / LLM API – Language Model

4. python-dotenv – Environment variable management


🚀 Installation Instructions
1️⃣ Clone the Repository
  git clone https://github.com/your-username/TalentScout-Hiring-Assistant.git
  cd TalentScout-Hiring-Assistant
2️⃣ Create Virtual Environment (Recommended)
  python -m venv venv

Activate:

  Windows

  venv\Scripts\activate

  Mac/Linux

  source venv/bin/activate
3️⃣ Install Dependencies
  pip install -r requirements.txt

4️⃣ Add API Key
  Create a .env file in the root folder:

  OPENAI_API_KEY=your_api_key_here
  
▶️ Run the Application
  streamlit run app.py

  The app will open at:

  http://localhost:8501

  
💡 How It Works
1️⃣ Greeting Phase

The chatbot introduces itself as TalentScout Hiring Assistant.

2️⃣ Information Gathering

It collects:

. Full Name

. Email Address

. Phone Number

. Years of Experience

. Desired Position(s)

. Current Location

. Tech Stack

3️⃣ Tech Stack Declaration

The candidate specifies technologies such as:

. Programming Languages

. Frameworks

. Databases

. Tools

4️⃣ Technical Question Generation

Based on declared tech stack, the model generates:

. 3–5 technical questions per technology

. Questions tailored to experience level

. Context-aware follow-ups if needed

5️⃣ Context Management

Conversation history is preserved using Streamlit session state.

6️⃣ Fallback Mechanism

If input is unclear:

. The chatbot asks for clarification

. Does not deviate from hiring purpose

7️⃣ End Conversation

Typing keywords like:

. exit
. quit
. bye

Gracefully ends the session and thanks the candidate.


🧠 Prompt Engineering Strategy

Prompts are structured in two layers:

🔹 System Prompt

Defines:

. Role as Hiring Assistant

. Professional tone

. Purpose restriction (no off-topic discussions)

🔹 Dynamic Prompt

Includes:

. Candidate details

. Tech stack

. Instructions to generate relevant technical questions

Example Logic:

Generate 3-5 technical questions to assess proficiency in:
- Python
- Django
- MySQL

Keep difficulty aligned with 3 years of experience.
Key Prompt Design Goals

Clarity

Controlled output format

Context awareness

No deviation from hiring scope


🔐 Data Handling & Privacy

Uses simulated data storage

No real database used

API key secured via environment variables

Designed keeping GDPR principles in mind


🧩 Architecture Overview
User → Streamlit UI (app.py)
        ↓
Prompt Construction
        ↓
LLM API Call (text_api.py)
        ↓
Response Processing
        ↓
Displayed in Chat Interface

app.py handles UI & session state

text_api.py handles API interaction and prompt generation


⚠️ Challenges Faced & Solutions

Challenge	with Solution
Maintaining conversation context :-	Used Streamlit session state
Generating relevant questions dynamically	:- Structured prompt templates
Preventing chatbot deviation :-	Strong system role instructions
Handling unexpected input :-	Added fallback response logic


📊 Evaluation Criteria Covered

✔ Technical Proficiency
✔ Effective Prompt Engineering
✔ Context Handling
✔ Clean UI
✔ Data Privacy Awareness
✔ Structured & Readable Code

