import math
import random

max_x = 200
max_y = 450
shape_options = 5
shape = random.randint(0, shape_options)
x = random.randint(0, max_x)
y = random.randint(0, max_y)
z = 0
send = True
while True:
    try:
        if send:
            f = open('input.txt', 'w')
            f.write('x' + str(x) + 'y' + str(y) + 'z' + str(z))
            print('x' + str(x) + 'y' + str(y) + 'z' + str(z))
            f.close()
            send = False
        else:
            g = open('request.txt', 'r+')
            r = str(g.read())
            g.close()
            open('request.txt', 'w').close()
            if r == 'request':
                x = random.randint(0, max_x)
                y = random.randint(0, max_y)
                z = random.randint(0, 1)
                send = True
    except KeyboardInterrupt:
        break

def square(x,y):
    size = random.randint(10,100)
    corner_bx = x + size
    corner_by = y + size
