Import necessary libraries (`pandas`, `sklearn.decomposition import PCA`, `from sklearn.preprocessing import StandardScaler`, `matplotlib.pyplot`, `from sklearn.cluster import KMeans`, `from sklearn.metrics import silhouette_score`, `numpy`, `matplotlib.patches as mpatches`, and `matplotlib.colors import Normalize`)

1) Create dataframe from imported data.
2) Select only numeric columns that has chemical properties (`.drop` method is used).
3) Scale the data with `StandardScaler()` to ensure that each feture contribute equally, before applying the PCA and clustering (Kmeans) algoritham.
4) PCA, n_components=2 (2D) - the goal is to reduce the dimensionality of a dataset while preserving as much variance (information) as possible.
**Printed output:** used for PCA graph:

Principal component 1 (PC1) and Principal component 2 (PC2):
```text
< [[ 2.51699613 -1.56144603]
<  [-0.11059088  3.93586821]
<  [ 5.35368569  3.36829477]
<  ...
<  [ 2.51128302  3.52608307]
<  [-0.63269646 -0.85170953]
<  [ 3.15243514  3.33707233]]
```
 * To ensure that PCA is shows the enought varience between the selected features: `p.sum(pca.explained_variance_ratio_)` was used! It shows that (0.5787931695723) 58 % of total  variance of original features is captured by each principal component.

5) Initializing the KMeans with chosen clusters. The best n_clusters number (`best_clusters`) is  chosen with `silhouette_score`.      So, the range of n_clusters were chosen [2,3,4,5] and the loop was created to go trought the range and compere the calculated silhouette with previously calculated silhouette.
 * but maybe for our case this is not the best solution --> because we have a lot of structures, and it will better to use bigger k value, to see wider diversity
* The list `cluster_label` is created to store the information of clusters labels for each chemical compound in the original dataframe.
**Printed output:**

List for indices:
```text
< [1 0 1 ... 1 0 1]
```
6) Plotting the Figure with two subplots, `plt.subplot(1,2,1)` is plot that shows PCA graph colored by the docking score (column: `score`), and `plt.sublot(1,2,2) is PCA graph colored by clusters.

**Figure**
![image](https://github.com/user-attachments/assets/ea65666c-0105-4b1e-b77c-f3f934f94619)

7) Creating the loop for calculating the average scores (`average_score`) of docking scores per clusters. First loop goes through unique set of `index` in indices list. Second loop goes through the all rows in original dataframe (df).                           Append all chemical properties information into the dictionary `chemical_properties_per_cluster = {}` where **key** is cluster number (`index` in loop), and **values** are chemical properties.

**Printed output:**
```text
Clusters average scores:
< Cluster 0 has average score:-68.15697424293974.
< Cluster 1 has average score:-73.84337848531261.
```
**Printed output:**
```text
Cluster with lowest average docking score is: 1
```
8) Compering selected features (Mw, XLogP, TPSA_No, and AromaticRingCount) to make final conclusions.
