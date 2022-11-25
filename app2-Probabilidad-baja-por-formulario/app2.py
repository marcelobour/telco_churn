#Importación librerías
import streamlit as st
import pandas as pd
import requests
import xgboost as xgb
import numpy as np

#Ruta del dataset
url_data='https://raw.githubusercontent.com/marcelobour/telco_churn/main/Telco_customer_churn.csv'

#Ruta del modelo entrenado
url_model='https://raw.githubusercontent.com/marcelobour/app2/main/aucpr-precision-8var.txt'

#Generamos dataframe de ciudades y coordenadas
coor_cols = ['City', 'Longitude', 'Latitude']
telco = pd.read_csv(url_data, sep=';', usecols=coor_cols)
to_num_cols = ['Longitude', 'Latitude']
telco[to_num_cols] = telco[to_num_cols].apply(lambda x: x.str.replace(',', '.')).apply(lambda x: x.str.replace(' ', '0')).apply(lambda x: pd.to_numeric(x))
cities_coor = telco.groupby(['City']).mean()
cities = np.sort(telco['City'].unique())

#Colocamos título
st.title("Probabilidad de baja")

#Definimos alineación centrada para el título ya que Stramlit no tiene opción
title_alignment="""
<style>
#probabilidad-de-baja {
  text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

#Creamos los elementos para cargar el formulario de 8 variables en la barra lateral
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