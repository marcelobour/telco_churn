# Libraries import
import streamlit as st
import pandas as pd
import requests
import xgboost as xgb
import numpy as np
import plotly.graph_objects as go

# Dataset path
url_data='https://raw.githubusercontent.com/marcelobour/telco_churn/main/data/Telco_customer_churn.csv'

# Trained model path
url_model='https://raw.githubusercontent.com/marcelobour/telco_churn/main/app2-Probabilidad-baja-por-formulario/aucpr-precision-8var.txt'

# Remove default excessive top margin
hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 2rem;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Set title
st.title("Leaving Probability")

# Define centered alignment for the title since Streamlit doesn't have the option.
title_alignment="""
<style>
#Leaving-Probability {
  text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

# Create cities and coordinates dataframe
coor_cols = ['City', 'Longitude', 'Latitude']
telco = pd.read_csv(url_data, sep=';', usecols=coor_cols)
to_num_cols = ['Longitude', 'Latitude']
telco[to_num_cols] = telco[to_num_cols].apply(lambda x: x.str.replace(',', '.')).apply(lambda x: x.str.replace(' ', '0')).apply(lambda x: pd.to_numeric(x))
cities_coor = telco.groupby(['City']).mean()
cities = np.sort(telco['City'].unique())

# Creamos variables for 8 variables input
with st.sidebar:
  '# Datos de cliente'
  charges = st.slider('Monthly Charges', 10, 120)
  tenure = st.slider('Tenure Months', 0, 80)
  contract = st.radio('Contract', ('Month to month', 'One year', 'Two year'))
  internet = st.radio('Internet Service', ('Fiber optic', 'DSL', 'No'))
  depen = st.checkbox('Dependents')
  paper = st.checkbox('Paperless Billing')
  city = st.selectbox('City', options=cities)  
  submit = st.button('Enviar')

# Define ranges
range_1 = [0, 0.6] 
range_2 = [0.6, 0.7]
range_3 = [0.7, 1]

# Ranges colores
ver_sua = '#bae3cd'
ver_int = '#59b378'
ama_sua = '#f7edae'
ama_int = '#ebc51c'
roj_sua = '#f0a8a8'
roj_int = '#d14b4b'

# Assign colors for initial empty plot
bar_color = None
pred = None
zone = None
instruc = None

# If form is submited preapre data and get prediction
if submit:
  # Assign lat and long values for selected city
  lat = cities_coor.loc[city][0]
  lon = cities_coor.loc[city][1]

  # Create dictionary and coonvert to dataframe to input trained model
  form_dict={
    'Tenure Months': tenure,
    'Monthly Charges': charges,
    'Dependents_No': 1 if depen==False else 0,
    'Latitude': lat,
    'Longitude': lon,
    'Paperless Billing_No': 1 if paper==False else 0,
    'Contract_Month-to-month': 1 if contract=='Month to month' else 0,
    'Internet Service_Fiber optic': 1 if internet=='Fiber optic' else 0}
  form = pd.DataFrame(form_dict, index=[0])

  # Get trained model from github
  req = requests.get(url_model)
  with open("modelo.txt", "wb") as file:
    file.write(req.content)

  # Instantiate and load trained model
  model_replica = xgb.XGBClassifier()
  model_replica.load_model("modelo.txt")

  # Generate prediction, append to data and display
  pred = model_replica.predict_proba(form)[:,1][0]

  # Set bar color according to range
  if range_1[0] <= pred < range_1[1]:
    bar_color = ver_int
    zone = 'baja'
  elif range_2[0] <= pred < range_2[1]:
    bar_color = ama_int
    zone = 'media'
  else:
    bar_color = roj_int
    zone = 'alta'

# Create colored status indicator
fig = go.Figure(go.Indicator(
domain = {'x': [0, 1], 'y': [0, 1]},
value = pred,
number = {'valueformat': '.0%'},
mode = "gauge+number",
title = {'text': ""},
gauge = {'axis': {'range': [None, 1], 'nticks': 20, 'ticklen': 0, 'tickformat': '.0%'},
           'borderwidth': 0,
           'bar': {'color': bar_color},
           'steps' : [{'range': range_1, 'color': ver_sua}, {'range': range_2, 'color': ama_sua}, {'range': range_3, 'color': roj_sua}]
          }))
st.plotly_chart(fig)  

# Choose user instructions
if zone=='alta':
  instruc = 'Offer transfer to Tech Support and a service bonus for 1 month.'
elif zone=='media':
  instruc = 'Offer a one-time transfer to Tech Support.'
elif zone=='baja':
  instruc = 'Proceed with standard procedure'
else:
  instruc = 'Enter customer information and press "Send" to find out the probability of churn'

# Display intruction
if instruc is not None:
  st.subheader(instruc, anchor='instruccion')

  # Center instruction
  inst_alin="""
  <style>
  #instruccion {
    text-align: center
  }
  </style>
  """
  st.markdown(inst_alin, unsafe_allow_html=True)
