import numpy as np
import math

def square(x, y, s):
    out = np.array([x, y, 0])
    for i in range(0, 4):
        if i == 0:
            sx = x + s
            sy = y
        elif i == 1:
            sx = x + s
            sy = y + s
        elif i == 2:
            sx = x
            sy = y + s
        else:
            sx = x
            sy = y
        out = np.vstack((out, np.array([sx, sy, 1])))

    #out = np.delete(out, 0, 0)
    #print(x, y)
    print('square')
    print(out)
    return x, y, out


def roto_square(x, y, s, a):  # This functions creates a square at an offset angle
	pass