BubbleColumnPhotoBioreactorOptimizer

In-depth data analysis, machine learning modeling, and optimization of microalgal growth in bubble column photobioreactors — achieving state-of-the-art predictive performance on a newly published dataset.

Overview
This repository contains all files required to reproduce the experiment on bubble column photobioreactor (BCPR) data for cultivating the microalgae Verrucodesmus verrucosus. It covers the complete workflow from raw data exploration to machine learning model training and evaluation.

The study is based on the research article:
"A comprehensive dataset of biomass and critical variables for Verrucodesmus verrucosus culture in bubble column photobioreactors"
Published by Elsevier, 22 August 2025
In addition to reproducing baseline findings, this project identifies new patterns and delivers improved ML model performance compared to previously reported results.

About the Dataset
The dataset is derived from controlled cultivation experiments of Verrucodesmus verrucosus grown in a bubble column photobioreactor using BG-11 medium.

Experimental Conditions:
Inoculum cell density: 1 × 10⁶ cells/mL
Light cycle: 12:12 (light:dark)
Light intensity: 2000 lux
LED illumination range: 450–700 nm
Reactor volume: 2.25 L
pH range maintained: 7–9
Biomass measurement: Dry weight method (filtered and dried at 75 °C)

About the Bubble Column Photobioreactor
A bubble column photobioreactor (BCPR) is a vertical, cylindrical vessel designed to cultivate microalgae through bottom-fed gas flow, enabling efficient mixing and mass transfer without mechanical agitation.

Key Design Features:
Simple cylindrical geometry with an aspect ratio (height-to-diameter) typically between 2 and 6
Uses a sparger at the base to control bubble size and distribution
Upward gas flow provides mixing, eliminating the need for mechanical stirrers
Diameter is generally kept below 20 cm to minimize mutual shading and ensure light penetration to all cells

Key Findings & Biological Insights
Correlation Analysis — What Drives Biomass?
Variable        	Correlation with Biomass	Relationship
NO₃             	−0.97                  	Strong negative
O₂ Gas          	−0.98                  	Strong negative
CO₂ Gas         	−0.95                  	Strong negative
Conductivity    	+0.81                  	Strong positive
pH              	+0.78                  	Strong positive
Temperature     	+0.31                  	Moderate positive
Irradiance      	+0.19                  	Weak positive

Effect of Nitrate (NO₃)
Nitrate shows the strongest negative correlation with biomass (−0.965), making it the primary limiting nutrient in this system.
NO₃ serves as the principal nitrogen source for Verrucodesmus verrucosus, essential for protein synthesis, chlorophyll formation, and cell growth
As biomass increases, NO₃ concentration decreases sharply, reflecting active and efficient nutrient uptake by the growing microalgae
This pattern is consistent with classical nitrogen-limited microalgal growth dynamics

Effect of pH
Biomass shows a strong positive correlation with pH (0.78), suggesting that slightly alkaline conditions favor growth
The pH range of 7–9 maintained in this study is generally optimal for Verrucodesmus verrucosus, keeping enzyme activity and metabolic processes stable
Cluster 1 in the dataset particularly highlights higher biomass concentrations at elevated pH, indicating robust growth under favorable alkaline conditions

Effect of Temperature
Temperature shows only a moderate positive correlation (0.31) with biomass
The variation in temperature within the dataset is not drastic enough to cause a significant change in growth or biomass production
This suggests temperature acted as a supportive, stable background variable rather than a growth-limiting factor in this experimental setup

Gas Exchange (O₂ and CO₂)
O₂ Gas (−0.98) and CO₂ Gas (−0.95) both show strong negative correlations with biomass
This directly reflects active photosynthetic metabolism: as microalgae grow, they consume CO₂ and produce O₂, altering gas concentrations measurably
These variables serve as strong indirect indicators of biological activity and culture health

Machine Learning Models
Three regression models were implemented and evaluated for predicting biomass concentration:
The Random Forest model delivered the best performance, achieving an R² of 0.986 — representing improved results over previously reported benchmarks for this dataset.

If you use this work or the dataset, please cite the original article:
"A comprehensive dataset of biomass and critical variables for Verrucodesmus verrucosus culture in bubble column photobioreactors", Elsevier, 22 August 2025.
https://www.sciencedirect.com/science/article/pii/S2352340925007279

and lastly if you want detailed overview key insights along with the graphs of analysis done by me please visit - "https://bubblecolumnphotobioreactoroptimizer.streamlit.app" ( if the website is sleeping just press the button present in the centre website will be live in 5-15 seconds )
