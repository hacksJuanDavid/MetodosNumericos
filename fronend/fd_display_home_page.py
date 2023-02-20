import streamlit as st # Import the streamlit library

# Create a function to display the app interface home page
def display_home_page():
    # add a title to the app
    st.markdown("""
    <style>
    .big-font {
        font-size:100px !important;
        text-align: center;
        color: #ffffff;
        width: 100%;
        height: 30%;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<h1 class="big-font">Core73🕵🏼</h1>',unsafe_allow_html=True)
    st.image("./images/img.png", use_column_width=True)
