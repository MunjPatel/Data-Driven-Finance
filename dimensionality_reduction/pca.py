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
ax.scatter(data_reduced[:, 0], data_reduced[:, 1], data_reduced[:, 2], c='b', alpha=0.6)
ax.set_title("PCA Projection")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")
plt.show()

