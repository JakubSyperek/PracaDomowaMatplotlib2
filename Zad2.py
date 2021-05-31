import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


a = pd.Series(np.random.randn(100), index=pd.date_range('1/1/2015', periods=100))
a = a.cumsum()
a.plot()

b = pd.Series(np.random.randn(100), index=pd.date_range('1/1/2015', periods=100))
b = b.cumsum()
b.plot()

c = pd.Series(np.random.randn(100), index=pd.date_range('1/1/2015', periods=100))
c = c.cumsum()
c.plot()

d = pd.Series(np.random.randn(100), index=pd.date_range('1/1/2015', periods=100))
d = d.cumsum()
d.plot()

e = pd.Series(np.random.randn(100), index=pd.date_range('1/1/2015', periods=100))
e = e.cumsum()
e.plot()

plt.show()