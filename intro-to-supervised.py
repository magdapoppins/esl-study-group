import random
import matplotlib.pyplot as plt
import math

# Generate a set of 2-dimensional data with 2 classes that have their own Gaussian distribution (mean and variance)

input_1_x = [random.gauss(0, 1) for x in range(100)]
input_1_y = [random.gauss(3, 6) for x in range(100)]

input_2_x = [random.gauss(10, 2) for x in range(100)]
input_2_y = [random.gauss(-2, 3) for x in range(100)]
"""
plt.figure(figsize=(3, 3))
plt.scatter(input_1_x, input_1_y, color='pink')
plt.scatter(input_2_x, input_2_y, color='green')
plt.show()
"""

inputs = [[x, y] for x, y in zip(input_1_x + input_2_x, input_1_y + input_2_y)]
outputs = [1 if x > 100 else 0 for x in range(200)]
"""
plt.figure(figsize=(3, 3))
plt.scatter(*zip(*inputs))
plt.show()
"""

i = [0, 3]


def get_class_NN(features, outputs, new_input, K):
    distances_to_i = [
        (e, math.sqrt((new_input[0] - x)**2 + (new_input[1] - y)**2))
        for e, (x, y) in enumerate(features)
    ]

    distances = sorted(distances_to_i, key=lambda l: l[1])
    K_nearest = distances[:K]
    return 1 if sum([outputs[o[0]] for o in K_nearest]) / K > 0.5 else 0


print("The class of i is", get_class_NN(inputs, outputs, i, 3))