import streamlit as st

def main():
    st.title("About")
    st.write("""
    Auto Value Pro is a web application designed to predict the price of a car based on various factors.
    
    ### How it Works:
    - Select the car company, model, year of purchase, fuel type, and other relevant details.
    - Click on the "Predict Car Price" button.
    - The app uses machine learning algorithms to predict the price of the selected car.
    
    ### Features:
    - Predict car prices using different algorithms like Linear Regression, Random Forest, etc.
    - User-friendly interface for easy input.
    - Explore predictions for various car configurations.
    
    ### Developers:
    - This app is developed by [Your Name].
    - Contact us for any inquiries or feedback.
    
    ### Technologies Used:
    - Streamlit
    - Python
    - Machine Learning Libraries (e.g., scikit-learn)
    
    **Disclaimer**: The predictions provided by this app are for reference purposes only. Actual market conditions may vary.
    """)

    st.markdown("### Contact Us:")
    st.write("For any inquiries or feedback, please contact us at [your.email@example.com].")

    st.markdown("### Acknowledgments:")
    st.write("We would like to thank the Streamlit community and the developers of the underlying libraries that made this app possible.")

if __name__ == "__main__":
    main()