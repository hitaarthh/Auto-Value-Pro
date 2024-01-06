import streamlit as st
st.set_page_config(page_title="Contact Us", page_icon="🚗", layout="wide")

def main():
      # Custom CSS for styling
    custom_css = """
    <style>
    body {
        font-size: 18px;  /* Adjust the font size as needed */
    }
    .about-title {
                color: #FF504D; /* Change text color for the about title */
                text-align: left;
            }
    </style>
    """
    

    # Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    st.sidebar.markdown("You are on the Contact Page")
    st.markdown("<h2 class='about-title'>Contact Us</h2>", unsafe_allow_html=True)

    st.write("""
    **For any inquiries or feedback, please contact us at hitarth.rohra@gmail.com**
    """) 
    st.markdown("#### Acknowledgments:")
    st.write("We would like to thank the Streamlit community and the developers of the underlying libraries that made this app possible.")

if __name__ == "__main__":
    main()