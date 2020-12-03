# 2-layer Fully-connected Custom Neural Network - building neural network from scratch

import numpy as np

class NeuralNet:
    def __init__(self, x, y, params):
        self.x = x  # input data
        self.y = y  # target output
        self.training_size = params['training_size']  # total number of data points

        self.out = np.zeros(self.y.shape)  # predicted output
        self.lr = params['lr']  # learning rate for model
        self.reg_strength = params['reg_strength']  # regularization strength
        self.activation = self.ReLU  # Activation used is ReLU, can also use Leaky ReLU, Sigmoid, Tanh

        # Weights and Biases for Hidden Layers
        # Layer 1
        self.weights1 = params['weights1']
        self.bias1 = params['bias1']
        # Layer 2
        self.weights2 = params['weights2']
        self.bias2 = params['bias2']
        # Output
        self.weights3 = params['weights3']
        self.bias3 = params['bias3']

    # Activation Functions
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def ReLU(self, x):
        return np.maximum(0, x)

    def softmax(self, x):
        exp = np.exp(x)
        return exp / np.sum(exp, axis=1, keepdims=True)

    # Feed-forward Computation
    def feedforward(self):
        self.layer1 = self.activation(np.dot(self.x, self.weights1) + self.bias1)
        self.layer2 = self.activation(np.dot(self.layer1, self.weights2) + self.bias2)
        self.out = np.dot(self.layer2, self.weights3) + self.bias3

    # Calculating Probabilities of Each Predicted Output and Backpropagation of Weights and Biases
    def backprop(self):
        self.prob = self.softmax(self.out)
        d_out = self.prob.copy()
        d_out[range(self.training_size), self.y] -= 1
        d_out /= self.training_size

        dW3 = np.dot(self.layer2.T, d_out)
        dB3 = np.sum(d_out, axis=0, keepdims=True)
        dhidden2 = np.dot(d_out, self.weights3.T)
        dhidden2[self.layer2 <= 0] = 0

        dW2 = np.dot(self.layer1.T, dhidden2)
        dB2 = np.sum(dhidden2, axis=0, keepdims=True)
        dhidden1 = np.dot(dhidden2, self.weights2.T)
        dhidden1[self.layer1 <= 0] = 0

        dW1 = np.dot(self.x.T, dhidden1)
        dB1 = np.sum(dhidden1, axis=0, keepdims=True)

        # Updating Weights and Biases
        self.weights3 -= self.lr * dW3
        self.weights2 -= self.lr * dW2
        self.weights1 -= self.lr * dW1
        self.bias3 -= self.lr * dB3
        self.bias2 -= self.lr * dB2
        self.bias1 -= self.lr * dB1

    # Calculating Loss - Cross Entropy + L2 Regularization
    def loss(self):
        correct_prob = self.y * np.log(self.prob[range(self.training_size), self.y])
        loss = -np.sum(correct_prob) / self.training_size
        regularization = 0.5 * self.reg_strength * ((np.sum(self.weights1 * self.weights1) + np.sum(self.weights2 * self.weights2) + np.sum(self.weights3 * self.weights3)) / self.training_size)
        total_loss = loss + regularization
        return total_loss
