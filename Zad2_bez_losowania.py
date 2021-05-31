import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)
s = np.sin(0.5*x)
t = np.sin(2*x)
u = np.cos(1/3*x)

plt.plot(x, y, 'o', color='red');
plt.plot(x, z, '^', color='yellow');
plt.plot(x, s, 'P', color='green');
plt.plot(x, t, 'D', color='blue');
plt.plot(x, u, '*', color='purple');
plt.show()