# Imports
from skmultiflow.data.sine_generator import SineGenerator
import matplotlib.pyplot as plt
from chebyshev_adwin import chebyshev_adwin as chebyshev

import sim_adwin as sim


import numpy as np
# from skmultiflow.drift_detection.adwin import ADWIN
# adwin = ADWIN()

from skmultiflow.drift_detection.eddm import EDDM
eddm = EDDM()

# Setting up the stream
# from skmultiflow.data.sine_generator import SineGenerator
# stream = SineGenerator(classification_function = 0, random_state = 112,
#                        balance_classes = False, has_noise = False)

# from skmultiflow.data.led_generator_drift import LEDGeneratorDrift
# stream = LEDGeneratorDrift(random_state = 112, noise_percentage = 0.28,has_noise= True,n_drift_features=4)

# from skmultiflow.data import ConceptDriftStream
# stream = ConceptDriftStream(random_state=123456, position=25000)

from skmultiflow.data.mixed_generator import MIXEDGenerator
stream = MIXEDGenerator(classification_function = 1, random_state= 112, balance_classes = False)

# Retrieving one sample
# stream.generate_drift()
data = stream.next_sample(1000)
list_data = []
change_point = []
print(data[0].size)
j = 0
for i in range(data[0].size):
    list_data.append(data[0].item(i))
    # eddm.add_element(data[0].item(i))
    # if eddm.detected_change():
    #     change_point.append(j)
    # j = j + 1
# for i in change_point:
#     plt.axvline(i, color='black', linestyle='-',linewidth=0.1)
plt.plot(list_data[0:2000])

# k = 3
# max_size = 400
# # chebyshev = chebyshev(max_size = max_size, k=k)
# cheb400 = chebyshev(max_size = 30, k=k)
# cheb1000 = chebyshev(max_size = 80, k=k)
#
# change_point400 = []
# change_point1000 = []
# change_point_in = []
# ###  change point400
#
# for i in range(len(list_data)):
#     cheb400.add_element(list_data[i])
#     if cheb400.detected_change():
#         change_point400.append(i)
#
# ###  change point1000
# for i in range(len(list_data)):
#     cheb1000.add_element(list_data[i])
#     if cheb1000.detected_change():
#         change_point1000.append(i)
# ###   change point
#
# for i in change_point400:
#     if i in change_point1000:
#         change_point_in.append(i)
#
# for i in change_point_in:
#     plt.axvline(i, color='black', linestyle='-',linewidth=0.1)

fig= plt.gcf()
fig.set_size_inches(20, 5.5)
plt.ylabel('value')
plt.xlabel('Time')

window = []
list_mean = []
list_up_variance3 = []
list_low_variance3 = []
list_up_variance2 = []
list_low_variance2 = []
for data in list_data:
    if len(window) >= 20:
        window.pop(0)
    window.append(data)
    mean = sum(window)/len(window)
    list_mean.append(mean)
    # variance = sum((i - mean) ** 2 for i in window) / len(window)
    variance =  np.std(window)
    list_up_variance3.append(mean+(variance*3))
    list_low_variance3.append(mean+(variance*(-3)))
    list_up_variance2.append(mean + (variance * 2))
    list_low_variance2.append(mean + (variance * (-2)))


plt.plot(list_up_variance2[0:2000],color='green')
plt.plot(list_low_variance2[0:2000],color='green')
plt.plot(list_up_variance3[0:2000],color='red')
plt.plot(list_low_variance3[0:2000],color='red')
plt.show()

plt.plot(list_data[0:400])
fig= plt.gcf()
fig.set_size_inches(20, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
plt.plot(list_up_variance2[0:400],color='green')
plt.plot(list_low_variance2[0:400],color='green')
plt.plot(list_up_variance3[0:400],color='red')
plt.plot(list_low_variance3[0:400],color='red')
plt.show()