import pandas as pd 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.colors import Normalize
 
# Create dataframe form imported data
data_url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/drug_class_struct.txt"
df = pd.read_csv(data_url, sep="\t")
 
# Selected features
features = df.drop(columns=['ID', 'SMILES', 'target', 'score'])
 
# Scale the data - ensuring that each feture contribute equally
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
 
# PCA
pca = PCA(n_components=2) 
principal_components = pca.fit_transform(scaled_features)
print(f"The captured variance of total original variance in data:{np.sum(pca.explained_variance_ratio_)}%") # 58 % of total variance
print(principal_components) # --> check

# Choosing the best n_clusters number
range_n_clusters = [2, 3, 4, 5] 
best_clusters = 0                  
previous_silh = 0.0

for n_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(principal_components)
    sample_size = min(1000, len(principal_components))  # Reduce computation
    silhouette = silhouette_score(principal_components[:sample_size], cluster_labels[:sample_size])
    
    if silhouette > previous_silh:
        previous_silh = silhouette
        best_clusters = n_clusters

print(f"Best n_clusters is: {best_clusters}")

# Initialize and fit KMeans with best n_clusters
kmeans = KMeans(n_clusters=best_clusters, random_state=42)
cluster_label = kmeans.fit_predict(principal_components)
print(cluster_label)

plt.figure(figsize=(15, 6))
# Scatter plot with color based on docking score 
plt.subplot(1,2,1)
norm=Normalize(vmin=-50, vmax=50)
plt.scatter(principal_components[:, 0],principal_components[:, 1], c=df['score'], s=50, edgecolors='black', linewidths=0.5, cmap='plasma', norm=norm)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Drug Class Structures (Colored by Docking Score)')
plt.colorbar(label='Docking Score')
 
# Scatter plot with color based on clusters
plt.subplot(1,2,2)
cmap = plt.cm.viridis
plt.scatter(principal_components[:, 0], principal_components[:, 1], c=cluster_label, cmap=cmap, s=50, edgecolors='black')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Drug Class Structures (Clustered by Kmeans)')
legend_labels = np.unique(cluster_label)
# Normalize cluster labels to the range [0, 1] for the colormap
norm = plt.Normalize(vmin=cluster_label.min(), vmax=cluster_label.max())
# Create legend handles with the correct colors
handles = [mpatches.Patch(color=cmap(norm(label)), label=f'Cluster {label}') for label in legend_labels]
plt.legend(handles=handles, title="Clusters")
plt.show()
 
# Calculating the averages scores of docking scores per clusters:
average_scores = []
chemical_properties_per_cluster = {}
# Loop throught (0-1):
for index in list(set(cluster_label)):
    count = 0
    total_score = 0
    chemical_properties_per_cluster[index] = []
    for i in range(len(df)):
        if cluster_label[i] == index:
            total_score += df.iloc[i]['score']
            chemical_properties_per_cluster[index].append(features.iloc[i])
            count += 1
    average_score = total_score/count
    average_scores.append(average_score)
    print(f"Cluster {index} has average score:{average_score}.")
 
print(f"Claster with lowerst average docking score is:{average_scores.index(min(average_scores))}")
 
# Print chemical properties of chemicals with lowest average docking score:
final_df = pd.DataFrame(chemical_properties_per_cluster[average_scores.index(min(average_scores))])
print(final_df)

# Cheking the chemical differences, chosen features: MW, XLogP, HBA and HBD:
df['Cluster'] = cluster_label
grouped_df = df.groupby('Cluster')[['MW', 'XLogP', 'TPSA_NO', 'AromaticRingCount']].agg(['mean', 'std', 'min', 'max'])
print(grouped_df)
print(f"Compering Mw: mean Mw(Cluster 1)> mean Mw(Cluster 0), Cluster 1 has heavier molecules.\n",
      f"Compering XLogP: mean XLogP(Cluster 1)> mean XLogP(Cluster 0), Cluster 1 is more lipophilic (less water-soluble).\n",
      f"Compering TPSA_NO: mean TPSA_NO(Cluster 1)> mean TPSA_NO(Cluster 0), Cluster 1 has higher polarity.\n",
      f"Compering AromaticRingCount: mean ARC(Claster1)> mean ARC(Cluster 0), Cluster 1 has more aromatic rings.\n")