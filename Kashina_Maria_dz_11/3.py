import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5)
y = [1 / i for i in x]
plt.plot(x, y, color='orange', linewidth=7)
plt.grid()
plt.title('y =1/x')
plt.xlabel('Аргумент')
plt.ylabel('Значение')
plt.show()
