import streamlit as st

# Title of the app
st.title("Simple Input App")

# Take user input
user_input = st.text_input("Enter something:")

# Display the user input
if user_input:
    st.write("You entered:", user_input)
