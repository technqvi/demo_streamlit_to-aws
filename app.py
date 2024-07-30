import streamlit as st #all streamlit commands will be available through the "st" alias

# set page config and title of the app streamlit 
st.set_page_config(page_title="My First Streamlit App", layout="wide")
st.title("Streamlit Demo") #page title

color_text = st.text_input("Question") #display a text box
go_button = st.button("Go", type="primary") #display a primary button


if go_button:
    st.write(f"Your question is {color_text} ")
