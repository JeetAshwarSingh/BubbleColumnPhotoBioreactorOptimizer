import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import mean_absolute_error,r2_score,mean_absolute_percentage_error
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

def CorrectionMap( df : pd.DataFrame) -> None:
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

def FrequencyDistribution( df : pd.Series) -> None:
    temp = df.name
    plt.figure(figsize=(8,5))
    sns.histplot(df, bins=30, kde=True)
    plt.title("FrequencyDistribution")
    plt.xlabel(f"{temp}")
    plt.ylabel("Frequency")
    plt.show()

def BoxPlot( df : pd.DataFrame , feature1 : str ,feature2 : str) -> None :
    plt.figure(figsize=(8,5))
    sns.boxplot(x=feature1, y=feature2, data=df)
    plt.title(f"{feature1} vs {feature2}")
    plt.show()

def ScatterPlot( df : pd.DataFrame , feature1 : str ,feature2 : str) -> None :
    plt.figure(figsize=(8,5))
    sns.scatterplot(x=feature1, y=feature2, data=df, color = "lightblue")
    plt.title(f"{feature1} vs {feature2}")
    plt.show()

def Pairplot(df : pd.DataFrame, *cols: str) -> None:
    sns.pairplot(df[list(cols)])
    plt.show()

def ScatterPlotAfterPrediction(y_test, y_predict):
    
    y_test = np.array(y_test)
    y_predict = np.array(y_predict)
    r2 = r2_score(y_test, y_predict)
    rmse = np.sqrt(mean_absolute_error(y_test, y_predict))

    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_predict, color='lightblue', alpha=0.7)

    plt.plot([y_test.min(), y_test.max()],
             [y_test.min(), y_test.max()],
             color='limegreen', linestyle='--', label='Perfect Fit')

    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title("Actual vs Predicted")

    plt.text(
        0.05, 0.95,
        f"R² = {r2:.3f}\nRMSE = {rmse:.3f}",
        transform=plt.gca().transAxes,
        fontsize=11,
        verticalalignment='top',
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.6)
    )
    plt.legend()
    plt.tight_layout()
    plt.show()

def PredictionPlotResidual(y_test, y_predict) -> None:
    y_test = np.array(y_test)
    y_predict = np.array(y_predict)
    errors = y_test - y_predict
    plt.figure(figsize=(8,4))
    plt.plot(errors, color='grey')
    plt.axhline(0, linestyle='--')
    plt.xlabel("Index")
    plt.ylabel("Residuals (Actual - Predicted)")
    plt.title("Residual Plot")
    plt.tight_layout()
    plt.show()

def LinePlotAfterPrediction(y_test, y_predict) -> None:
    y_test = np.array(y_test)
    y_predict = np.array(y_predict)
    plt.figure(figsize=(8,5))
    plt.plot(y_test, label='Actual', color='limegreen')
    plt.plot(y_predict, label='Predicted', color='lightblue')
    plt.xlabel('Number of Values')
    plt.ylabel('Biomass')
    plt.title('Actual vs Predicted')
    plt.legend()
    plt.tight_layout()
    plt.show()

def ElbowMethod(df :pd.DataFrame) -> None:
    inertia = []

    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(df)
        inertia.append(kmeans.inertia_)

    plt.plot(range(1,10), inertia, marker='o')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.title('Elbow Method')
    plt.show()

def SilhouetteScore(df : pd.DataFrame) -> None:
    for k in range(2, 8):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(df)
        score = silhouette_score(df, labels)
        print(f"K={k}, Score={score}")

def ClusterSummary(df : pd.DataFrame):
    cluster_summary = df.groupby('Cluster').mean()
    print(cluster_summary)