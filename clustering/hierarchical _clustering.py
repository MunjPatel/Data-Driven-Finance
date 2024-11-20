from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import numpy as np

# generating synthetic stock return data
np.random.seed(42)
data = np.random.rand(2000, 3) 

# performing hierarchical clustering
linkage_matrix = linkage(data, method='ward')

# plotting dendrogram
plt.figure(figsize=(12, 8))
dendrogram(
    linkage_matrix,
    truncate_mode="lastp",  
    p=50,                 
    leaf_rotation=90.,    
    leaf_font_size=10.,    
    show_contracted=True
)
plt.title("Hierarchical Clustering Dendrogram for Systemic Risk Detection")
plt.xlabel("Data Point Index")
plt.ylabel("Distance")
plt.show()