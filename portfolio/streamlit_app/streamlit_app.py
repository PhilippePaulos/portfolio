import streamlit as st

home_page = st.Page("app_pages/home.py", icon="👋", title="Home")
snake_page = st.Page("app_pages/snake.py", icon="🐍", title="Snake")
about_page = st.Page("app_pages/about.py", icon="💬", title="About")

pg = st.navigation([home_page, snake_page, about_page])
pg.run()
