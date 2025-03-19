import streamlit as st

# Set the page layout
st.set_page_config(page_title="Sign Language WebApp", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        flex-direction: column;
        height: 100vh;
    }
    .button {
        background-color: black;
        color: white;
        justify-content: center;
        align-items: center;
        padding: 15px 100px;
        font-size: 18px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
    }
    .button:hover {
        background-color: #333333;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state['page'] = 'main_page'

# Define the main page
def main_page():
    st.markdown('<div class="center">', unsafe_allow_html=True)
    st.image(r"assets\Sign Language UI.png", use_container_width=True)
    st.title("American Sign Language")
    if st.button("Start", key="first_image_button"):
        st.session_state['page'] = 'first_image'
    st.markdown('</div>', unsafe_allow_html=True)

# Define the first image page
def first_image_page():
    st.title("First Image")
    st.image(r"assets\Signs-Part1.jpg", use_container_width=True)
    if st.button("Next", key="second_image_button"):
        st.session_state['page'] = 'second_image'

# Define the second image page
def second_image_page():
    st.title("Second Image")
    st.image(r"assets\Signs -Part2.jpg", use_container_width=True)
    if st.button("Back to Home", key="back_home_button"):
        st.session_state['page'] = 'main_page'

# Render the appropriate page based on session state
if st.session_state['page'] == 'main_page':
    main_page()
elif st.session_state['page'] == 'first_image':
    first_image_page()
elif st.session_state['page'] == 'second_image':
    second_image_page()
