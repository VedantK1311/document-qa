import streamlit as st
from lab1 import run_lab1
from lab2 import run_lab2

# Define pages using Streamlit's Page object (assuming Streamlit version >= 1.12)
pages = {
    "Lab 1": st.Page(run_lab1, title="Lab 1"),
    "Lab 2": st.Page(run_lab2, title="Lab 2")
}

# Setup the navigation
current_page = st.navigation(pages)

# Execute the function associated with the current page
current_page.run()
