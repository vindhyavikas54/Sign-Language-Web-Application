import streamlit as st

# Define the main page
def main_page():
    # Custom CSS for centering and styling
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
            color:black;
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

    # Center the content and button
    st.markdown('<div class="center">', unsafe_allow_html=True)
    
    # Add image and title
    st.image(r"C:\Users\M.V.Vindhya\OneDrive\Desktop\WEB APP\Sign Language UI.png", use_container_width=True)
    st.title("American Sign Language")

    # Create a Streamlit button
    if st.button("Start", key="start_button"):
        st.session_state['page'] = 'next_page'

    st.markdown('</div>', unsafe_allow_html=True)

# Define the next page
def next_page():
    st.title("Next Page")
    st.write("You have successfully navigated to the next page!")
    st.image(r"C:\Users\M.V.Vindhya\OneDrive\Desktop\WEB APP\American Sign Language Signs.jpg", use_container_width=True)

# Set the page layout
st.set_page_config(page_title="Sign Language WebApp", layout="centered")

# Use session state to manage navigation
if 'page' not in st.session_state:
    st.session_state['page'] = 'main_page'

# Render the appropriate page based on session state
if st.session_state['page'] == 'main_page':
    main_page()
elif st.session_state['page'] == 'next_page':
    next_page()
