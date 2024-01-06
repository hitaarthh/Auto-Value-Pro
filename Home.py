import streamlit as st
st.set_page_config(page_title=f"Auto Value Pro", page_icon="🚗", layout="wide")
import time
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
st.markdown("<h1 class='title-text'>Auto Value Pro : A Vehicle Valuation Wizard</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>This app predicts the price of a car you want to sell or buy. Try filling the details below:</h5>", unsafe_allow_html=True)
st.markdown(f"")
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
    selected_company = st.selectbox(f"##### Select the Company:", company_options)
with col2:
    selected_model = st.selectbox("##### Select the Model:", model_options)

col3, col4 = st.columns(2)
with col3:
    selected_year = st.selectbox("##### Select the Year of Purchase:", year_options)
with col4:
    selected_fuel = st.selectbox("##### Select the Fuel Type:", fuel_options)

col5, col6 = st.columns(2)
with col5:
    transmission_type = st.radio("##### Transmission Type:", ["Manual", "Automatic"])
with col6:
    num_previous_owners = st.slider("##### Number of Previous Owners:", min_value=0, max_value=5, value=1, step=1)

col7, col8 = st.columns(2)
with col7:
    kilometers_driven = st.number_input("##### Enter the Number of Kilometers Driven:",min_value=0.00,value=0.00)
with col8:
    selected_algorithm = st.selectbox("##### Choose the Prediction Algorithm:", algorithm_options)

col9, col10 = st.columns(2)
with col9:
    predict_button = st.button("Predict Car Price", help="Click to predict car price", key="predict_button", use_container_width=True)
with col10:
    modelReport = st.button("Model Report", help="Click to model report", key="model_report",use_container_width=True)

max_thresholdDriven = 200000
base_price_for_high_mileage = 100000

def perform_actions(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven):
    if kilometers_driven < max_thresholdDriven:
         st.success(f"###### Predicting car price for {selected_company} {selected_model} ({selected_year}) with {kilometers_driven} kms driven, {transmission_type} transmission, and {num_previous_owners} previous owner(s) using {selected_algorithm} algorithm.")
    else: 
        st.success(f"Attention: Your car has been driven more than {max_thresholdDriven} kilometers, indicating high mileage.")
        st.success(f"Considering this, the estimated selling price has been adjusted to a base price of ${base_price_for_high_mileage}.")
        # st.success(f"Original Predicted Price: ${predicted_price}")
        # st.success(f"Adjusted Selling Price: ${adjusted_price}")
    # Add your machine learning prediction logic here and display the result
    # For example: predicted_price = predict_price(selected_company, selected_model, selected_year, selected_fuel, kilometers_driven, selected_algorithm, transmission_type, num_previous_owners)
    # st.write(f"Predicted Price: ${predicted_price}")

def modelReportFunc(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven):
    with st.spinner("Generating model report..."):
        time.sleep(3)  # Simulate a delay for calculations
    perform_actions(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven)
    st.markdown(f"##### Model Report:")
    st.markdown(f"- Here are the attributes associated with the chosen algorithm, {selected_algorithm}, revealing the model's performance indicators.")

# Display results if the button is pressed
if predict_button:
    with st.spinner("Calculating the price..."):
        time.sleep(3)  # Simulate a delay for calculations
    perform_actions(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven)
if modelReport:
    modelReportFunc(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven)
    
# if page == "Home":
#     home.show()
# elif page == "About":
#     about.show()
# elif page == "Contact":
#     contact.show()