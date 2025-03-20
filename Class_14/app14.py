import streamlit as st

st.title("Growth Mindset!")
st.header("Header 1")
st.write("This is Growth Mindset Challenge!")
name = st.text_input("Enter Your Name")

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

if st.button("Click Me"):
    st.write(f"My Name is {name}")


st.title("Counter")
if "count" not in st.session_state:
    st.session_state["count"] = 0
    st.session_state.count = 0


st.header(st.session_state.count)

col1, col2  = st.columns(2)

print("count>>>",st.session_state.count)
with col1:
    if st.button("Increment"):
        #        0-> 1 ->2             =    0                  + 1 -> 1 + 1
        st.session_state.count = st.session_state.count + 1

with col2:
   if st.button("Decrement"):
        st.session_state.count = st.session_state.count - 1 