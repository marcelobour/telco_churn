#Importación de librerías
import streamlit as st
import pandas as pd
import requests
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder

#Ruta del dataset
url='https://raw.githubusercontent.com/marcelobour/telco_churn/main/Telco_customer_churn.csv'

#Quitamos margen de arriba excesivo por defecto
hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 2rem;}
</style>
"""
st.title("Predictor de Churn")
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#st.markdown("***") #Esto agrega una línea pero mucho margen arriba

'##### 1) Seleccione el modelo predictivo orientado a:'
opa = 'a) Precisión: para lograr en torno a un 68% de precisión y capturar 59% de potenciales bajas'
opb = 'b) Maximizar la captura: para lograr capturar entorno a un 83% de potenciales bajas con una precisión del 52%' 
modelo = st.radio(label = 'tipo modelo', options = [opa, opb], label_visibility='collapsed')

''
'##### 2) Elija el archivo sobre el que desea pronosticar churn:'

#Creamos dataframe donde pondremos los datos
telco_sample = pd.DataFrame()

#Generamos opción para datos automáticos
if st.checkbox('Generar set de datos aleatorios de prueba automáticamente'):
    
  #Definimos función para obtener por única vez datos sampleados y quitamos columnas relacionadas con pronósticos precios y churn
  @st.cache
  def get_sample():
    sample = pd.read_csv(url, sep=';').sample(n=20).drop(['Churn Value', 'Churn Label', 'Churn Score', 'Churn Reason', 'CLTV'], axis=1)
    return sample
  telco_sample = get_sample()

#Si no se tilda casilla podemos subir un archivo
else:
  #Subimos y leemos el archivo
  datos = st.file_uploader('Seleccione un archivo')
  if datos is not None:
    telco_sample = pd.read_csv(datos, sep = ',')

#Mostramos los datos cargados
if not telco_sample.empty:
  'Datos cargados'
  telco_sorted = telco_sample.sort_index().reset_index(drop=True)
  st.dataframe(telco_sorted)

  #Obtenemos columnas de los datos cargados y comparamos contra lo esperado
  expected_cols = pd.read_csv(url, sep=';').drop(['Churn Value', 'Churn Label', 'Churn Score', 'Churn Reason', 'CLTV'], axis=1).columns
  if len(expected_cols) != len(telco_sample.columns):
    st.error('El archivo cargado posee una cantidad de columnas diferente a las esperadas por el modelo.', icon="🚨")
  else:
    if (expected_cols != telco_sample.columns).any():
      st.error('El archivo cargado no posee los campos esperados por el modelo.', icon="🚨")
    else:
      #Terminamos de preparar los datos elinando más columnas, convirtiendo a números otras y convirtiendo variables categóricas en binarias
      #Asignamos a un nuevo dataframe el dataset original sin las columnas que descartamos en análisis de variables
      X_pre = telco_sample.drop(['CustomerID', 'Count', 'Country', 'State', 'Lat Long', 'Total Charges', 'City', 'Zip Code'], axis=1)

      #Convertimos columnas a número y variables categóricas a nuevas variables binarias
      cols = ['Longitude', 'Latitude', 'Monthly Charges']
      X_pre[cols] = X_pre[cols].apply(lambda x: x.str.replace(',', '.')).apply(lambda x: x.str.replace(' ', '0')).apply(lambda x: pd.to_numeric(x))
      X = pd.get_dummies(X_pre)

      #Obtenemos modelo entrenado desde github
      if modelo == opa:
        url = 'https://raw.githubusercontent.com/neoncoip/telco_churn/main/modelos/aucpr-average_precision.txt'
      else: 
        url = 'https://raw.githubusercontent.com/neoncoip/telco_churn/main/modelos/aucpr-recall.txt'
      req = requests.get(url)
      with open("modelo.txt", "wb") as file:
        file.write(req.content)

      #Intanciamos y cargamos modelo entrenado y 
      model_replica = xgb.XGBClassifier()
      model_replica.load_model("modelo.txt")

      #Indicamos etiquetas
      model_replica._le = LabelEncoder().fit([0, 1])

      #Generamos predicción sobre datos, la anexamos a la planilla de datos y la mostramos
      Y = model_replica.predict(X)
      telco_sorted.insert(loc = 0, column = 'Churn prediction', value = Y)
      'Datos + Predicción'
      telco_sorted
      
      #Guardamos el archivo como csv y permitimos descargar
      telco_csv = telco_sorted.to_csv().encode('utf-8')
      st.download_button(label="Descargar datos con predicción", data=telco_csv, file_name="Predicciones_churn.csv", mime="text/csv")
