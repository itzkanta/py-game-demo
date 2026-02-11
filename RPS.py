import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮")

st.title("🪨 Rock Paper Scissors Game")

if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0


choices = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}


col1, col2, col3 = st.columns(3)
user_choice = col2.radio("👉 Choose your move:", choices, horizontal=True)

play_col, reset_col = st.columns([3, 1])
play_clicked = play_col.button("🎯 Play")
reset_clicked = reset_col.button("🔄 Reset Score")

if reset_clicked:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.success("Scores reset!")


if play_clicked:
    computer_choice = random.choice(choices)
    st.write(f"💻 Computer chose: {emojis[computer_choice]} **{computer_choice}**")

    if user_choice == computer_choice:
        st.info("🤝 It's a TIE!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        st.success("🎉 YOU WIN!")
        st.session_state.user_score += 1
    else:
        st.error("💻 COMPUTER WINS!")
        st.session_state.computer_score += 1


st.markdown("---")
st.subheader("📊 Scoreboard")
st.write(f"**You:** {st.session_state.user_score} 🧑‍💻")
st.write(f"**Computer:** {st.session_state.computer_score} 💻")

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Built with ❤️ using Streamlit and Python")