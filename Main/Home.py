import streamlit as st
import pandas as pd
st.title("BIOPRODUCTION OPTIMIZER")
st.header(":blue[ACKNOWLEDGEMENT]",divider="blue")
st.write('This project showcases my work in Industrial Biotechnology, carried out during my 4th semester (2026) under the guidance of [Dr Prangya Ranjan Rout](https://departments.nitj.ac.in/dept/bt/Faculty/6430447538bff038a7808ff4).')
st.write('In this study, I performed in-depth data analysis and developed machine learning models on a given dataset, achieving improved performance compared to previously reported results.')
st.write('Additionally, I identified new patterns and conducted a detailed analytical investigation based on the research article titled “A comprehensive dataset of biomass and critical variables for Verrucodesmus verrucosus culture in bubble column photobioreactors”, published by Elsevier on 22 August 2025. To review click [here](https://www.sciencedirect.com/science/article/pii/S2352340925007279)')
st.header(":blue[DATA DESCRIPTION]",divider="blue")
st.write('The dataset is derived from controlled cultivation experiments of the microalgae Verrucodesmus verrucosus grown in a bubble column photobioreactor using BG-11 medium. The inoculum was initially prepared at a cell density of 1 × 10⁶ cells/mL and incubated under a 12:12 light–dark cycle with a light intensity of 2000 lux to promote growth. The culture was maintained in a 2.25 L photobioreactor with continuous aeration and LED illumination in the 450–700 nm range, while key environmental conditions such as pH (7–9) and temperature were carefully regulated. Biomass was measured using the dry weight method by filtering samples and drying them at 75 °C, ensuring high precision.')
st.header(":blue[ABOUT THE DATASET]",divider="blue")
data = {
    "Feature": [
        "Irradiance",
        "NO3",
        "Temperature",
        "pH",
        "Biomass",
        "O2 Gas",
        "CO2 Gas",
        "OD",
        "Conductivity"
    ],
    "Description": [
        "Light intensity provided to the culture (lux), influencing photosynthesis",
        "Nitrate concentration (NO₃), a key nutrient for microalgal growth",
        "Culture temperature affecting metabolic activity",
        "pH level of the medium, maintained between 7–9",
        "Biomass concentration measured using dry weight method",
        "Dissolved or gaseous oxygen produced during photosynthesis",
        "Carbon dioxide concentration supplied/consumed in the system",
        "Optical density indicating cell concentration in culture",
        "Electrical conductivity representing ionic strength of the medium"
    ]
}

df1 = pd.DataFrame(data)
st.dataframe(df1)
st.header(":blue[ABOUT THE BIOREACTOR]",divider="blue")
st.text('A bubble column photobioreactor (BCPR) is a vertical, cylindrical vessel used to cultivate microalgae by feeding gas into the bottom, promoting mixing and mass transfer through bubble flow. ')
st.image('images/BubbleColumnBioreactor.jpg',width=700)
st.text('It has a simple design with an aspect ratio (height-to-diameter) usually ranging between 2 to 6, often using a sparger at the base to control bubble size.')
st.text('Uses upward gas flow for mixing, eliminating the need for mechanical agitation, diameter is often kept below 20 cm to minimise mutual shading and ensure light penetrates all cells.')
st.header(":blue[ML ALGORITHMS IMPLEMENTED ]",divider="blue")
st.image("images/randomForestImage.png")
st.write(
    "In this project, I implemented three machine learning models: Linear Regression, "
    "XGBoost, and Random Forest. Among these, the Random Forest model delivered the best performance. "
    "The evaluation metrics obtained were: R² Score = 0.986, "
    "Mean Absolute Percentage Error (MAPE) = 0.058, and "
    "Mean Absolute Error (MAE) = 0.069."
)
st.header(":blue[CITATION]",divider="blue")
st.markdown(':grey[Hector Ricardo Hernandez-de Leon, Julio Cesar Martinez-Morgan, Jose Armando Fragoso-Mandujano, Hector Rodriguez-Rangel, Leonel Ernesto Amabilis-Sosa, Sheyla Karina Flores-Guirao,A comprehensive dataset of biomass and critical variables for Verrucodesmus verrucosus culture in bubble column photobioreactors,Data in Brief,Volume 62,2025,112003,ISSN 2352-3409 (https://www.sciencedirect.com/science/article/pii/S2352340925007279)]')