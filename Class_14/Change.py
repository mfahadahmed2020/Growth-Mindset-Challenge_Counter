import streamlit as st

st.title("Growth Mindset!")
st.header("Header 1")
st.write("This is growth mindset challenge!")
name = st.text_input("Enter Your Name")
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

if st.button("Click Me"):
    st.write(f"My Name is {name}")

# Counter Section
st.title("Counter")

# Check if 'count' exists in session_state, if not, initialize it
if "count" not in st.session_state:
    st.session_state.count = 0  # Initialize count to 0 if not present

# Display the counter value
st.write(f"Current Count: {st.session_state.count}")

# Create columns for buttons
col1, col2 = st.columns(2)

# Increment button
with col1:
    if st.button("Increment"):
        st.session_state.count += 1  # Increment count
# Decrement button
with col2:
    if st.button("Decrement"):
        st.session_state.count -= 1  # Decrement count