import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
file_path = "C:\\Users\\mikey\\Desktop\\NBA val\\V1\\nba_24_25.csv"
df = pd.read_csv(file_path)

# Select relevant columns (basic + advanced metrics)
print(df.columns)
features = ['PTS', 'AST', 'TRB', 'STL', 'BLK', 'FG%', '3P%']
df_cluster = df[features]

# Normalize the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_cluster)

# Apply K-Means clustering with 8 clusters based on specific roles
kmeans = KMeans(n_clusters=8, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(df_scaled)

# Define cluster role labels
cluster_labels = {
    0: 'Stars',
    1: 'Playmakers',
    2: 'Three-Point Specialists',
    3: 'Mid-Range Specialists',
    4: 'Slashers',
    5: 'Perimeter Defenders',
    6: 'Interior Defenders',
    7: 'Two-Way'
}
df['Cluster Name'] = df['Cluster'].map(cluster_labels)

# Identify players excelling in multiple roles (e.g., belonging to multiple clusters)
df['Multi-Role'] = df_cluster.apply(lambda row: sum(row > row.mean() + row.std()), axis=1) > 2
df['Marker'] = df['Multi-Role'].apply(lambda x: '⭐' if x else '')

# Interactive visualization with legend and markers
fig = px.scatter(
    df, x='PTS', y='AST', color='Cluster Name',
    hover_data=['Player', 'PTS', 'AST', 'TS%', 'PER', 'USG%', 'Marker'],
    title='NBA Player Clustering (Interactive)',
    labels={'PTS': 'Points Per Game', 'AST': 'Assists Per Game'},
    symbol='Marker'
)
fig.update_layout(legend_title='Player Role')
fig.show()
