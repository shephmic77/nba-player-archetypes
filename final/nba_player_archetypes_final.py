"""
NBA Player Archetypes - Final Analysis
Michael Shepherd

A cleaned final version reconstructed from the original development files.
It preserves the later 10-cluster K-Means direction while making the workflow
complete and reproducible.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

DATA_FILE = "2023-2024 NBA Player Stats - Regular.csv"

df = pd.read_csv(DATA_FILE, encoding="latin1", sep=";")

# Keep one row per player. If a player changed teams, use the season-total row.
tot_players = set(df.loc[df["Tm"] == "TOT", "Player"])
df = df[~(df["Player"].isin(tot_players) & (df["Tm"] != "TOT"))].copy()

features = ["PTS", "AST", "TRB", "STL", "BLK", "TOV", "FG%", "3P%", "FT%", "MP"]
for col in features:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Filter out very small samples.
analysis = df[(df["G"] >= 20) & (df["MP"] >= 10)].copy()
analysis = analysis.dropna(subset=features).reset_index(drop=True)

scaler = StandardScaler()
X = scaler.fit_transform(analysis[features])

kmeans = KMeans(n_clusters=10, random_state=42, n_init=50)
analysis["Cluster"] = kmeans.fit_predict(X)

centroids = pd.DataFrame(kmeans.cluster_centers_, columns=features)

cluster_names = {
    0: "Playmaking Scorers",
    1: "Low-Usage Interior Finishers",
    2: "Bench Guards / Wings",
    3: "All-Around Stars",
    4: "Rebounding Forwards / Bigs",
    5: "Two-Way Rotation Wings",
    6: "High-Impact Rim Protectors",
    7: "Low-Usage Perimeter Players",
    8: "Interior Centers",
    9: "Shooting-Efficiency Outliers",
}

analysis["Archetype"] = analysis["Cluster"].map(cluster_names)

distances = kmeans.transform(X)
analysis["Distance_to_Centroid"] = distances[np.arange(len(analysis)), analysis["Cluster"]]

print("Players analyzed:", len(analysis))
print("Silhouette score:", round(silhouette_score(X, analysis["Cluster"]), 3))
print(analysis["Archetype"].value_counts())

analysis.to_csv("nba_2023_24_player_archetypes.csv", index=False)
centroids.assign(Archetype=pd.Series(cluster_names)).to_csv(
    "cluster_centroids_standardized.csv", index_label="Cluster"
)
