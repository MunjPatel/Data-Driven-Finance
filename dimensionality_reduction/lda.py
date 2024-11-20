from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# generating synthetic credit data
n_obs = 2000
X, y = make_classification(
    n_samples=n_obs,
    n_features=5,         
    n_informative=3,     
    n_classes=3,          
    n_clusters_per_class=2, 
    random_state=42
)

# applying LDA
lda = LDA(n_components=2) 
X_reduced = lda.fit_transform(X, y)

# 2d visualization
plt.figure(figsize=(10, 8))
scatter = plt.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    c=y,
    cmap='viridis',
    alpha=0.7
)
plt.title("2D LDA Projection for Credit Risk Categorization")
plt.xlabel("LD1")
plt.ylabel("LD2")
plt.colorbar(scatter, label="Credit Category")
plt.show()