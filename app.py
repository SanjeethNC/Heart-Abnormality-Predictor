import streamlit as st
import pandas as pd
import pickle
from keras.models import load_model


# Sample DataFrame
data = {
    'Smoking': ['Yes', 'No'],
    'AlcoholDrinking': ['No', 'Yes'],
    'Stroke': ['No', 'Yes'],
    'DiffWalking': ['No', 'Yes'],
    'Sex': ['Female', 'Male'],
    'AgeCategory': ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54',
                  '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older'],
    'Race': ['White', 'Black', 'Asian', 'American Indian/Alaskan Native', 'Other', 'Hispanic'],
    'Diabetic': ['Yes', 'No', 'No, borderline diabetes', 'Yes (during pregnancy)'],
    'PhysicalActivity': ['Yes', 'No'],
    'GenHealth': ['Very good', 'Fair', 'Good', 'Poor', 'Excellent'],
    'Asthma': ['Yes', 'No'],
    'KidneyDisease': ['No', 'Yes'],
    'SkinCancer': ['Yes', 'No'],
    'BMI': [25.5, 30.2],
    'PhysicalHealth': [8, 5],
    'MentalHealth': [7, 4],
    'SleepTime': [7, 6],
}


predicting_data = {
    'BMI': None,
    'Smoking': None,
    'AlcoholDrinking': None,
    'Stroke': None,
    'PhysicalHealth': None,
    'MentalHealth': None,
    'DiffWalking': None,
    'Sex': None,
    'AgeCategory': None,
    'Race': None,
    'Diabetic': None,
    'PhysicalActivity': None,
    'GenHealth': None,
    'SleepTime': None,
    'Asthma': None,
    'KidneyDisease': None,
    'SkinCancer': None
}

# Categorical columns
col_ob = ['Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking',
          'Sex', 'AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth',
          'Asthma', 'KidneyDisease', 'SkinCancer']

# Numeric columns
numeric_cols = ['BMI', 'PhysicalHealth', 'MentalHealth', 'SleepTime']

# Streamlit app
st.title("Your Death Date")

import streamlit as st
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    image_path = "heart.gif"
    st.image(image_path, width=300)
with col3:
    st.write(' ')



# Input for categorical columns
for col in col_ob:
    selected_value = st.selectbox(f"Select {col}", set(data[col]))
    model=pickle.load(open(f'{col}.pkl','rb'))
    print('wdeer')
    predicting_data[col]=model.transform([selected_value])

# Input for numeric columns
for col in numeric_cols:
    input_value = st.number_input(f"Enter {col}", min_value=0.0, step=0.1)
    predicting_data[col]=input_value
    
normalizer_model=pickle.load(open('Normalize.pkl','rb'))
    
Final_model = load_model('NN_30.h5')

col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    button=st.button('Predict')
    if button:
        pred=Final_model.predict(normalizer_model.transform(pd.DataFrame(predicting_data)))
if button:
    st.write(f'So there are {pred[0][0][0]*100:.2f} % of chance of you having Heart Disease ')
    

