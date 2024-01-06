import streamlit as st
st.set_page_config(page_title="About Us", page_icon="🚗", layout="wide")

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

    st.markdown("<h2 class='about-title'>About Us</h2>", unsafe_allow_html=True)
    st.write("""
    Auto Value Pro is a web application designed to predict the price of a car based on various factors.
    
    #### How it Works:
    - Select the car company, model, year of purchase, fuel type, and other relevant details.
    - Click on the "Predict Car Price" button.
    - The app uses machine learning algorithms to predict the price of the selected car.
    
    _**Disclaimer**: The predictions provided by this app are for reference purposes only. Actual market conditions may vary._

    
    #### Technologies Used:
    - Streamlit
    - Python
    - Machine Learning Libraries (e.g., scikit-learn)
    
     #### Developers:
    - Hitarth Rohra (AM.EN.U4EAC21032)
    - Ansh Grover (AM.EN.U4EAC21015)
    - Amodh Anil (AM.EN.U4EAC21010)
    - Anirudh K (AM.EN.U4EAC21012)
    - Nandana V V (AM.EN.U4EAC21052)  
                    
    **Repository Link**: https://github.com/hitaarthh/Auto-Value-Pro
             
    **Data Set**: https://github.com/hitaarthh/Auto-Value-Pro/tree/main/dataset         
    """)

if __name__ == "__main__":
    main()
