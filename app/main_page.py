import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(
    page_title="Mudita School",
)

show_pages(
    [
        Page("app/main_page.py", "Home", ""),
        Page("app/pages/intake_form.py", "Inquiry", ""),
    ]
)

st.write("# Welcome to Mudita School of Music 👋")


st.markdown(""" Coimbatore's No 1 School of Music

"""
            )