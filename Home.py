import streamlit as st
import time
import pandas as pd
import pickle
import os

#Importing datasets and the Machine learning models
df = pd.read_csv("dataset/Cleaned_Car_data.csv")

#Loading the pickle file of the model.
lrmodel_path = os.path.join('model', 'LinearRegressionModel.pkl')
dtmodel_path = os.path.join('model', 'DecisionTreeModel.pkl')
rfmodel_path = os.path.join('model', 'RandomForestModel.pkl')
svmmodel_path = os.path.join('model', 'SVMModel.pkl')
gbmodel_path = os.path.join('model', 'GradientBoostModel.pkl')

lrModel = pickle.load(open(lrmodel_path, 'rb'))
lr_pipeline = lrModel['pipeline']
lr_r2=lrModel['r2score']
lr_mse=lrModel['mse']
lr_mae=lrModel['mae']

dtModel = pickle.load(open(dtmodel_path, 'rb'))
dt_pipeline = dtModel['pipeline']
dt_r2=dtModel['r2score']
dt_mse=dtModel['mse']
dt_mae=dtModel['mae']

rfModel = pickle.load(open(rfmodel_path, 'rb'))
rf_pipeline = rfModel['pipeline']
rf_r2=rfModel['r2score']
rf_mse=rfModel['mse']
rf_mae=rfModel['mae']

svmModel = pickle.load(open(svmmodel_path, 'rb'))
sv_pipeline = svmModel['pipeline']
sv_r2=rfModel['r2score']
sv_mse=rfModel['mse']
sv_mae=rfModel['mae']

GradientBoostModel = pickle.load(open(gbmodel_path, 'rb'))
gb_pipeline = GradientBoostModel['pipeline']
gb_r2=GradientBoostModel['r2score']
gb_mse=GradientBoostModel['mse']
gb_mae=GradientBoostModel['mae']


def modelMetrics():
    st.write(f"#### Model Metrics:")
    if selected_algorithm == "Linear Regression":
        st.write(f"- ##### **_R2 score_** for the Linear Regression model is: {lr_r2}")
        st.write(f"- ##### **_Mean Squared Error_** for the Linear Regression model is: {lr_mse}")
        st.write(f"- ##### **_Mean Absolute Error_** for for the Linear Regression model is: {lr_mae}")
    elif selected_algorithm == "Decision Trees Regressor":
        st.write(f"- ##### **_R2 score_** for the Decision Trees Regressor is:  {dt_r2}")
        st.write(f"- ##### **_Mean Squared Error_** for the Decision Trees Regressor is:  {dt_mse}")
        st.write(f"- ##### **_Mean Absolute Error_** for the Decision Trees Regressor is:  {dt_mae}")
    elif selected_algorithm == "Random Forest Regressor":
        st.write(f"- ##### **_R2 score_** for the Random Forest Regressor is:  {rf_r2}")
        st.write(f"- ##### **Mean Squared Error** for the Random Forest Regressor is:  {rf_mse}")
        st.write(f"- ##### **Mean Absolute Error** for the Random Forest Regressor is:  {rf_mae}")
    elif selected_algorithm == "Gradient Boosting":
        st.write(f"- ##### **_R2 score_** for the Gradient Boosting is:  {gb_r2}")
        st.write(f"- ##### **_Mean Squared Error_** for the Gradient Boosting is:  {gb_mse}")
        st.write(f"- ##### **_Mean Absolute Error_** for the Gradient Boosting is:  {gb_mae}")
    elif selected_algorithm == "Support Vector Machines (SVM)":
        st.write(f"- ##### **_R2 score_** for the Support Vector Machines (SVM) is:  {sv_r2}")
        st.write(f"- ##### **_Mean Squared Error_** for the Support Vector Machines (SVM) is:  {sv_mse}")
        st.write(f"- ##### **_Mean Absolute Error_** for the Support Vector Machines (SVM) is:  {sv_mae}")
    else:
        st.write(f"Default Model Report")





#<!-The Machine Learning importing part ends here!>

st.set_page_config(page_title=f"Auto Value Pro", page_icon="🚗", layout="wide")
# Custom CSS for styling
custom_css = """
    <style>
    body {
        font-size: 18px;  /* Adjust the font size as needed */
    }

    .title-text {
        color: #FF504C; /* Change text color for title text */
        text-align: center;
    }
    </style>
"""
# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)
# Sidebar
st.sidebar.markdown("You are on the Home Page")

# Title, subtitle, and description with center alignment
st.markdown("<h1 class='title-text'>Auto Value Pro : A Vehicle Valuation Wizard</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>This app predicts the price of a car you want to sell or buy. Try filling the details below:</h5>", unsafe_allow_html=True)

# Form to accept data
 # Add your actual list of car companies
company_options = sorted(df['company'].unique().tolist())
year_options = list(range(2000, 2021))[::-1]  # Reverse the list of years from 2000 to 2020
year_options.append(1995)
fuel_options = ["Petrol", "Diesel", "LPG"]
algorithm_options = [
    "Linear Regression",
    "Random Forest Regressor",
    "Decision Trees Regressor",
    "Gradient Boosting",
    "Support Vector Machines (SVM)",
]

# User input forms
col1, col2 = st.columns(2)
with col1:
    # Selectbox for choosing the company
    selected_company = st.selectbox(f"##### Select the Company:", company_options)

# Filter the unique car names based on the selected company
carname = df[df['company'] == selected_company]['name'].unique().tolist()

# Initialize model_options with a default value
model_options = ['default value']

if carname:
    # Extract models for the selected company based on the length of the company name
    company_length = len(selected_company)
    model_options = [f"{selected_company} {car[company_length+1:]}" for car in carname if car.startswith(selected_company + ' ')]
    model_options.sort()

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
    kilometers_driven = st.number_input("##### Enter the Number of Kilometers Driven:", min_value=0.00, value=0.00)
with col8:
    selected_algorithm = st.selectbox("##### Choose the Prediction Algorithm:", algorithm_options)

col9, col10 = st.columns(2)
with col9:
    predict_button = st.button("Predict Car Price", help="Click to predict car price", key="predict_button", use_container_width=True)
with col10:
    modelReport = st.button("Model Report", help="Click to model report", key="model_report", use_container_width=True)


testingData = pd.DataFrame({
    'name':selected_model,
    'company':selected_company,
    'year': selected_year,
    'kms_driven':kilometers_driven,
    'fuel_type':selected_fuel
},index=[0])


max_thresholdDriven = 200000
base_price_for_high_mileage = 100000

def perform_actions(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven,prediction):
    value=prediction[0]
    if kilometers_driven < max_thresholdDriven:
         st.success(f"###### Predicting car price for {selected_company} {selected_model} ({selected_year}) with {kilometers_driven} kms driven, {transmission_type} transmission, and {num_previous_owners} previous owner(s) using {selected_algorithm} algorithm.")
         st.success(f"###### Predicted Price: ₹{round(value,2)}")
    else: 
        st.success(f"###### Predicting car price for {selected_company} {selected_model} ({selected_year}) with {kilometers_driven} kms driven, {transmission_type} transmission, and {num_previous_owners} previous owner(s) using {selected_algorithm} algorithm.")
        st.success(f"Attention: Your car has been driven more than {max_thresholdDriven} kilometers, indicating high mileage.")
        st.success(f"Considering this, the estimated selling price has been adjusted to a base price of ₹{base_price_for_high_mileage}.")

def modelReportFunc(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven,prediction):
    with st.spinner("Generating model report..."):
        time.sleep(3)  # Simulate a delay for calculations
    perform_actions(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven,prediction)
    st.markdown(f"<h3 style='text-align: center; color: #FF504C;'>Model Report</h3>", unsafe_allow_html=True)
    st.markdown(f"##### Here are the attributes associated with the chosen algorithm, {selected_algorithm}, revealing the model's performance indicators.")

def model_selection():
    y_predict=[]
    if selected_algorithm == "Linear Regression":
        y_predict = lr_pipeline.predict(testingData)
    elif selected_algorithm == "Random Forest Regressor":
        y_predict = rf_pipeline.predict(testingData)
    elif selected_algorithm ==  "Decision Trees Regressor":
        y_predict = dt_pipeline.predict(testingData)
    elif selected_algorithm == "Gradient Boosting":
        y_predict = gb_pipeline.predict(testingData)
    elif selected_algorithm == "Support Vector Machines (SVM)":
        y_predict = svmModel.predict(testingData)
    else:
        y_predict=["0.00"]
    # y_predic=y_predict[0]
    return y_predict

# Display results if the button is pressed
if predict_button:
    with st.spinner("Calculating the price..."):
        time.sleep(3)  # Simulate a delay for calculations
    prediction=[]
    prediction = model_selection()
    perform_actions(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven,prediction)

if modelReport:
        prediction = model_selection()
        modelReportFunc(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven,prediction)
        modelMetrics()





