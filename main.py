import streamlit as st
import random


# Title
st.title("🎯 Number Guessing Game")
st.write("Guess a number between 1 and 100!")

# Initialize random number in session state
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check guess
if st.button("Check Guess"):
    if guess < st.session_state.random_number:
        st.warning("Try a higher number! 🔼")
    elif guess > st.session_state.random_number:
        st.warning("Try a lower number! 🔽")
    else:
        st.success("🎉 Congratulations! You guessed it right!")
        st.balloons()
        st.session_state.random_number = random.randint(1, 100)  # Reset game
