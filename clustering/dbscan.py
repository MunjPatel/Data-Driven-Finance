from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# generating synthetic stock return data
np.random.seed(42)
data_core = np.random.rand(1950, 3)  # core dense data (main clusters)
data_outliers = np.random.uniform(low=0.2, high=1.7, size=(50, 3))  # introducing outliers
data = np.vstack((data_core, data_outliers))  # combining core data and outliers

# applying DBSCAN
dbscan = DBSCAN(eps=0.1, min_samples=10)
clusters = dbscan.fit_predict(data)

# plotting 3d DBSCAN clustering
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(
    data[:, 0],
    data[:, 1],
    data[:, 2],
    c=clusters,
    cmap='viridis',
    alpha=0.7
)
ax.set_title("DBSCAN Clustering with Outliers")
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_zlabel("Feature 3")
plt.colorbar(scatter, label="Cluster")
plt.show()