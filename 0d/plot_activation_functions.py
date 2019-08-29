####################
# plot graphs of step function and sigmoid and ReLU
####################

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
	return np.array(x > 0, dtype=np.int)

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def relu(x):
	return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
step = step_function(x)
plt.plot(x, step)

sig = sigmoid(x)
plt.plot(x, sig)

relu = relu(x)
plt.plot(x, relu)

plt.grid(True)
plt.ylim(-0.1, 5.0)
plt.show()
