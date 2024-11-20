from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# generating synthetic data
np.random.seed(42)
n_obs, n_features = 2000, 10
data = np.random.rand(n_obs, n_features)

# applying PCA
pca = PCA(n_components=3)
data_reduced = pca.fit_transform(data)

# 3d visualization
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(
    data_reduced[:, 0], 
    data_reduced[:, 1], 
    data_reduced[:, 2], 
    c=np.arange(n_obs),  
    cmap='viridis', 
    alpha=0.7
)

# setting titles and labels
ax.set_title("3D PCA Projection for Portfolio Risk")
ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_zlabel("Principal Component 3")

# adding colorbar for interpretation
plt.colorbar(scatter, label="Observation Index")
plt.show()
