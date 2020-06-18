import numpy as np
from skmultiflow.drift_detection.adwin import ADWIN
from skmultiflow.drift_detection.eddm import EDDM
import matplotlib.pyplot as plt
import math
from random import gauss
adwin = ADWIN()
# eddm = EDDM()
 # Simulating a data stream as a normal distribution of 1's and 0's
my_mean = 10
my_variance = 0.1

data_stream = [gauss(my_mean, math.sqrt(my_variance)) for i in range(500)]

# data_stream = np.random.randint(10, size=100)
# data_stream = [1,0,1,0,1,0,1,1,0,1,1,1,1,1,1]
 # Changing the data concept from index 999 to 2000
# for i in range(50, 100):
#     data_stream[i] = np.random.randint(4, high=8)
 # Adding stream elements to ADWIN and verifying if drift occurred
print(np.mean(data_stream))
plt.plot(data_stream)
plt.show()

for i in range(len(data_stream)):
    adwin.add_element(data_stream[i])
    if adwin.detected_change():
        print('Change detected in data: ' + str(data_stream[i]) + ' - at index: ' + str(i))