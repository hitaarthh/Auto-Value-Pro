import streamlit as st

st.set_page_config(
    page_title="Auto Value Pro",
    page_icon="",
    layout="centered",
    initial_sidebar_state="auto"
)
# Custom CSS for styling
custom_css = """
    <style>
        .navbar {
            background-color: #FF504D;
            padding: 10px;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .navbar a {
            color: white;
            text-decoration: none;
            padding: 10px;
            margin: 0 10px;  /* Adjusted margin for better spacing */
            font-weight: bold;
        }
    </style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Navigation bar
st.markdown(
    """
    <div class="navbar">
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Title, subtitle, and description with center alignment
st.markdown("<h2 style='text-align: center;'>Auto Value Pro : A Vehicle Valuation Wizard</h2>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>This app predicts the price of a car you want to sell or buy. Try filling the details below:</div>", unsafe_allow_html=True)

# Form to accept data
company_options = ["Company A", "Company B", "Company C"]  # Add your actual list of car companies
model_options = ["Model X", "Model Y", "Model Z"]  # Add your actual list of car models
year_options = list(range(2000, 2021))[::-1]  # Reverse the list of years from 2000 to 2020
year_options.append(1995)
fuel_options = ["Petrol", "Diesel", "LPG"]
algorithm_options = [
    "Linear Regression",
    "Random Forest",
    "Decision Trees",
    "Gradient Boosting",
    "Support Vector Machines (SVM)",
    "K-Nearest Neighbors (KNN)"
]

# User input forms
selected_company = st.selectbox("Select the Company:", company_options)
selected_model = st.selectbox("Select the Model:", model_options)
selected_year = st.selectbox("Select the Year of Purchase:", year_options)
selected_fuel = st.selectbox("Select the Fuel Type:", fuel_options)

# Create columns for "Transmission Type" and "Number of Previous Owners"
col1, col2 = st.columns(2)

with col1:
    transmission_type = st.radio("Transmission Type", ["Manual", "Automatic"])

with col2:
    num_previous_owners = st.slider("Number of Previous Owners", min_value=0, max_value=5, value=1, step=1)

kilometers_driven = st.number_input("Enter the Number of Kilometers Driven:")
selected_algorithm = st.selectbox("Choose the Prediction Algorithm:", algorithm_options)

# Button to trigger prediction with center alignment
predict_button = st.button("Predict Car Price", help="Click to predict car price", key="predict_button")

# Display results if the button is pressed
if predict_button:
    st.success(f"Predicting car price for {selected_company} {selected_model} ({selected_year}) with {kilometers_driven} km driven, {transmission_type} transmission, and {num_previous_owners} previous owner(s) using {selected_algorithm} algorithm.")
    # Add your machine learning prediction logic here and display the result
    # For example: predicted_price = predict_price(selected_company, selected_model, selected_year, selected_fuel, kilometers_driven, selected_algorithm, transmission_type, num_previous_owners)
    # st.write(f"Predicted Price: ${predicted_price}")
