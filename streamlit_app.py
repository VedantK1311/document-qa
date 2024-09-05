import streamlit as st

pages = {
    "Lab 1": st.Page("lab1.py", title="Lab 1"),
    "Lab 2": st.Page("lab2.py", title="Lab 2")
}

current_page = st.navigation(pages)
current_page.run()
