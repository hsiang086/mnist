from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np

def import_npy():
    global img
    img = np.load("img.npy")
    img = np.rot90(img, 3)
    img = np.flip(img, axis = 1)

import_npy()
print(np.max(img), img.min())

model = load_model('mnist.h5')
print(np.argmax(model(img[np.newaxis, ..., np.newaxis].astype(np.float32), training=False)))

fig, ax = plt.subplots(1, 1)
ax.imshow(img)
plt.show()
