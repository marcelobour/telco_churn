# Telco Churn

Este proyecto analiza los datos de clientes de una empresa de telecomunicaciones 
y diseña soluciones para disminuir el churn (baja de clientes).
  
El proyecto se desarrolla en 3 ejes:
*  Análisis exploratorio de los datos.
*  Creación de modelos predictivos de churn.
*  Implementación de modelos predictivos a través de Web Apps.

## Tech Stack

**Análisis:** Python, Numpy, Pandas, Matplotlib, Seaborn, Plotly, Google Colab

**Predicción:** XGBoost, Scikit-Learn

**Web Apps:** Streamlit


## Content

1. **Análisis Exploratorio del dataset**
[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZQnyETsrGXiIqxI5QOmK-CpBnxxyiYw1)
Aquí encontramos un exhaustivo análisis y una completa intepretación de todas la variables, un análisis univariado del efecto sobre el churn de cada una y la clasificación e interpretación de los motivos de baja.

2. **Modelos predictivos XGB**
[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1LN329kdfCsPbfyL9yPgW1lLzq6Elu_k9)
Utilizando XGBoost se plantean 2 modelos, uno orientado a precisión y otro a captura (recall).

3. **Web App 1: Predicción por formularios**
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://telco-churn-prediccion-por-archivo.streamlit.app/)
Los modelos predictivos de la sección 2 se implementan en una solución tipo web app. Cargando un archivo de datos de clientes se obtiene la predicción para cada uno.

4. **Modelo predictivo para app2**
[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mAljIO4qR_3l-ufKnFnwRDu70YZ7J7I0)
Se analiza y genera un modelo con menor cantidad de variables para implementar en la web app2.

5. **Análisis de impacto y diseño de retención preventiva**
[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Mil7F0M8OejNTuZM_MRfRBGkAsyxR16z)
Se diseña un agregado en el procedimiento de atención para el canal técnico con el objetivo de disminuir la probabilidad de baja del cliente. Se evaluan costos, alcance e impacto.

6. **Web App 2: Probabilidad de baja**
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://telco-churn-probabilidad-baja-por-formulario.streamlit.app/)
Un modelo predictivo de 8 variables es utilizado para conocer la probabilidad de baja y ejecutar directivas según los escenarios estudiados en la sección 5. El flow del proceso puede verse [aquí](https://docs.google.com/presentation/d/1eqBfX3qzZ_CABcjgoiHDySgU-elu64DJCei-NLWb4uM/edit?usp=sharing).

## Acknowledgements

 - [Dataset IBM obtenido de Kaggle](https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset)
 - [Descripción del Dataset IBM](https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113)
## Agradecimientos

A Juan Arístide por iluminarme con muchos temas nuevos, responderme preguntas kilométricas y ser desde hace años mi referente en el mundo tech.  
A Esteban Manrupe por ser junto a Juan los primeros en darme feedback del proyecto.  
A Alfredo Carella por aconsejarme sobre la estructura y diferentes líneas de desarrollo del proyecto.  
A Teresa Codagnone por inspirarme a ser un profesional con orgullo y alegría.