import numpy as np
import math

def circle(x, y, r):  # (center x, center y, radius)
    out = np.array([x + r * math.cos(0), y + math.sin(0), 0])  # move carraige to circle perimeter
    # x = r * cos 
    # y = r * sin
    theta = np.arange(0, 1.01, .01)
    theta = theta * 2 * math.pi   # list of 100 term, 0 ----> 2pi
    
    for i in range(0, len(theta)):  # draw 100 small lines
        x1 =  x + r * math.cos(theta[i])
        y1 =  y + r * math.sin(theta[i])
        out = np.vstack((out, np.array([x1, y1, 1])))

    return x, y, out

