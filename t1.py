# Imports
from skmultiflow.drift_detection import ADWIN, DDM

import sim_adwin as sim
import numpy as np
from skmultiflow.drift_detection.eddm import EDDM
import matplotlib.pyplot as plt

eddm = EDDM()
adwin = ADWIN()
ddm = DDM()
# Simulating a data stream as a normal distribution of 1's and 0's
data_stream = np.random.randint(3, size=200)
# Changing the data concept from index 999 to 1500, simulating an
# increase in error rate
for i in range(100, 150):
    data_stream[i] = 0
# Adding stream elements to EDDM and verifying if drift occurred
detected_warning1,change_point1 = sim.sim_ddm(data_stream)
change_point2 = sim.sim_adwin(data_stream)
# detected_warning3,change_point3 = sim.sim_eddm(data_stream)
# print(detected_warning)
# print(change_point)

for i in change_point1:
    # if(i>=900)&(i<=1200):
    #     plt.axvline(i-900, color='r', linestyle='--',linewidth=0.3)
    plt.axvline(i, color='r', linestyle='--', linewidth=1)

plt.plot(data_stream)
fig= plt.gcf()
fig.set_size_inches(10, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
for i in detected_warning1:
    # if(i>=900)&(i<=1200):
    #     plt.axvline(i-900, color='r', linestyle='--',linewidth=0.3)
    plt.axvline(i, color='g', linestyle='--', linewidth=1)
plt.show()

for i in change_point2:
    # if(i>=900)&(i<=1200):
    #     plt.axvline(i-900, color='r', linestyle='--',linewidth=0.3)
    plt.axvline(i, color='r', linestyle='--', linewidth=1)

plt.plot(data_stream)
fig= plt.gcf()
fig.set_size_inches(10, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
plt.show()

# for i in change_point3:
#     # if(i>=900)&(i<=1200):
#     #     plt.axvline(i-900, color='r', linestyle='--',linewidth=0.3)
#     plt.axvline(i, color='r', linestyle='--', linewidth=1)
#
# plt.plot(data_stream)
# fig= plt.gcf()
# fig.set_size_inches(10, 5.5)
# plt.ylabel('value')
# plt.xlabel('Time')
# for i in detected_warning3:
#     # if(i>=900)&(i<=1200):
#     #     plt.axvline(i-900, color='r', linestyle='--',linewidth=0.3)
#     plt.axvline(i, color='g', linestyle='--', linewidth=1)
# plt.show()