# Auto Value Pro: A Vehicle Valuation Wizard

Auto Value Pro is a Streamlit web application that predicts the price of a car you want to sell or buy. It provides a user-friendly interface to input details about the car and uses machine learning algorithms for price prediction.

## Features

- Predict car prices based on various input parameters.
- Simple and intuitive user interface.
- Modular code structure for better organization.
- Integration with Streamlit for web-based deployment.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/auto-value-pro.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run main_app.py
    ```

4. Open the provided URL in your browser to use the application [Auto Value Pro](https://autovaluepro.streamlit.app/).

## Project Structure

- **Home.py**
- **__pycache__/**
  - about.cpython-311.pyc
  - about_page.cpython-311.pyc
  - decomp.cpython-311.pyc
- **client_secrets.json**
- **dataset/**
  - Cleaned_Car_data.csv
  - quikr_car.csv
- **kernelVersion/**
  - DecisionTreeModel.ipynb
  - GradientBoostModel.ipynb
  - LinearRegressionModel.ipynb
  - RandomForestModel.ipynb
  - SVM.ipynb
- **model/**
  - DecisionTreeModel.pkl
  - GradientBoostModel.pkl
  - LinearRegressionModel.pkl
  - RandomForestModel.pkl
  - SVMModel.pkl
- **pages/**
  - **About Us.py**
  - **Contact Us.py**
  - **__pycache__/**
    - about.cpython-311.pyc
- **readme.md**
- **requirements.txt**




## Contributing

If you would like to contribute to this project, please follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
