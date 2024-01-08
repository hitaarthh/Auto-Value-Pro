import streamlit as st
import time
import pandas as pd
import pickle
import os
# from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pyplot as plt

#Importing datasets and the Machine learning models
df = pd.read_csv("dataset/Cleaned_Car_data.csv")

#Importing the pickle file of the model.
lrmodel_path = os.path.join('model', 'LinearRegressionModel.pkl')
dtmodel_path = os.path.join('model', 'DecisionTreeModel.pkl')
rfmodel_path = os.path.join('model', 'RandomForestModel.pkl')
svmmodel_path = os.path.join('model', 'SVMModel.pkl')
gbmodel_path = os.path.join('model', 'GradientBoostModel.pkl')

#Loading the dependencies from the Linear Regression model to the app.
lrModel = pickle.load(open(lrmodel_path, 'rb'))
lr_pipeline = lrModel['pipeline']
lr_r2=lrModel['r2score']
lr_mse=lrModel['mse']
lr_mae=lrModel['mae']
lr_train_sizes = lrModel['train_sizes']
lr_train_scores=lrModel['train_scores']
lr_test_scores=lrModel['test_scores']

#Loading the dependencies from the Decision Tree Regressor model to the app.
dtModel = pickle.load(open(dtmodel_path, 'rb'))
dt_pipeline = dtModel['pipeline']
dt_r2=dtModel['r2score']
dt_mse=dtModel['mse']
dt_mae=dtModel['mae']
dt_train_sizes =dtModel['train_sizes']
dt_train_scores=dtModel['train_scores']
dt_test_scores=dtModel['test_scores']

#Loading the dependencies from the Random Forest Regressor model to the app.
rfModel = pickle.load(open(rfmodel_path, 'rb'))
rf_pipeline = rfModel['pipeline']
rf_r2=rfModel['r2score']
rf_mse=rfModel['mse']
rf_mae=rfModel['mae']
rf_train_sizes =rfModel['train_sizes']
rf_train_scores=rfModel['train_scores']
rf_test_scores=rfModel['test_scores']

#Loading the dependencies from the Support Vector Machines (SVM) model to the app.
svmModel = pickle.load(open(svmmodel_path, 'rb'))
sv_pipeline = svmModel['pipeline']
sv_r2=svmModel['r2score']
sv_mse=svmModel['mse']
sv_mae=svmModel['mae']
sv_train_sizes =svmModel['train_sizes']
sv_train_scores=svmModel['train_scores']
sv_test_scores=svmModel['test_scores']

#Loading the dependencies from the Gradient Boosting model to the app.
GradientBoostModel = pickle.load(open(gbmodel_path, 'rb'))
gb_pipeline = GradientBoostModel['pipeline']
gb_r2=GradientBoostModel['r2score']
gb_mse=GradientBoostModel['mse']
gb_mae=GradientBoostModel['mae']
gb_train_sizes =GradientBoostModel['train_sizes']
gb_train_scores=GradientBoostModel['train_scores']
gb_test_scores=GradientBoostModel['test_scores']

#Function to display the model report.
#gets imported onClick "Stats for nerd" button.
def modelMetrics():
    st.write(f"#### Model Metrics:")
    if selected_algorithm == "Linear Regression":
        metrics_data = {
            'count':[1,2,3],
            'Metrics': ['R2 Score', 'Mean Squared Error', 'Mean Absolute Error'],
            'Linear Regression': [lr_r2, lr_mse, lr_mae],}
        metrics_df = pd.DataFrame(metrics_data)
        metrics_df.set_index('count', inplace=True)
        st.table(metrics_df)
        learningCurve(lr_train_sizes,lr_train_scores,lr_test_scores)
    elif selected_algorithm == "Decision Trees Regressor":
        metrics_data = {
            'count':[1,2,3],
            'Metrics': ['R2 Score', 'Mean Squared Error', 'Mean Absolute Error'],
            'Decision Trees Regressor': [dt_r2, dt_mse, dt_mae],}
        metrics_df = pd.DataFrame(metrics_data)
        metrics_df.set_index('count', inplace=True)
        st.table(metrics_df)
        learningCurve(dt_train_sizes,dt_train_scores,dt_test_scores)
    elif selected_algorithm == "Random Forest Regressor":
        metrics_data = {
            'count':[1,2,3],
            'Metrics': ['R2 Score', 'Mean Squared Error', 'Mean Absolute Error'],
            'Random Forest Regressor': [rf_r2, rf_mse, rf_mae],}
        metrics_df = pd.DataFrame(metrics_data)
        metrics_df.set_index('count', inplace=True)
        st.table(metrics_df)
        learningCurve(rf_train_sizes,rf_train_scores,rf_test_scores)
    elif selected_algorithm == "Gradient Boosting":
        metrics_data = {
            'count':[1,2,3],
            'Metrics': ['R2 Score', 'Mean Squared Error', 'Mean Absolute Error'],
            'Gradient Boosting': [gb_r2, gb_mse, gb_mae],}
        metrics_df = pd.DataFrame(metrics_data)
        metrics_df.set_index('count', inplace=True)
        st.table(metrics_df)
        learningCurve(gb_train_sizes,gb_train_scores,gb_test_scores)
    elif selected_algorithm == "Support Vector Machines (SVM)":
        metrics_data = {
            'count':[1,2,3],
            'Metrics': ['R2 Score', 'Mean Squared Error', 'Mean Absolute Error'],
            'Support Vector Machines (SVM)': [sv_r2, sv_mse, sv_mae],}
        metrics_df = pd.DataFrame(metrics_data)
        metrics_df.set_index('count', inplace=True)
        st.table(metrics_df)
        learningCurve(sv_train_sizes,sv_train_scores,sv_test_scores)
    else:
        st.write(f"Default Model Report")

#Function to display the learning curve of the model
#gets imported within the modelMetrics()
def learningCurve(train_sizes, train_scores, test_scores, figsize=(8, 4)):
    st.write(f"#### Learning Curve:")
    train_scores_mean = -np.mean(train_scores, axis=1)
    test_scores_mean = -np.mean(test_scores, axis=1)
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(train_sizes, train_scores_mean, label='Training Score')
    ax.plot(train_sizes, test_scores_mean, label='Validation Score')
    ax.set_xlabel('Training Set Size')
    ax.set_ylabel('Negative Mean Squared Error')
    ax.legend()
    plt.subplots_adjust(left=3.1, right=5.9)
    plt.tight_layout()
    st.pyplot(fig)

#<!-price prediction and report display ends here!>
    
# Frontend of the Streamlit app starts here...
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
    .subtitle-text {
        color: #FF504C; /* Change text color for title text */
        text-align: center;
    }
    </style>
"""

# Applying custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.markdown("You are on the Home Page")

# Title, subtitle, and description with center alignment
st.markdown("<h1 class='title-text'>Auto Value Pro : A Vehicle Valuation Wizard</h1>", unsafe_allow_html=True)
st.markdown("<h5 class='subtitle-text'><i>\"Empowering Decisions, One Car at a Time\"</i></h5>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>This app predicts the price of a car you want to sell or buy. Try filling the details below:</h5>", unsafe_allow_html=True)

#<!-Form to accept data-!>
company_options = sorted(df['company'].unique().tolist()) #loading the unique values of the car company names
year_options = list(range(2000, 2021))[::-1] #generating the various year options as per supervised dataset.
year_options.append(1995)
fuel_options = ["Petrol", "Diesel", "LPG"]
algorithm_options = [
    "Linear Regression",
    "Decision Trees Regressor",
    "Random Forest Regressor",
    "Gradient Boosting",
    "Support Vector Machines (SVM)",
]#Defining different types of models on which predictions can be made.

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
    num_previous_owners = st.slider("##### Number of Previous Owners:", min_value=1, max_value=5, value=1, step=1)

col7, col8 = st.columns(2)
with col7:
    kilometers_driven = st.number_input("##### Enter the Number of Kilometers Driven:", min_value=0.00, value=0.00)
with col8:
    selected_algorithm = st.selectbox("##### Choose the Prediction Algorithm:", algorithm_options)

col9, col10 = st.columns(2)
with col9:
    predict_button = st.button("Predict Car Price", help="Click to predict car price", key="predict_button", use_container_width=True)
with col10:
    modelReport = st.button("Stats for nerds", help="Click to get model report", key="model_report", use_container_width=True)

#Creating the testing data for model prediciton
testingData = pd.DataFrame({
    'name':selected_model,
    'company':selected_company,
    'year': selected_year,
    'kms_driven':kilometers_driven,
    'fuel_type':selected_fuel,
    'No. of Previous Owners':num_previous_owners,
    'Transmission Type':transmission_type,
},index=[0])

#Maximum threshold value incaase the output because negative.
max_thresholdDriven = 200000
base_price_for_high_mileage = 100000

def perform_actions(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven,prediction):
    value=prediction[0]
    if kilometers_driven < max_thresholdDriven or value<=0:
         st.success(f"###### Predicting car price for {selected_company} {selected_model} ({selected_year}) with {kilometers_driven} kms driven, {transmission_type} transmission, and {num_previous_owners} previous owner(s) using {selected_algorithm} algorithm.")
         st.success(f"###### Predicted Price: ₹{round(value,2)}")
    else: 
        st.success(f"###### Predicting car price for {selected_company} {selected_model} ({selected_year}) with {kilometers_driven} kms driven, {transmission_type} transmission, and {num_previous_owners} previous owner(s) using {selected_algorithm} algorithm.")
        st.success(f"Attention: Your car has been driven more than {max_thresholdDriven} kilometers, indicating high mileage.")
        st.success(f"Considering this, the estimated selling price has been adjusted to a base price of ₹{base_price_for_high_mileage}.")

def modelReportFunc(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven,prediction):
    with st.spinner("Generating model report..."):
        time.sleep(3)  
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
        y_predict = sv_pipeline.predict(testingData)
    else:
        y_predict=["0.00"]
    # y_predic=y_predict[0]
    return y_predict

#onclick "Predict Car Price" button
if predict_button:
    with st.spinner("Calculating the price..."):
        time.sleep(3)  # Simulate a delay for calculations
    prediction=[]
    prediction = model_selection()
    perform_actions(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven,prediction)

#onClick "Stats for nerds"
if modelReport:
        prediction = model_selection()
        modelReportFunc(selected_company, selected_model, selected_year, kilometers_driven, transmission_type, num_previous_owners, selected_algorithm, max_thresholdDriven,prediction)
        modelMetrics()