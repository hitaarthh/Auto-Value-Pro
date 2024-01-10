import streamlit as st
st.set_page_config(page_title="About Us", page_icon="🚗", layout="wide")


def main():
    # Custom CSS for styling
    custom_css = """
    <style>
    body {
        font-size: 18px;  /* Adjust the font size as needed */
    }

    .about-title {
                color: #FF504D; /* Change text color for the about title */
                text-align: center;
            }
    </style>
    """

    # Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    st.sidebar.markdown("You are on the About Page")

    st.markdown("<h1 class='about-title'>About Us</h1>", unsafe_allow_html=True)
    st.write("""
    ###### Auto Value Pro, an advanced web app, predicts car prices using sophisticated machine learning. Users input details like make, model, and year, initiating dynamic analysis with models like Linear Regression as default.

    ###### Ensemble models, including Decision Tree, Random Forest, Gradient Boosting, and Support Vector Machine, enhance accuracy. The app selects the best model for each scenario, ensuring precision tailored to each car.

    ###### While providing valuable insights, users are encouraged to see predictions as references. Real-world variations influenced by factors underscore the app's role as a guiding tool, aiding informed decisions in the dynamic automotive market.
              
    #### Technologies Used:
    - _Streamlit_
    - _Python_
    - _Machine Learning Libraries_
    
     #### Developers:
    - [Hitarth Anand Rohra](https://hitaarthh.github.io/)
    - [Ansh Grover]()
    - [Amodh Anil]() 
    - [Anirudh K]() 
    - [Nandana V V]()  
                    
    [Source Code](https://github.com/hitaarthh/Auto-Value-Pro)
             
    [Data Set Used](https://github.com/hitaarthh/Auto-Value-Pro/tree/main/dataset)      
    """)

if __name__ == "__main__":
    main()
