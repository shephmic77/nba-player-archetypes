import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset (replace 'nba_stats.csv' with your actual file)
df = pd.read_csv('nba_24_25.csv')

# Select relevant columns for clustering (customize this based on your dataset)
features = ['PTS', 'AST', 'TRB', 'STL', 'BLK', 'FG%', '3P%', 'GmSc']  # Use actual columns
df = df[features]

# Normalize data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)  # 5 clusters as an example
df['Cluster'] = kmeans.fit_predict(scaled_features)

# Visualizing clusters (e.g., PTS vs AST)
plt.scatter(df['PTS'], df['AST'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Points Per Game')
plt.ylabel('Assists Per Game')
plt.title('NBA Player Clustering')
plt.show()

