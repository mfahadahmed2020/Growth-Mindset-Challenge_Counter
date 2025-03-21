import streamlit as st

st.title("I Am Fahad Ahmed My First Streamlit App ")
st.header("""خوش آمدید رمضان""")

user = st.text_input("What is Your Name ? | تمہارا نام کیا ہے ؟ ")
if user:
    st.write("السلام و علیکم رمضان", user )

agree = st.checkbox("Agree With Me?")
if agree:
    st.write("Lets Goo!", user)
 

if st.button("Click Me!"):
    st.success(f"رمضان مبارک ہو تمہیں {user}.") 

st.subheader("Dou You Wanna Play Number Guessing Game ?")

import random 
if "Get_Started" not in st.session_state:
    st.session_state.get_started = False

if st.button("Yes"):
    st.session_state.get_started = True
    if "Number" not in st.session_state:
        st.session_state.number = random.randint(1, 10)

if st.session_state.get_started:
    st.header("🎲 Guess The Number Game Begin...")

    guess = st.number_input("Enter a Number Between 1 to 10: ", min_value = 1, max_value = 10, step = 1)

    if st.button("Guess"):
        if guess > st.session_state.number:
            st.warning("Sorry Too High.")
        elif guess < st.session_state.number:
            st.warning("Sorry Too Low.")
        else:
         st.success("Yayy! You Guess The Right Number.")
         st.session_state.number = random.randint(1, 10)

if st.button("No"):
    st.session_state.get_started = False
    st.write("Okay! As You Want.")



st.title("Growth Mindset! Counter...")
st.header("Welcome To Counter.")
st.write("This is Growth Mindset Challenge!")

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