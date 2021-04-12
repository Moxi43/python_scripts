import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


#Define my data
x = np.array([
    [-2, 4, -1],
    [4, 1, -1],
    [1, 6, -1],
    [2, 4, -1],
    [6, 2, -1],
])

y = np.array([-1, -1, 1, 1, 1])

for d, sample in enumerate(x):
    #plot the negative samples
    if d < 0:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidth=2)
    #plot the positive samples
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidth=2)
plt.plot([-2, 6], [6, 0.5])
