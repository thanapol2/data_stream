 # Imports
import numpy as np
import matplotlib.pyplot as plt
from skmultiflow.drift_detection.adwin import ADWIN
adwin = ADWIN()
adwin.mint_min_window_length = 250
# Simulating a data stream as a normal distribution of 1's and 0's
data_stream = np.random.randint(2, size=2000)

for i in range (0,5):
    for j in range((51)+(i*30), (80)+(i*30)):
        data_stream[j] = np.random.randint(i+2, high=i+4)

# for i in range(111, 140):
#     data_stream[i] = np.random.randint(4, high=8)
x = np.linspace(-np.pi, 20*np.pi,2000)
sinx = np.sin(x)
plt.plot(np.sin(x))
plt.show()

for i in range(2000):
    adwin.add_element(sinx[i])
    if adwin.detected_change():
        print('Change detected in data: ' + str(sinx[i]) + ' - at index: ' + str(i))