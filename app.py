import streamlit as st
from groq import Groq

# paste your groq key here
client = Groq(api_key="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")

st.title("TalentScout Hiring Assistant")

# initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0

if "candidate" not in st.session_state:
    st.session_state.candidate = {}

# function to generate questions
def generate_questions(tech_stack):

    prompt = f"""
    You are a technical interviewer.

    Generate 5 interview questions for each technology listed below:

    Tech Stack: {tech_stack}

    Make questions clear and professional.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# chatbot steps

if st.session_state.step == 0:

    name = st.text_input("Enter your Full Name")

    if name:
        st.session_state.candidate["Name"] = name
        st.session_state.step = 1
        st.rerun()


elif st.session_state.step == 1:

    email = st.text_input("Enter your Email")

    if email:
        st.session_state.candidate["Email"] = email
        st.session_state.step = 2
        st.rerun()


elif st.session_state.step == 2:

    phone = st.text_input("Enter your Phone Number")

    if phone:
        st.session_state.candidate["Phone"] = phone
        st.session_state.step = 3
        st.rerun()


elif st.session_state.step == 3:

    exp = st.text_input("Enter your Years of Experience")

    if exp:
        st.session_state.candidate["Experience"] = exp
        st.session_state.step = 4
        st.rerun()


elif st.session_state.step == 4:

    tech = st.text_input("Enter your Tech Stack (Python, SQL, ML, etc)")

    if tech:
        st.session_state.candidate["Tech Stack"] = tech

        questions = generate_questions(tech)

        st.session_state.questions = questions

        st.session_state.step = 5
        st.rerun()


elif st.session_state.step == 5:

    st.success("Information collected successfully!")

    st.write("### Candidate Details")
    st.write(st.session_state.candidate)

    st.write("### Technical Questions")
    st.write(st.session_state.questions)

    st.write("Thank you! Our team will contact you soon.")