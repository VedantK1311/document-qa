import streamlit as st

def load_page(page_file):
    with open(page_file, 'r') as file:
        st.code(file.read())

pages = {
    "Lab 1": lambda: load_page("lab1.py"),
    "Lab 2": lambda: load_page("lab2.py")
}

# Set up the navigation
current_page = st.navigation(pages)

# Execute the selected page function
current_page()
