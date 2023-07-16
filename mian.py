from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

def import_npy():
    global img
    img = np.load("img.npy")
    img = np.rot90(img, 3)
    img = np.flip(img, axis = 1)

import_npy()
print(np.max(img), img.min())

model = keras.models.load_model('mnist.keras')
print(np.argmax(model.predict(np.reshape(img, (1, 28*28)).astype('float32'))[0]))

plt.imshow(img, cmap = 'gray')
plt.show()
