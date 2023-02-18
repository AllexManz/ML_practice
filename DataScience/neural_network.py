import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return (1 / (1 + np.exp(-x)))


training_inputs = np.array([[0, 0, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])

training_outputs = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)
synaptic_weights = 2 * np.random.random((3, 1)) - 1

#Метод обратного распространения
x, y = [], []
for i in range(20000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    err = training_outputs - outputs
    x.append(i)
    y.append(sum(sum(err)))
    adjustment = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
    
    synaptic_weights += adjustment

plt.plot(x, y)
plt.title("Изменение ошибки")
plt.xlabel('Время')
plt.ylabel('Значение ошибки')
plt.show()

print("Результат:")
print(*outputs)







