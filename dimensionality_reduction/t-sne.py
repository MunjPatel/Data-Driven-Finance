from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt

# generating synthetic market data
np.random.seed(42)
data = np.random.rand(2000, 10)

# applying t-SNE
tsne = TSNE(n_components=3, random_state=42)
data_reduced = tsne.fit_transform(data)

# 3d visualization
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(
    data_reduced[:, 0],
    data_reduced[:, 1],
    data_reduced[:, 2],
    c=np.arange(data.shape[0]),
    cmap='viridis',
    alpha=0.7
)
ax.set_title("3D t-SNE Projection for Market Anomalies")
ax.set_xlabel("Dimension 1")
ax.set_ylabel("Dimension 2")
ax.set_zlabel("Dimension 3")
plt.colorbar(scatter, label="Observation Index")
plt.show()