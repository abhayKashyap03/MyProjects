import numpy as np
import tensorflow as tf
import os
import cv2
import random
import argparse
from tensorflow.keras import layers
from sklearn.metrics import multilabel_confusion_matrix, precision_score, accuracy_score, recall_score
from glob import glob
from ast import literal_eval
from time import time

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, required=True)
parser.add_argument('--save', type=literal_eval, choices=[True, False], required=True)
parser.add_argument('--save_as', type=str, required=False,
                    default='/home/abhay_kashyap03/Desktop/comp_project/model.h5')
parser.add_argument('--custom_testing', type=literal_eval, default=True)
parser.add_argument('--custom_data', type=str, required=False,
                    default='/home/abhay_kashyap03/Desktop/comp_project/xray_images/images')
args = parser.parse_args()

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Image Processing

start = time()

# Join normal and positive image names lists into one list containing all filenames, for training, testing and validation 
x_tr = glob(os.path.join(args.dataset, 'train/*/*'))
y_train = [1 if 'PNEUMONIA' in file else 0 for file in x_tr]
x_ts = glob(os.path.join(args.dataset, 'test/*/*'))
y_test = [1 if 'PNEUMONIA' in file else 0 for file in x_ts]
x_v = glob(os.path.join(args.dataset, 'val/*/*'))
y_val = [1 if 'PNEUMONIA' in file else 0 for file in x_v]

# Randomize filenames for better training
c_tr = list(zip(x_tr, y_train))
c_ts = list(zip(x_ts, y_test))
c_v = list(zip(x_v, y_val))
random.shuffle(c_tr)
random.shuffle(c_ts)
random.shuffle(c_v)
x_tr, y_train = zip(*c_tr)
x_ts, y_test = zip(*c_ts)
x_v, y_val = zip(*c_v)

# Load image file as numpy array and resize image into (224, 224, 3)
x_train, x_test, x_val = [], [], []
for i, file in enumerate(x_tr):
    if i % 150 == 0:
        print(i)
    x_train.append(cv2.resize(cv2.imread(file), (224, 224)))
for i, file in enumerate(x_ts):
    if i % 100 == 0:
        print(i)
    x_test.append(cv2.resize(cv2.imread(file), (224, 224)))
for i, file in enumerate(x_v):
    if i % 10 == 0:
        print(i)
    x_val.append(cv2.resize(cv2.imread(file), (224, 224)))
# Convert list into 4D array
x_train = np.asarray(x_train)
x_test = np.asarray(x_test)
x_val = np.asarray(x_val)

# Convert target lists into numpy array and categorize the labels into the arrays
y_train, y_test, y_val = np.asarray(y_train).reshape(-1, 1), np.asarray(y_test).reshape(-1, 1), np.asarray(
    y_val).reshape(-1, 1)
y_train, y_test, y_val = tf.keras.utils.to_categorical(y_train), tf.keras.utils.to_categorical(
    y_test), tf.keras.utils.to_categorical(y_val)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Model Creation, Training and Running Inference on Test Files

# Neural network creation
inp = layers.Input((224, 224, 3))
x = layers.Conv2D(128, (3, 3), activation='relu')(inp)
x = layers.MaxPooling2D(2, 2)(x)
x = layers.Dropout(0.5)(x)
x = layers.Conv2D(128, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(2, 2)(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(2, 2)(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(2, 2)(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(2, 2)(x)
x = layers.Dropout(0.5)(x)
x = layers.Flatten()(x)
x = layers.Dense(512, activation='relu')(x)
out = layers.Dense(2, activation='softmax')(x)
# Model creation and compiling
model = tf.keras.Model(inp, out)
model.compile(tf.keras.optimizers.RMSprop(), 'categorical_crossentropy', metrics=['accuracy'])
print(model.summary())
# Train neural network(model) on xray images to give proper inference (whether xray is pneumonic or normal)
train = model.fit(x_train, y_train, epochs=50, validation_data=(x_val, y_val))
# Save model
if args.save:
    model.save(args.save_as)
# Running inference on test images
pred = np.argmax(np.round(model.predict(x_test)), axis=1)
y_test = np.argmax(y_test, axis=1)

# Evaluation metrics
print(multilabel_confusion_matrix(y_test, pred))
print(precision_score(y_test, pred))
print(accuracy_score(y_test, pred))
print(recall_score(y_test, pred))

print("Training and Testing : ", round(time() - start), "seconds")
