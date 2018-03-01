import math
import numpy as np
import random

canvas = 800, 600
data = np.load('brain_data.npy')
length = len(data)
output = np.array([0, 0, 0])
x = 0
y = 0


def square1(x, y, d):
    size = 5 * math.fabs(d) + 5
    out = np.array([0, 0, 0])
    for i in range(0, 4):
        if i == 0:
            sx = x + size
            sy = y
        elif i == 1:
            sx = x + size
            sy = y + size
        elif i == 2:
            sx = x
            sy = y + size
        else:
            sx = x
            sy = y
        out = np.vstack((out, np.array([sx, sy, 1])))

    x += size
    out = np.delete(out, 0, 0)
    #print(x, y)
    return x, y, out

def square2(x, y, d):
    pass


for i in range(0, length):
    if data[i] < 1:
        x, y, step = square1(x, y, data[i])
        output = np.vstack((output, step))
        output = np.vstack((output, np.array([x, y, 0])))
    #else:
    #    x, y, step = square2(x, y, data[i])


#output = output.astype(int)
print(output)
np.save('square_matrix.npy', output)
