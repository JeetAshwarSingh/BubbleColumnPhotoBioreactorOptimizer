import streamlit as st 
import pickle
import pandas as pd
with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
st.title("MODEL EVALUATION")
st.header(":blue[MODEL PERFORMANCE METRIX]",divider="blue")
st.text(
    "Model comparison shows that Random Forest achieved the best overall performance "
    "with the highest R² score and the lowest error values (MAE and MAPE). "
)
st.image('images/ModelEvaluation.png')
st.text("XGBoost also performed strongly and was close to Random Forest, while Linear "
    "Regression showed comparatively lower accuracy and higher prediction error. "
    "Overall, ensemble-based models performed better for this dataset.")
st.header(":blue[PERFORMANCE OF RANDOM FOREST]",divider="blue")
st.text('As it can be seen from the from the graph the model had an exceptional fitting on the data.')
st.image('images/FittingPlot.png')
st.text('one can suspect overfitting on the data but these claims can be quashed on the basis that of correlation between the parameters.')
st.text('The graph below is the residualplot of predicted vs actual values')
st.image('images/ResidualPlot.png')
st.text('A residual plot is a graph used in regression analysis to check how well a machine learning model fits the data.')
st.text('The graph below shows the lineplot of the data vs the actual predicted value.')
st.image('images/lineplot.png')
st.text('This indicates the exceptional understanding of randomforest on this dataset. showcasing the true power and potential of emsemble models.')
st.header(':blue[CLUSTERING FOR PATTERN IDENTIFICATION]',divider="blue")
st.text('for selection of n for formation of cluster i used Elbow plot and silhouette score, and based upon output provided by them i picked value of n to be considered 2.')
st.image('images/Elbowplot.png')
st.write('Based upon the findings in Elbowplot KMean cluster algorithm was applied which in turn lead to application of Principal component analysis (PCA) for dimensionality reduction and better visualisation.')
st.image('images/PcaCluster.png')
st.text(' As it can be observed from the PCA value 2 suits best for the clustering algorithm supporting and justifying the previous assumption of it being 2 two.')
st.header(':blue[MODEL DEMO]',divider="blue")
CO2 = st.slider("What is Concentration of CO₂(ppm)",400,900,value=600,step=1)
O2 = st.slider("What is Concentration of O₂(in %)",8,12,value=9,step=1)
NO3 = st.slider("What is Concentration of NO₃(mg/L)",20,250,value=50,step=1)
Conductivity = st.slider("What is Conductivity(μScm⁻¹)",280,310,value=300,step=1)
pH = st.slider("What is pH",6,10,value=8,step=1)
Irradiance = st.slider("What is Irradiance(μmol/m²s)",75,200,value=100,step=1)
Temperature = st.slider("What is Temperature°C",19,24,value=22,step=1)
if st.button(":blue[GET RESULT]"):
    x = pd.DataFrame([[
    Irradiance,
    NO3,
    Temperature,
    pH,
    O2,
    CO2,
    Conductivity
    ]], columns=[
    "Irradiance",
    "NO3",
    "Temperature",
    "pH",
    "O2 Gas",
    "CO2 Gas",
    "Conductivity"
    ])
    biomass = loaded_model.predict(x)
    st.success(f"Predicted Biomass: {biomass[0]:.4f}")
col1, col2, col3, col4, col5,col6 = st.columns([1,1,3,2, 1,2])
with col4:
    if st.button(":grey[THE END]"):
        st.subheader(" :green[Thanks for Reading :)] ")