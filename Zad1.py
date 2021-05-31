import matplotlib.pyplot as plt
import numpy as np

z = np.arange(0,2*np.pi,0.1)
x = np.sin(z)
y = np.cos(2*z)

plt.plot(z,x,z,y)

plt.show()