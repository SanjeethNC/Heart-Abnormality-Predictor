# Heart Disease Predictor

Welcome to the Heart Disease Predictor project! This repository contains a Streamlit application designed to predict the likelihood of heart disease based on user inputs. The model uses various health metrics and lifestyle factors to make its predictions.

## Introduction

Heart disease is a major health concern worldwide. This project aims to provide an easy-to-use interface for individuals to assess their risk of heart disease based on a set of health and lifestyle parameters. The predictions are generated using a trained neural network model.

## Features

- **User-friendly Streamlit interface**
- **Input fields for various health metrics and lifestyle factors**
- **Real-time prediction of heart disease risk**
- **Visualization of the prediction result**

## Installation

To run the application locally, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/heart-disease-predictor.git
    ```

2. **Navigate to the project directory:**
    ```sh
    cd heart-disease-predictor
    ```

3. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To start the Streamlit application, run the following command:

```sh
streamlit run app.py
```

This will launch the application in your default web browser.

## Inputs

The application requires the following inputs from the user:

- **BMI:** Body Mass Index
- **Smoking:** Whether the user smokes or not
- **Alcohol Drinking:** Whether the user drinks alcohol or not
- **Stroke:** Whether the user has had a stroke
- **Physical Health:** Number of days of poor physical health in the past month
- **Mental Health:** Number of days of poor mental health in the past month
- **Diff Walking:** Difficulty walking or climbing stairs
- **Sex:** User's sex (Female/Male)
- **Age Category:** User's age category
- **Race:** User's race
- **Diabetic:** User's diabetic status
- **Physical Activity:** Whether the user engages in physical activity
- **Gen Health:** General health status
- **Sleep Time:** Average hours of sleep per day
- **Asthma:** Whether the user has asthma
- **Kidney Disease:** Whether the user has kidney disease
- **Skin Cancer:** Whether the user has skin cancer

## Model Details

The prediction model is a neural network trained on health data. It has been optimized for accuracy and is used to predict the likelihood of heart disease based on the provided inputs. The model and the normalizer are loaded from saved files (`NN_30.h5` and `Normalize.pkl`).

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request. For major changes, please discuss them with us first to ensure they fit with the project's direction.

