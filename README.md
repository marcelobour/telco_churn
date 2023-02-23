# Telco Churn

This project analyzes customer data from a telecommunications company and designs solutions to reduce churn (customer loss).
  
The project is developed in 3 areas:
*  Exploratory data analysis.
*  Creation of churn predictive models.
*  Implementation of predictive models through Web Apps.

## Tech Stack

**Analysis:** Python, Numpy, Pandas, Matplotlib, Seaborn, Plotly, Google Colab

**Prediction:** XGBoost, Scikit-Learn

**Web Apps:** Streamlit


## Content

1. **Exploratory data analysis**
[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZQnyETsrGXiIqxI5QOmK-CpBnxxyiYw1)  
Here you can find a comprehensive analysis and interpretation of all variables, a univariate analysis of the effect of each one on churn, and the classification and interpretation of reasons for customer loss.

2. **XGB predictive models**
[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1LN329kdfCsPbfyL9yPgW1lLzq6Elu_k9)  
Using XGBoost, two models are proposed, one focused on accuracy and the other on recall.

3. **Web App 1: Prediction by forms**
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://telco-churn-prediccion-por-archivo.streamlit.app/)  
The predictive models from section 2 are implemented in a web app solution. By loading a customer data file, a prediction is obtained for each one.

4. **Predictive model for app2**
[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mAljIO4qR_3l-ufKnFnwRDu70YZ7J7I0)  
A model with fewer variables is analyzed and generated to implement in web app2.

5. **Impact analysis and preventive retention solution design**
[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Mil7F0M8OejNTuZM_MRfRBGkAsyxR16z)  
An addition to the technical support procedure is designed with the aim of reducing the probability of customer loss. Costs, scope, and impact are evaluated.

6. **Web App 2: Probabilidad de baja**
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://telco-churn-probabilidad-baja-por-formulario.streamlit.app/)  
A predictive model with 8 variables is used to determine the probability of churn and execute directives according to the scenarios studied in section 5. The process flow can be seen [here](https://docs.google.com/presentation/d/1eqBfX3qzZ_CABcjgoiHDySgU-elu64DJCei-NLWb4uM/edit?usp=sharing).

## Acknowledgements

 - [Dataset IBM obtenido de Kaggle](https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset)
 - [Descripción del Dataset IBM](https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113)

## Thanks

To Juan Arístide for enlightening me with many new topics, answering my kilometric questions, and being my reference in the tech world for years.
To Esteban Manrupe for being one of the first to give me feedback on the project, alongside Juan.
To Alfredo Carella for advising me on the structure and different lines of development of the project.
To Teresa Codagnone for inspiring me to be a professional with pride and joy.
