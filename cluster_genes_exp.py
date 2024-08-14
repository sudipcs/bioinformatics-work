#!/usr/bin/env python
# coding: utf-8

# ### Cluster genes based on their expression patterns across samples. Visualize the representative expression profile for each identified cluster. Do the inverse, i.e., cluster samples based and plot gene signatures.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Read the gene expression data from T2.txt file
data = pd.read_csv("T2.txt", sep="\t", index_col=0)

# Number of clusters
num_clusters = 4

# Apply PCA for dimensionality reduction
pca = PCA(n_components=2)
pca_result = pca.fit_transform(data)

# Apply KMeans clustering on PCA-transformed data
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(pca_result)

# Visualize the PCA-transformed data and cluster assignments
plt.figure(figsize=(8, 6))
for cluster_num in range(num_clusters):
    cluster_genes = data.index[cluster_labels == cluster_num]
    print(cluster_genes)
    plt.scatter(pca_result[cluster_labels == cluster_num, 0],
                pca_result[cluster_labels == cluster_num, 1],
                label=f'Cluster {cluster_num + 1}')

plt.xlabel('Principal_Component_1')
plt.ylabel('Principal_Component_2')
plt.title('PCA and KMeans Clustering for Gene Expression Data')
plt.legend()
plt.show()


# In[2]:


import pandas as pd
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

data = pd.read_csv("T2.txt", sep="\t", index_col=0) # Assuming the first column contains gene names

arr = data.to_numpy()
#print('\nNumpy Array\n----------\n', arr)

# Perform hierarchical clustering
linkage_matrix = hierarchy.linkage(data.T, method='average')  # Transpose the DataFrame

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram = hierarchy.dendrogram(linkage_matrix, labels=data.columns)
plt.title('Gene Clustering based on Expression Patterns')
plt.xlabel('Samples')
plt.ylabel('expression')
plt.show()


# ### Attached are two matrices T3_M1.txt and T3_M2.txt. Can you think of any statistical test to test for differences/similarity between any two matrices by preserving the matrix structure?

# In[3]:


import numpy as np
from scipy.stats import ks_2samp

# Load your matrices (m1 and m2) as NumPy arrays
m1 = np.loadtxt('T3_M1.txt')
m2 = np.loadtxt('T3_M2.txt')
# Perform K-S Test between two matrices
ks_statistic, p_value = ks_2samp(m1.flatten(), m2.flatten())

# Output the test statistic and p-value
print("K-S Statistic:", ks_statistic)
print("P-Value:", p_value)

# Interpret the results
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis i.e. The two matrices have different distributions.")
else:
    print("Fail to reject the null hypothesis i.e The two matrices have similar distributions.")


# In[4]:


import numpy as np
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
from scipy.stats import pearsonr

# Load your matrices
m1 = np.loadtxt('T3_M1.txt')
m2 = np.loadtxt('T3_M2.txt')

# Calculate pairwise Euclidean distances for the matrices
distances_m1 = squareform(pdist(m1))
distances_m2 = squareform(pdist(m2))

# Perform the Mantel test
mantel_corr, mantel_p_value = pearsonr(distances_m1.flatten(), distances_m2.flatten())

# Output the Mantel correlation and p-value
print(f"Mantel Correlation: {mantel_corr}")
print(f"P-value: {mantel_p_value}")

# Interpret the results
if mantel_p_value < 0.05:
    print("There is a significant correlation between the matrices, i.e similarities.")
else:
    print("There is no significant correlation between the matrices, i.e dissimilarities.")


# In[ ]:




