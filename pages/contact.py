import streamlit as st

def main():
    # Custom CSS for styling
    custom_css = """
        <style>
            .about-title {
                color: #FF504D; /* Change text color for the about title */
                text-align: left;
            }
        </style>
    """
    # Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    st.markdown("<h1 class='about-title'>Contact Us</h1>", unsafe_allow_html=True)

    st.write("""
    **For any inquiries or feedback, please contact us at hitarth.rohra@gmail.com**
    """) 
    st.markdown("### Acknowledgments:")
    st.write("We would like to thank the Streamlit community and the developers of the underlying libraries that made this app possible.")

if __name__ == "__main__":
    main()