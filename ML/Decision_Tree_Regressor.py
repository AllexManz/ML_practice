from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeRegressor
import numpy as np


def f(x):
    x = x.ravel()
    return np.exp(-x ** 2) + 1.5 * np.exp(-(x - 2) ** 2)


def generate(n_samples, nse):
    x = np.random.rand(n_samples) * 10 - 5
    x = np.sort(x).ravel()
    y = np.exp(-x ** 2) + 1.5 * np.exp(-(x - 2) ** 2) + np.random.normal(0.0, nse, n_samples)
    x = x.reshape((n_samples, 1))
    return x, y


n_train, n_test, noise = 150, 1000, 0.1
x_train, y_train = generate(n_samples=n_train, nse=noise)
x_test, y_test = generate(n_samples=n_test, nse=noise)

reg_tree = DecisionTreeRegressor(max_depth=5, random_state=17)
reg_tree.fit(x_train, y_train)
reg_tree_predicted = reg_tree.predict(x_test)

plt.figure(figsize=(10, 6))
plt.plot(x_test, f(x_test), "blue")
plt.scatter(x_train, y_train, c="red", s=20)
plt.plot(x_test, reg_tree_predicted, "green", lw=2)
plt.xlim([-5, 5])
plt.title("Decision Tree Regressor, MSE = %.2f" % np.sum((y_test - reg_tree_predicted) ** 2))
plt.show()
