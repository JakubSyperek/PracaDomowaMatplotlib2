import matplotlib.pyplot as plt
import numpy as np

#cmaps['Sequential (2)'] = [
#            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
#            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
#            'hot', 'afmhot', 'gist_heat', 'copper']

x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)
s = np.sin(0.5*x)
t = np.sin(2*x)
u = np.cos(1/3*x)

plt.plot(x, y, color='red');
plt.plot(x, z, color='yellow');
plt.plot(x, s, color='green');
plt.plot(x, t, color='blue');
plt.plot(x, u, color='purple');
plt.show()