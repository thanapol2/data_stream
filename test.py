from create_pattern import pattern
import matplotlib.pyplot as plt
import numpy as np

a = pattern()
t = a.gradual()
plt.plot(t)
plt.show()
for i in range(len(t)):
    t[i] = t[i]+np.random.random_sample()
plt.plot(t)
plt.show()