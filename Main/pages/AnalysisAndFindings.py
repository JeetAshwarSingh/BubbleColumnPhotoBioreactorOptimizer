import streamlit as st
import pandas as pd
import os
from pathlib import Path
os.chdir(Path(__file__).parent)
st.title("DATA ANALYSIS")
st.header(":blue[PRODUCTION OF BIOMASS]",divider="blue")
st.write('The correlation analysis highlights that biomass is strongly influenced by key biochemical variables in the system. It shows a very strong negative correlation with nitrate (NO₃) (-0.97), indicating that as biomass increases, nitrate concentration decreases due to nutrient consumption by the growing microalgae. Similarly, biomass has a strong negative relationship with oxygen (O₂ gas) (-0.98) and carbon dioxide (CO₂ gas) (-0.95), reflecting active metabolic processes where gas exchange is closely tied to growth.')
st.image('images/CorrelationMatrix.png')
st.write('biomass exhibits a strong positive correlation with pH (0.78) and conductivity (0.81), suggesting that changes in medium chemistry accompany biomass accumulation. Temperature shows a moderate positive correlation (0.31), indicating a supportive but less dominant role in growth, while irradiance has only a weak positive influence (0.19).')
st.write('Overall, biomass is primarily driven by nutrient utilization and metabolic activity, with environmental factors playing a secondary role.')
st.header(":blue[AFFECT OF pH]",divider="blue")
st.write('The pH was maintained in the range of 7–9, which is generally favorable for Verrucodesmus verrucosus growth. Within this range, enzyme activity and metabolic processes remain stable, allowing efficient biomass production.')
st.image('images/BiomassVspH.png')
st.write('As pH increases (within the optimal range), biomass also increases, suggesting that slightly alkaline conditions likely enhance nutrient availability and cellular activity.')
st.write('Additionally it is observed that increased Biomass Concentration is obtained at higher pH suggesting favourable condition and robust growth for the Algae as Observed in Cluster 1')
st.header(":blue[AFFECT OF NO₃]",divider="blue")
st.write('Nitrate (NO₃) plays a central role as a limiting nutrient in their dataset and shows the strongest negative correlation with biomass (-0.965).')
st.image('images/BiomassVsNO3.png')
st.write('NO₃ acts as a primary nitrogen source for Verrucodesmus verrucosus, which is essential for protein synthesis, chlorophyll formation, and overall cell growth.The strong negative correlation with biomass indicates that as biomass increases, NO₃ concentration decreases sharply. This clearly reflects active nutrient uptake by the growing microalgae')
st.header(":blue[AFFECT OF TEMPERATURE]",divider="blue")
st.write("In this dataset temperature Doesn't seem to have a any trend with growth of microbe and may seems like ambiguity in the data")
st.image('images/BiomassVsTemp.png')
st.text('But upon deeper observation it could be observed that the variation in temperature is not drastic to cause a change in growth or production of the biomass ')
