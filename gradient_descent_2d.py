import numpy as np
import matplotlib.pyplot as plt

def y_function(x):
    return x ** 2

def y_derivative(x):
    return 2 * x

def init():
    global current_pos
    global x
    global y
    x = np.arange(-100, 100, 0.1)
    y = y_function(x)
    current_pos = (80, y_function(80))

learning_rate = 0.05
init()
while True:
    new_x = current_pos[0] - learning_rate * y_derivative(current_pos[0])
    new_y = y_function(new_x)
    current_pos = (new_x, new_y)

    plt.plot(x, y)
    plt.scatter(current_pos[0], current_pos[1], color="red")
    plt.pause(0.01)
    plt.clf()

    if abs(y_derivative(current_pos[0])) < 0.01:
        init()