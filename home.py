import streamlit as st
st.set_page_config(page_title="Auto Value Pro", page_icon="🚗", layout="wide")

# Custom CSS for styling
custom_css = """
    <style>
    body {
            font-size: 18px;  /* Adjust the font size as needed */
        }

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

        .title-text {
            color: #FF504C; /* Change text color for title text */
            text-align: center;
        }
    </style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)
st.sidebar.markdown("You are on the Home Page")
# page = st.sidebar.radio("Go to")
# # Sidebar
# st.sidebar.markdown("# Navigation")
# page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Title, subtitle, and description with center alignment
st.markdown("<h2 class='title-text'>Auto Value Pro : A Vehicle Valuation Wizard</h2>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>This app predicts the price of a car you want to sell or buy. Try filling the details below:</div>", unsafe_allow_html=True)

# Form to accept data
company_options = ["Company A", "Company B", "Company C"]  # Add your actual list of car companies
model_options = ["Model X", "Model Y", "Model Z"]  # Add your actual list of car models
year_options = list(range(2000, 2021))[::-1]  # Reverse the list of years from 2000 to 2020
year_options.append(1995)
fuel_options = ["Petrol", "Diesel", "LPG"]
algorithm_options = [
    "Linear Regression",
    "Random Forest Regressor",
    "Decision Trees Regressor",
    "Gradient Boosting",
    "Support Vector Machines (SVM)",
    "K-Nearest Neighbors (KNN)"
]

# User input forms
col1, col2 = st.columns(2)
with col1:
    selected_company = st.selectbox("Select the Company:", company_options)
with col2:
    selected_model = st.selectbox("Select the Model:", model_options)

col3, col4 = st.columns(2)
with col3:
    selected_year = st.selectbox("Select the Year of Purchase:", year_options)
with col4:
    selected_fuel = st.selectbox("Select the Fuel Type:", fuel_options)

col5, col6 = st.columns(2)
with col5:
    transmission_type = st.radio("Transmission Type:", ["Manual", "Automatic"])
with col6:
    num_previous_owners = st.slider("Number of Previous Owners:", min_value=0, max_value=5, value=1, step=1)

col7, col8 = st.columns(2)
with col7:
    kilometers_driven = st.number_input("Enter the Number of Kilometers Driven:")
with col8:
    selected_algorithm = st.selectbox("Choose the Prediction Algorithm:", algorithm_options)


col9, col10 = st.columns(2)
with col9:
    predict_button = st.button("Predict Car Price", help="Click to predict car price", key="predict_button")
with col10:
    modelReport = st.button("Model Report", help="Click to model report", key="model_report")


# Display results if the button is pressed
if predict_button:
    st.success(f"Predicting car price for {selected_company} {selected_model} ({selected_year}) with {kilometers_driven} km driven, {transmission_type} transmission, and {num_previous_owners} previous owner(s) using {selected_algorithm} algorithm.")
    # Add your machine learning prediction logic here and display the result
    # For example: predicted_price = predict_price(selected_company, selected_model, selected_year, selected_fuel, kilometers_driven, selected_algorithm, transmission_type, num_previous_owners)
    # st.write(f"Predicted Price: ${predicted_price}")
if modelReport:
    st.success(f"Predicting car price for {selected_company} {selected_model} ({selected_year}) with {kilometers_driven} km driven, {transmission_type} transmission, and {num_previous_owners} previous owner(s) using {selected_algorithm} algorithm.")
    st.markdown(f"Model Report:")
# if page == "Home":
#     home.show()
# elif page == "About":
#     about.show()
# elif page == "Contact":
#     contact.show()