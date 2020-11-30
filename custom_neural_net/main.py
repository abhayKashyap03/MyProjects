# Main file - run custom neural network from this file

import numpy as np
from custom_neural_net import *

n = 100  # number of data points
c = 3  # number of classes
d = 2  # dimensions
epochs = 1000  # number of epochs/iterations
x = np.zeros((n*c, d))  # input data
y = np.zeros((n*c), dtype='uint8')  # target outputs

for i in range(c):
    xi = range(n*i, n*(i+1))
    r = np.linspace(0, 1, n)
    t = np.linspace(i*4, (i+1)*4, n) + np.random.random(n)*0.2
    x[xi] = np.c_[r*np.sin(t), r*np.cos(t)]
    y[xi] = i
y = np.eye(c)[y]
print(y.shape)
# Random Weights and Bias for Hidden Layers
weights1 = np.random.random((x.shape[1], n))
bias1 = np.zeros((1, n))
weights2 = np.random.random((n, n))
bias2 = np.zeros((1, n))
weights3 = np.random.random((n, c))
bias3 = np.zeros((1, c))

net = NeuralNet(x, y, weights1, bias1, weights2, bias2, weights3, bias3)

for i in range(epochs):
    net.feedforward()
    print("[Epoch %d] Loss : %f" % ((i+1), net.crossentropy_l2()))
    net.backprop()
