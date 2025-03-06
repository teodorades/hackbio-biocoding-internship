import pandas as pd 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.patches as mpatches
from matplotlib.colors import Normalize
 
# Import data and create dataframe
data = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/drug_class_struct.txt"
df = pd.read_csv(data, sep="\t")
 
# Select only numeric columns for PCA analysis that has only chemical properties
numeric_columns = df.drop(columns=['ID', 'SMILES', 'target'])
 
# Scale the data - before applying the clustering algoritham, ensuring that each feture contribute equally
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_columns)
 
# PCA
pca = PCA(n_components=2) # 2D
principal_components = pca.fit_transform(scaled_data)
print(np.sum(pca.explained_variance_ratio_)) # 56 % of total variation
print(principal_components) # --> check
 
# Initialize KMeans with 5 clusters:
kmeans = KMeans(n_clusters=5, random_state=42)
# Fit the model, and indices of the cluster each sample belongs to:
indices = kmeans.fit_predict(principal_components)
print(indices)
 
 
plt.figure(figsize=(15, 6))
 
# Scatter plot with color based on docking score 
plt.subplot(1,2,1)
norm=Normalize(vmin=-50, vmax=50)
plt.scatter(principal_components[:, 0],principal_components[:, 1], c=df['score'], s=50, edgecolors='black', linewidths=0.5, cmap='plasma', norm=norm)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Drug Class Structures (Colored by Docking Score')
plt.colorbar(label='Docking Score')
 
# Scatter plot with color based on clusters
plt.subplot(1,2,2)
plt.scatter(principal_components[:, 0], principal_components[:, 1], c=indices, s=50, edgecolors='black')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Drug Class Structures (Clustered by Kmeans)')
legend_labels = list(set(indices))
handles = [mpatches.Patch(color=plt.cm.viridis(i/4),label=legend_labels[i]) for i in range(len(legend_labels))]
plt.legend(handles=handles)
plt.show()
 
# Calculating the averages scores of docking scores per clusters:
average_scores = []
chemical_properties_per_cluster = {}
# Loop throught (0-4):
for index in list(set(indices)):
    count = 0
    sum = 0
    chemical_properties_per_cluster[index] = []
    for i in range(len(df)):
        if indices[i] == index:
            sum += df.iloc[i]['score']
            chemical_properties_per_cluster[index].append(numeric_columns.iloc[i])
            count += 1
    average_score = sum/count
    average_scores.append(average_score)
    print(f"Cluster {index} has average score:{average_score}.")
 
print(f"Claster with lowerst average docking score is:{average_scores.index(min(average_scores))}")
 
# Print chemical properties of chemicals with lowest average docking score:
final_df = pd.DataFrame(chemical_properties_per_cluster[average_scores.index(min(average_scores))])
print(final_df)