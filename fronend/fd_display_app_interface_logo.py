import streamlit as st # Import the streamlit library

# Create a function to display the app interface logo
def display_app_interface_logo():
    # add a title to the app
    st.markdown("""
    <style>
    .big-font {
        font-size:100px !important;
        text-align: center;
        color: #000000;
        width: 30%;
        height: 30%;
    }
    </style>
    """, unsafe_allow_html=True)
    st.image("./images/logocalculadorametodosN.png", use_column_width=True)
    