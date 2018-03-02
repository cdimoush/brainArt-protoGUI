import math
import numpy as np
import random
import os
from functions.square import square

save_path = os.path.dirname(os.path.abspath(__file__)) + '/data'
print(save_path)

canvas = 800, 600
#data = np.load('data/brain_data.npy')
#length = len(data)
output = np.array([0, 0, 0])
x = 0
y = 0



def square_art(x, y, n, z):
    out = np.array([0, 0, 0])
    for i in range(0, n):
        x, y, step = square(x, y, z)
        z += 5
        x += 2.5
        y += 2.5

        out = np.vstack((out, step))
    return out


'''x, y, step = square(350, 250, 50)
output = np.vstack((output, step))
x, y, step = square(325, 225, 100)
output = np.vstack((output, step))
x, y, step = square(300, 200, 150)
output = np.vstack((output, step))
print(output)'''

out = square_art(200, 200, 15, 20)
output = np.vstack((output, out))



np.save(os.path.join(save_path , 'art_array.npy'), output)
