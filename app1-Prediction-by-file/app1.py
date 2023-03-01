# Importing libraries
import streamlit as st
import pandas as pd
import requests
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder

# Dataset url
url='https://raw.githubusercontent.com/marcelobour/telco_churn/main/data/Telco_customer_churn.csv'

# Remove default excessive top margin
hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 2rem;}
</style>
"""
st.title("Churn predictor")
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#st.markdown("***") # This adds a line on top

'##### 1) Select predictive model oriented towards:'
opa = 'a) Precision: to achieve around 68% precision and capture 59% of potential lefts.'
opb = 'b) Recall: to capture around 83% of potential lefts with 52% precision.' 
modelo = st.radio(label = 'model type', options = [opa, opb], label_visibility='collapsed')

''
'##### 2) Choose the file on which you want to predict churn:'

# Create dataframe to put data
telco_sample = pd.DataFrame()

# Option por automatic data
if st.checkbox('Auto generate random test dataset'):
    
  # Define a function to get the sampled data once and remove columns related to price and churn forecasting
  @st.cache
  def get_sample():
    sample = pd.read_csv(url, sep=';').sample(n=20).drop(['Churn Value', 'Churn Label', 'Churn Score', 'Churn Reason', 'CLTV'], axis=1)
    return sample
  telco_sample = get_sample()

# If not automatic then allow to upload file
else:
  # File upload an read
  datos = st.file_uploader('Select file')
  if datos is not None:
    telco_sample = pd.read_csv(datos, sep = ',')

# Show sampled o uploaded data
if not telco_sample.empty:
  'Loaded data'
  telco_sorted = telco_sample.sort_index().reset_index(drop=True)
  st.dataframe(telco_sorted)

  # Get loaded data columns and compare them against what is expected
  expected_cols = pd.read_csv(url, sep=';').drop(['Churn Value', 'Churn Label', 'Churn Score', 'Churn Reason', 'CLTV'], axis=1).columns
  if len(expected_cols) != len(telco_sample.columns):
    st.error('Loaded file has a different number of columns than expected by the model.', icon="🚨")
  else:
    if (expected_cols != telco_sample.columns).any():
      st.error('Loaded file does not have the fields expected by the model.', icon="🚨")
    else:
      # We finished preparing the data by removing more columns, converting others to numbers, and converting categorical variables to binaries
      # We assign to a new dataframe the original dataset without the columns that we discarded in the variable analysis
      X_pre = telco_sample.drop(['CustomerID', 'Count', 'Country', 'State', 'Lat Long', 'Total Charges', 'City', 'Zip Code'], axis=1)

      # Convert columns into numbers and categorical variables into new binary variables
      cols = ['Longitude', 'Latitude', 'Monthly Charges']
      X_pre[cols] = X_pre[cols].apply(lambda x: x.str.replace(',', '.')).apply(lambda x: x.str.replace(' ', '0')).apply(lambda x: pd.to_numeric(x))
      X = pd.get_dummies(X_pre)

      # Get trained model from github
      if modelo == opa:
        #url = 'https://raw.githubusercontent.com/neoncoip/telco_churn/main/models/aucpr-average_precision.txt'
        url = '../models/aucpr-average_precision.txt'
      else: 
        #url = 'https://raw.githubusercontent.com/neoncoip/telco_churn/main/models/aucpr-recall.txt'
        url = '../models/aucpr-recall.txt'
      req = requests.get(url)
      with open("modelo.txt", "wb") as file:
        file.write(req.content)

      # Instantiate and load the trained model
      model_replica = xgb.XGBClassifier()
      model_replica.load_model("modelo.txt")

      # Indicate labels
      model_replica._le = LabelEncoder().fit([0, 1])

      # Generates predictions on data, appends them to the data spreadsheet, and displays
      Y = model_replica.predict(X)
      telco_sorted.insert(loc = 0, column = 'Churn prediction', value = Y)
      'Data + Prediction'
      telco_sorted
      
      # Save the file as CSV and allow downloading
      telco_csv = telco_sorted.to_csv().encode('utf-8')
      st.download_button(label="Download prediction", data=telco_csv, file_name="Churn_predictions.csv", mime="text/csv")
