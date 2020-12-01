import numpy as np
from custom_neural_net import NeuralNet

n = 100  # number of data points
c = 3  # number of classes
d = 2  # dimensions
x = np.zeros((n*c, d))  # input data
y = np.zeros((n*c), dtype='uint8')  # target outputs
epochs = 25000  # number of epochs/iterations
training_size = x.shape[0]
lr = 10
reg_strength = 0.005

for i in range(c):
    xi = range(n*i, n*(i+1))
    r = np.linspace(0, 1, n)  # radius
    t = np.linspace(i*4, (i+1)*4, n) + np.random.random(n)*0.2  # theta
    x[xi] = np.c_[r*np.sin(t), r*np.cos(t)]
    y[xi] = i

# Random Weights and Bias for Hidden Layers
weights1 = np.random.randn(d, n) * 0.01
bias1 = np.zeros((1, n))
weights2 = np.random.randn(n, n) * 0.01
bias2 = np.zeros((1, n))
weights3 = np.random.randn(n, c) * 0.01
bias3 = np.zeros((1, c))

net = NeuralNet(x, y, weights1, bias1, weights2, bias2, weights3, bias3)

for i in range(epochs):
    net.feedforward()
    net.backprop()
    if i % 1000 == 0:
        print("[Epoch %d] Loss : %f" % (i, net.loss()))

net.feedforward()
pred = np.argmax(net.out, axis=1)
print("Accuracy : %f" % (np.mean(pred == y)))
