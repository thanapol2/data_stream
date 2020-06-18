# Imports
import numpy as np
import sim_adwin as sim
from skmultiflow.drift_detection import ADWIN, EDDM,DDM
import matplotlib.pyplot as plt

ddm = DDM()
adwin = ADWIN()
eddm =EDDM()
# Simulating a data stream as a normal distribution of 1's and 0's
data_stream = np.random.randint(2, size=200)
# Changing the data concept from index 999 to 1500, simulating an
# increase in error rate
for i in range(100, 150):
     data_stream[i] = np.random.randint(4, high=8)
# Adding stream elements to DDM and verifying if drift occurred
plt.plot(data_stream)
fig= plt.gcf()
fig.set_size_inches(10, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
for i in range(200):
    ddm.add_element(data_stream[i])
    if ddm.detected_warning_zone():
        plt.axvline(i, color='g', linestyle='--', linewidth=0.7)
        # print('Warning zone has been detected in data: ' + str(data_stream[i]) + ' - of index: ' + str(i))
    if ddm.detected_change():
        plt.axvline(i, color='r', linestyle='--', linewidth=0.7)
        # print('Change has been detected in data: ' + str(data_stream[i]) + ' - of index: ' + str(i))
plt.show()

plt.plot(data_stream)
fig= plt.gcf()
fig.set_size_inches(10, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
for i in range(200):
    eddm.add_element(data_stream[i])
    if eddm.detected_warning_zone():
        plt.axvline(i, color='g', linestyle='--', linewidth=0.7)
        # print('Warning zone has been detected in data: ' + str(data_stream[i]) + ' - of index: ' + str(i))
    if eddm.detected_change():
        plt.axvline(i, color='r', linestyle='--', linewidth=0.7)
        # print('Change has been detected in data: ' + str(data_stream[i]) + ' - of index: ' + str(i))
plt.show()


plt.plot(data_stream)
fig= plt.gcf()
fig.set_size_inches(10, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
for i in range(200):
    adwin.add_element(data_stream[i])
    if adwin.detected_change():
        plt.axvline(i, color='r', linestyle='--', linewidth=0.7)
        # print('Change has been detected in data: ' + str(data_stream[i]) + ' - of index: ' + str(i))
plt.show()