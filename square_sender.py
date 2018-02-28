import math
import random
from time import sleep

x = 5
y = 5

sq_xy = []  # of the format x1, y1, x2, y2
bound_list = []
index = 0
s_index = 0
send = False

b_data = []

# This for loop generates binary brain data
# NOTE: squares will not be randomly placed, randint is only used to create the b_data
for i in range(0, 10):
    b_data.append(random.randint(0, 1))


def create_square(x1, y1, b):
    if b == 1:
        size = 10
    else:
        size = 20

    x2 = x1 + size
    y2 = y1 + size

    square = [x1, y1, x2, y2]
    return square


def send_fun(x, y, z): # The send function
    f = open('input.txt', 'w')
    print('Sending Coordinates ---> ' + 'x' + str(x) + 'y' + str(y) + 'z' + str(z))
    ans = input('check')
    f.write('x' + str(x) + 'y' + str(y) + 'z' + str(z))
    f.close()


def request_fun():  # The request function, checks if main.py needs coordinates
    g = open('request.txt', 'r+')
    r = str(g.read())
    g.close()
    open('request.txt', 'w').close()
    if r == 'request':
        print('Coordinates Requested')
        return True
    else:
        return False


while index < len(b_data):
    try:
        while not send:  # waits for the main program to ask for coordinates, will send init coordinates after this loop
            try:
                send = request_fun()
            except KeyboardInterrupt:
                exit()
        sleep(1)
        send_fun(x, y, 0)
        send = False

        sq_xy = create_square(x, y, b_data[index])
        print(sq_xy)
        while s_index < 4:
            '''Coordinates to send for each s_index step
            #0: x2, y1 = sq_xy[2,1]
            #1: x2, y2 = [2,3]
            #2: x1, y2 = [0,3]
            #3: x1, y1 = [0,1]'''
            while not send:
                try:
                    send = request_fun()
                except KeyboardInterrupt:
                    exit()
            sleep(1)
            if s_index == 0:
                sx = 2
                sy = 1
            elif s_index == 1:
                sx = 2
                sy = 3
            elif s_index == 2:
                sx = 0
                sy = 3
            else:
                sx = 0
                sy = 1
            send_fun(sq_xy[sx], sq_xy[sy], 1)
            send = False
            s_index += 1

        x = sq_xy[2]
        y = sq_xy[3]
        index += 1
        s_index = 0
    except KeyboardInterrupt:
        break


