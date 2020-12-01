import numpy as np

class NeuralNet:
    def __init__(self, x, y, weights1, bias1, weights2, bias2, weights3, bias3):
        # Inputs and Target Outputs
        self.x = x
        self.y = y
        self.training_size = self.x.shape[0]

        self.n = 100  # number of data points
        self.c = 3  # number of classes
        self.out = np.zeros(self.y.shape)  # predicted output
        self.lr = 1  # learning rate for model
        self.reg_strength = 0.05
        self.activation = self.softmax

        # Weights and Bias for Hidden Layers
        self.weights1 = weights1
        self.bias1 = bias1
        self.weights2 = weights2
        self.bias2 = bias2
        self.weights3 = weights3
        self.bias3 = bias3

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def ReLU(self, x):
        return np.maximum(0, x)

    def softmax(self, x):
        exp = np.exp(x)
        return exp / np.sum(exp, axis=1, keepdims=True)

    def feedforward(self):
        self.layer1 = self.activation(np.dot(self.x, self.weights1) + self.bias1)
        self.layer2 = self.activation(np.dot(self.layer1, self.weights2) + self.bias2)
        self.out = np.dot(self.layer2, self.weights3) + self.bias3

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

        self.weights3 -= self.lr * dW3
        self.weights2 -= self.lr * dW2
        self.weights1 -= self.lr * dW1
        self.bias3 -= self.lr * dB3
        self.bias2 -= self.lr * dB2
        self.bias1 -= self.lr * dB1

    def loss(self):
        correct_prob = self.y * np.log(self.prob[range(self.training_size), self.y])
        loss = -np.sum(correct_prob) / self.training_size
        regularization = 0.5 * self.reg_strength * ((np.sum(self.weights1 * self.weights1) + np.sum(self.weights2 * self.weights2) + np.sum(self.weights3 * self.weights3)) / self.training_size)
        total_loss = loss + regularization
        return total_loss
