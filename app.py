import streamlit as st

import pickle
import numpy as np
import pandas as pd

#Load pre-trained K_Means



with open('K_means.pkl', 'rb') as f: 
    kmeans = pickle.load(f) #pickle.load(f) loads the object from the file object f.



cluster_names = {
    0: 'Older Moderate Spenders',
    1: 'Young High Spenders',
    2: 'Middle-aged Low Spenders',
    3: 'Middle-aged High Income Low Spenders',
    4: 'Young Moderate Income High Spenders'
}

#Streamlit App

st.title("Mall Customer Segmentation")
st.write("Predict customer segments based on user input")

#User Input
annual_income = st.slider('Annual Income in $',15,330,1)
spending_score = st.slider('spending score',1,100,50)

# annual_income = st.number_input('Annual Income in $k', min_value=0, value=50, step=1)
# spending_score = st.number_input('Spending Score (1-100)', min_value=0, max_value=100, value=50, step=1)


#Predict cluster

if st.button("Predict Cluster"):
        user_data= pd.DataFrame([[annual_income,spending_score]], columns=['Annual Income (k$)', 'Spending Score (1-100)'])
        predict_cluster = kmeans.predict(user_data)[0]
         
         
           
#Display Prediction

        st.subheader(f"The Customer belongs to {predict_cluster}")
        st.write(cluster_names.get(predict_cluster,"cluster description not available"))


