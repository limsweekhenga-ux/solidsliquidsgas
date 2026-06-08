import streamlit as st
import random

# 1. Page Configuration & Title
st.set_page_config(page_title="Matter Explorer Game!", page_icon="🧪", layout="centered")

st.title("🧪 Matter Explorer: The Solid, Liquid & Gas Game!")
st.write("Welcome, Scientist! Test your knowledge on the states of matter and score points!")

# 2. Define the Question Bank (Scenarios & Questions)
# Each question has a scenario, 3 choices, the correct answer, and a kid-friendly explanation.
questions_bank = [
    {
        "question": "You put a glass of water in the freezer overnight. What state of matter does it turn into?",
        "options": ["Solid", "Liquid", "Gas"],
        "correct": "Solid",
        "explanation": "Freezing liquid water turns it into ice, which is a solid! Solids keep their own shape."
    },
    {
        "question": "Look at the steam rising from a hot bowl of soup. What state of matter is that steam?",
        "options": ["Solid", "Liquid", "Gas"],
        "correct": "Gas",
        "explanation": "Steam is water vapor, which is a gas! Gases bounce around and fill up whatever space they are in."
    },
    {
        "question": "You spill some orange juice on the kitchen table. It spreads out into a puddle. What state of matter is it?",
        "options": ["Solid", "Liquid", "Gas"],
        "correct": "Liquid",
        "explanation": "Orange juice is a liquid! Liquids can flow and take the shape of the container (or table!) they are in."
    },
    {
        "question": "Why can you easily push your hand through water, but you can't push your hand through a wooden brick?",
        "options": [
            "Water particles are locked tight, brick particles are loose.",
            "Brick particles are locked tightly together, water particles can slide past each other.",
            "Water is magical."
        ],
        "correct": "Brick particles are locked tightly together, water particles can slide past each other.",
        "explanation": "In a solid brick, particles are packed tight like a wall. In liquid water, particles can slide around your hand!"
    },
    {
        "question": "What happens to the gas inside a balloon if you pop it?",
        "options": [
            "It stays in the exact shape of the balloon.",
            "It turns into a liquid.",
            "It spreads out quickly into the whole room."
        ],
        "correct": "It spreads out quickly into the whole room.",
        "explanation": "Gas particles love freedom! They will spread out to fill up the entire room as soon as they escape."
    },
    {
        "question": "Think about a metal spoon. It doesn't change its shape whether it is in a cup, a bowl, or on the table. Why?",
        "options": ["It is a solid", "It is a liquid", "It is a gas"],
        "correct": "It is a solid",
        "explanation": "Solids have a fixed shape and a fixed volume. They don't change shape just because you move them!"
    }
]

# 3. Initialize Session State Variables
if "score" not in st.session_state:
    st.session_state.score = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "current_q" not in st.session_state:
    # Pick a random question to start
    st.session_state.current_q = random.choice(questions_bank)
if "answered" not in st.session_state:
    st.session_state.answered = False
if "feedback_type" not in st.session_state:
    st.session_state.feedback_type = None
if "feedback_text" not in st.session_state:
    st.session_state.feedback_text = ""

# 4. Scoreboard Display
col1, col2 = st.columns(2)
with col1:
    st.metric(label="⭐ Total Score", value=st.session_state.score)
with col2:
    st.metric(label="🔥 Win Streak", value=st.session_state.streak)

st.write("---")

# 5. Display Current Question
q = st.session_state.current_q

st.subheader("🎯 Your Challenge:")
st.info(q["question"])

# Use a form so the radio button doesn't instantly trigger a reload before clicking submit
with st.form(key="quiz_form"):
    # Fixed version line below for older Streamlit compatibility
    user_choice = st.radio("Choose your answer:", q["options"])
    submit_button = st.form_submit_button(label="Submit Answer 🚀")

# 6. Handle Answer Submission
if submit_button:
    if st.session_state.answered:
        st.warning("You already answered this one! Click 'Next Question' below.")
    else:
        st.session_state.answered = True
        if user_choice == q["correct"]:
            st.session_state.score += 10
            st.session_state.streak += 1
            st.session_state.feedback_type = "success"
            st.session_state.feedback_text = f"🎉 **CORRECT! (+10 points)**\n\n{q['explanation']}"
        else:
            st.session_state.streak = 0  # Reset streak
            st.session_state.feedback_type = "error"
            st.session_state.feedback_text = f"❌ **OOPS! Not quite right.**\n\nThe correct answer was: **{q['correct']}**\n\n{q['explanation']}"

# 7. Show Feedback & Next Button
if st.session_state.answered:
    if st.session_state.feedback_type == "success":
        st.success(st.session_state.feedback_text)
    elif st.session_state.feedback_type == "error":
        st.error(st.session_state.feedback_text)
        
    # Button to move to the next random question
    if st.button("Next Question ➡️"):
        st.session_state.current_q = random.choice(questions_bank)
        st.session_state.answered = False
        st.session_state.feedback_type = None
        st.session_state.feedback_text = ""
        st.rerun()

st.write("---")

# 8. Reset Game Button
if st.button("🔄 Reset Game & Score"):
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.current_q = random.choice(questions_bank)
    st.session_state.answered = False
    st.session_state.feedback_type = None
    st.session_state.feedback_text = ""
    st.success("Game reset! Good luck on your next try!")
    st.rerun()
