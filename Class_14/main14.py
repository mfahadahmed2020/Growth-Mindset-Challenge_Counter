import streamlit as st

st.title("Welcome to Streamlit Class")
name = st.text_input("Enter your name")
if st.button("Say Hi"):
    st.write(f"Hello, {name}! Welcome to Streamlit! 😊")

st.title("🔢 Simple Counter App")

if "count" not in st.session_state: st.session_state.count = 0
# Display the counter value

st.write(f"Current Count: {st.session_state.count}")

col1, col2 = st.columns(2)

with col1:
    if st.button("Increase + "): st.session_state.count = st.session_state.count + 1

with col2:
    if st.button("Decrease + "): st.session_state.count = st.session_state.count - 1