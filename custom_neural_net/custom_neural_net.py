# Custom Neural Network - building neural network from scratch

import numpy as np


class NeuralNet:
    def __init__(self, x, y, weights1, bias1, weights2, bias2, weights3, bias3):
        # Inputs and Target Outputs
        self.inp = x
        self.y = y

        self.n = 100  # number of data points
        self.c = 3  # number of classes
        self.out = np.zeros(self.y.shape)  # predicted output
        self.lr = 0.05  # learning rate for model

        # Weights and Bias for Hidden Layers
        self.weights1 = weights1
        self.bias1 = bias1
        self.weights2 = weights2
        self.bias2 = bias2
        self.weights3 = weights3
        self.bias3 = bias3

    # Activation function used is sigmoid, other functions like ReLU, Leaky ReLU, Tanh can also be used
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_deriv(self, x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))

    def softmax(self, x):
        exp = np.exp(x)
        return exp/np.sum(exp, axis=1, keepdims=True)

    def feedforward(self):
        self.layer1 = self.sigmoid(np.dot(self.inp, self.weights1) + self.bias1)
        self.layer2 = self.sigmoid(np.dot(self.layer1, self.weights2) + self.bias2)
        self.out = np.dot(self.layer2, self.weights3) + self.bias3
        print(self.out)

    def mse(self):
        diff = self.out - self.y
        diff_sq = diff ** 2
        m_s_e = diff_sq.mean()
        return m_s_e

    def crossentropy_l2(self):
        correct_x = (self.y * np.log(self.softmax(self.out))) + (1-self.y) * (np.log(1 - self.softmax(self.out)))
        loss = -np.sum(correct_x)
        return loss


    def backprop(self):
        error = self.mse()
        print("self.out : ", self.out.shape, "\nself.layer2 : ", self.layer2.shape, "\nself.layer1 : ", self.layer1.shape, "\nself.weights3 : ", self.weights3.shape, "\nself.weights2 : ",
        self.weights2.shape, "\nself.weights1 : ", self.weights1.shape)

        scores = self.out
        prob = self.softmax(scores)



        d_weights3 = np.dot(self.layer2.T, np.dot(error, self.sigmoid_deriv(self.out)))
        d_bias3 = np.sum(np.dot(error, self.sigmoid_deriv(self.out)), axis=0, keepdims=True)
        d_weights2 = np.dot(self.layer1.T, np.dot(np.dot(error, self.sigmoid_deriv(self.out)), self.weights3.T))
        d_bias2 = np.sum(np.dot(np.dot(error, self.sigmoid_deriv(self.out)), self.weights3.T), axis=0, keepdims=True)
        d_weights1 = np.dot(self.inp.T, np.dot(np.dot(error, self.sigmoid_deriv(self.out)), self.weights2.T))
        d_bias1 = np.sum(np.dot(np.dot(error, self.sigmoid_deriv(self.out)), self.weights2.T), axis=0, keepdims=True)

        self.weights3 -= self.lr * d_weights3
        self.bias3 -= self.lr * d_bias3
        self.weights2 -= self.lr * d_weights2
        self.bias2 -= self.lr * d_bias2
        self.weights1 -= self.lr * d_weights1
        self.bias1 -= self.lr * d_bias1
