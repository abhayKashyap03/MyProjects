import numpy as np
from custom_neural_net import NeuralNet
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--data_points', type=int, required=True)
parser.add_argument('--classes', type=int, required=True)
parser.add_argument('--dimensions', type=int, required=True)
parser.add_argument('--epochs', type=int, required=True)
parser.add_argument('--lr', type=float, required=True)
parser.add_argument('--reg_strength', type=float, required=True)
args = parser.parse_args()


# 1. Initialize Hyperparameters and Other Variables Required

n = args.data_points  # number of data points
c = args.classes  # number of classes
d = args.dimensions  # dimensions
x = np.zeros((n * c, d))  # input data
y = np.zeros((n * c), dtype='uint8')  # target outputs
epochs = args.epochs  # number of epochs/iterations
training_size = x.shape[0]
lr = args.lr  # learning rate
reg_strength = args.reg_strength  # regularization strength


# 2. Add Data to 'x' and 'y'

for i in range(c):
    xi = range(n * i, n * (i + 1))
    r = np.linspace(0, 1, n)  # radius
    t = np.linspace(i * 4, (i + 1) * 4, n) + np.random.random(n) * 0.2  # theta
    x[xi] = np.c_[r * np.sin(t), r * np.cos(t)]
    y[xi] = i


# 3. Initialize Random Weights and Biases for Hidden Layers

weights1 = np.random.randn(d, n) * 0.01
bias1 = np.zeros((1, n))
weights2 = np.random.randn(n, n) * 0.01
bias2 = np.zeros((1, n))
weights3 = np.random.randn(n, c) * 0.01
bias3 = np.zeros((1, c))


# Parameters for Neural Network
params = {'n': n, 'training_size': training_size, 'lr': lr, 'reg_strength': reg_strength, 'weights1': weights1, 'bias1': bias1, 'weights2': weights2, 'bias2': bias2, 'weights3': weights3,
          'bias3': bias3}


# Neural Network
net = NeuralNet(x, y, params)


# 4. Gradient Descent Loop - Training Loop

for i in range(epochs):
    # 4.a) Feed-forward Computation
    net.feedforward()
    # 4.b) Backpropagation
    net.backprop()
    # 4.c) Loss
    if i % 1000 == 0:
        print("[Epoch %d] Loss : %f" % (i, net.loss()))


# 5. Evaluation

net.feedforward()
pred = np.argmax(net.out, axis=1)
print("Accuracy : %.3f" % (np.mean(pred == y)))
