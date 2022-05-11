import streamlit as st
from tsunamiml import MultiApp
from apps import home, tsuMadlibs, tsuTEAv1 # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Madlib Generator", tsuMadlibs.app)
app.add_app("Twitter Emotion Analyzer", tsuTEAv1.app)
# The main app
app.run()
