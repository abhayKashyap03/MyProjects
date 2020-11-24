import os, cv2, time, random, argparse
import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
try :
    tf.config.experimental.set_memory_growth(gpus[0], True)
    print(gpus[0])
except :
    print("No GPUs")

import numpy as np
from glob import glob


parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['image', 'folder'], type=str, required=True, help="Type of input - image or folder of images")
parser.add_argument('--path', type=str, required=True, help="Path (Location) where image or folder of images is stored")
parser.add_argument('--model_path', type=str, default='/home/abhaykashyap03/Desktop/comp_project/model.h5')
args = parser.parse_args()

start = time.time()


images = []
if args.type == 'image':
    images.append(cv2.resize(cv2.imread(args.path), (224, 224)))
elif args.type == 'folder':
    start_ = time.time()
    files = glob(os.path.join(args.path, '*'))
    random.shuffle(files)
    print("\n\nNumber of Images :", len(files))
    print("\nLoading Images ...")
    for i, file in enumerate(files):
        if i % 100 == 0:
            print("Image", i, "loaded")
        images.append(cv2.resize(cv2.imread(file), (224, 224)))
    print("\nImages loaded in", round(time.time() - start_), "seconds")

images = np.array(images)
model = tf.keras.models.load_model(args.model_path)
print('\n', model.summary(), '\n')
print("\nPredicting Labels ...\n")
preds = np.argmax(model.predict(images), axis=1)

print("\n\n")
for i, pred in enumerate(preds):
    label = "PNEUMONIC" if pred == 1 else "NORMAL"
    if args.type == 'folder':
        print("Image", i, os.path.basename(files[i]), ":", label)
    elif args.type == 'image':
        print("Image", i, os.path.basename(args.path), ":", label)


print("\nTime Taken :", round(time.time() - start), "seconds")
