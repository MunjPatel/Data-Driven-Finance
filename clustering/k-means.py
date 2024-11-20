from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# simulating synthetic stock return data
np.random.seed(42)
n_assets = 10
n_obs = 2000  
returns = np.random.multivariate_normal(
    mean=[0.02] * n_assets, 
    cov=np.cov(np.random.rand(n_assets, n_assets)), 
    size=n_obs
)
returns_df = pd.DataFrame(returns, columns=[f"Asset_{i+1}" for i in range(n_assets)])

# preparing data for clustering
raw_data = returns_df.stack().reset_index()
raw_data.columns = ['Observation', 'Asset', 'Return']

# encoding asset names into numeric values
raw_data['Asset'] = raw_data['Asset'].str.extract('(\d+)').astype(int)

# performing k-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
raw_data['Cluster'] = kmeans.fit_predict(raw_data[['Return']])

# clustering based on raw returns 3d plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(
    raw_data['Observation'],
    raw_data['Asset'],
    raw_data['Return'],
    c=raw_data['Cluster'],
    cmap='viridis',
    alpha=0.7
)
ax.set_title('3D K-Means Clustering for Portfolio Diversification')
ax.set_xlabel('Observation')
ax.set_ylabel('Asset')
ax.set_zlabel('Return')
plt.colorbar(scatter, label='Cluster')
plt.show()