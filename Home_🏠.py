


# Main page of my portfolio
# %pip install streamlit

import streamlit as st

def run():
    st.set_page_config(
        page_title="Tsunamifi's Python Portfolio",
        page_icon="🧠",
    )

    st.write("# Welcome to my portfolio!")
    st.write("My name is Elton White and I am a 24 year old junior python & cyber security enthusiast")

    st.markdown(
        """
        Here are all of my personal projects built with python!.
       - **👈 Select a project to interact with** 
        ### Contact me!
        - Check me out on [LinkedIn](https://www.linkedin.com/in/whitee)
        
    """
    )


if __name__ == "__main__":
    run()
    
