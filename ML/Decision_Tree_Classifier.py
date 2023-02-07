import numpy as np
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import pydot


def get_grid(data):
    x_min, x_max = data[:, 0].min(),  data[:, 0].max()
    y_min, y_max = data[:, 1].min(), data[:, 1].max()
    return np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))


np.random.seed(1)

# First Class
train_data = np.random.normal(size=(100, 2))
train_labels = np.zeros(100)

# Second Class
train_data = np.r_[train_data, np.random.normal(size=(100, 2), loc=2)]
train_labels = np.r_[train_labels, np.ones(100)]

plt.rcParams['figure.figsize'] = (10, 8)
plt.scatter(train_data[:, 0], train_data[:, 1], c=train_labels, s=100,
            cmap='autumn', edgecolors='black', linewidths=1.5)
plt.plot(range(-2, 5), range(4, -3, -1))
plt.show()

clf_tree = DecisionTreeClassifier(criterion='entropy', max_depth=2, random_state=17)

# Training
clf_tree.fit(train_data, train_labels)
xx, yy = get_grid(train_data)
predicted = clf_tree.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.pcolormesh(xx, yy, predicted, cmap='autumn')
plt.scatter(train_data[:, 0], train_data[:, 1], c=train_labels, s=100,
            cmap='autumn', edgecolors='black', linewidths=1.5)
plt.show()

export_graphviz(clf_tree, feature_names=['x1', 'x2'], out_file="img/small_tree.dot", filled=True)
'''
# Visualisation via graph, currently not working

graphs = pydot.graph_from_dot_file('img/small_tree.dot')
graph = graphs[0]
graph.write('img/output.png', format='png')
'''
