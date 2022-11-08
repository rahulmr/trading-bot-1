import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('tst.txt')
# data = [[1 3 4 5 2 5 1 2 3]
#         [1 3 5 1 1 5 2 5 4]]
# print(data)

fig, ax = plt.subplots()
data = ax.imshow(data, extent=[0, 300, 0, 300], cmap='Greys')
x = np.array(range(300))
ax.plot(x, x, ls='dotted', linewidth=2)
plt.show()