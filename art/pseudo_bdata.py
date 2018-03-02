import numpy as np
import random

pseudo_data = []

for i in range(0, 100):
    x = random.randint(-2, 3)
    pseudo_data.append(x)

output = np.array(pseudo_data)
print(output)
np.save('data.brain_data.npy', output)
