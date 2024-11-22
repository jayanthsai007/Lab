'''Clustering'''
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plot
x, y = make_blobs(n_samples=15, n_features=2, centers=3,
                  cluster_std=0.5, random_state=0)
plot.scatter(x[:, 0], x[:, 1], c='green',
             marker='+', edgecolors='black', s=100)
plot.xlabel('feature 1')
plot.ylabel('feature 2')
plot.grid()
plot.show()
