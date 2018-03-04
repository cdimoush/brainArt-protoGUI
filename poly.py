import numpy as np
import math as m

def poly(x, y, r, n, s): 
    # n- number of sides 
    # r- shape radius from origin to verticies
    # s- start fraction (defult = -0.25)
    out = np.array([x, y, 0])
    n = 1/n             # set step size
    th = np.arange(s, 1+s+n, n)
    th = th * 2 * m.pi  # covert to rads

    for i in range(0, len(th)):    
        sx = x + r*m.cos(th[i])
        sy = y + r*m.sin(th[i])
        out = np.vstack((out, np.array([sx, sy, 1])))
    
    print('polygon with ' + str(1/n) + ' sides')
    return x, y, out