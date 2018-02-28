from tkinter import *
import numpy as np

data = np.load('square_matrix.npy')
master = Tk()

w = Canvas(master, width=800, height=600)
w.pack()

x = data[0, 0]
y = data[0, 1]
for i in range(1, data.shape[0]):
    if data[i, 2] == 1:
        w.create_line(x, y, data[i, 0], data[i, 1])
    x = data[i, 0]
    y = data[i, 1]

mainloop()