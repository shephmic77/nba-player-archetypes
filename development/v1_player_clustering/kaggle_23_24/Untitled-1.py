import pandas as pd
import plotly.express as px
import chardet
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# **Step 1: Detect Encoding Automatically**
file_path = r"C:\Users\mikey\Desktop\NBA val\V1\start 2_12_25_Cluster\Kaggle 23_24\2023-2024 NBA Player Stats - Regular.csv"

# Detect file encoding
with open(file_path, "rb") as f:
    result = chardet.detect(f.read(100000))  # Read first 100,000 bytes
    detected_encoding = result["encoding"]
    print("Detected Encoding:", detected_encoding)

# **Step 2: Load Dataset with Correct Encoding**
df = pd.read_csv(file_path, encoding=detected_encoding)

# Inspect the first few rows
print(df.head())

# **Step 3: Data Exploration**
print(df.columns)  # Show available columns
print(df.info())  # Check for missing values
print(df.describe())  # Summary statistics

# **Step 4: Select Relevant Stats for Clustering**
selected_features = [
    "PTS",   # Points per game
    "AST",   # Assists per game
    "TRB",   # Total rebounds per game
    "STL",   # Steals per game
    "BLK",   # Blocks per game
    "TOV",   # Turnovers per game
    "3P%",   # Three-point percentage
    "FG%",   # Field goal percentage
    "FT%",   # Free throw percentage
    "MP"     # Minutes per game (to filter out low-minute players)
]

# Filter dataset to only include selected columns (dropping NaNs)
df_filtered = df[selected_features].dropna()

# **Step 5: Normalize the Data**
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_filtered)

# **Step 6: Apply K-Means Clustering**
num_clusters = 10  # Adjust number of clusters if necessary
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
df_filtered["Cluster"] = kmeans.fit_predict(df_scaled)

# **Step 7: Add Player Names & Clusters Back to the Main Data**
df_filtered["Player"] = df["Player"]  # Ensure the column name matches your dataset
df["Cluster"] =
