import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(
    optimizer='rmsprop',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
(train_images, train_lab), (test_images, test_lab) = \
    tf.keras.datasets.mnist.load_data()
train_images = train_images.reshape((60000, 28*28))
test_images = test_images.reshape((10000, 28*28))
train_images = train_images.astype("float32") / 255
test_images = test_images.astype("float32") / 255
model.fit(train_images, train_lab, epochs=5, batch_size=128)