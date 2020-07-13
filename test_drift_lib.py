# Imports
from skmultiflow.data.sine_generator import SineGenerator
import matplotlib.pyplot as plt
from skmultiflow.data import ConceptDriftStream
import sim_adwin as sim

import numpy as np
# from skmultiflow.drift_detection.adwin import ADWIN
# adwin = ADWIN()

from skmultiflow.drift_detection.eddm import EDDM
eddm = EDDM()

# Setting up the stream
stream = SineGenerator(classification_function = 0, random_state = 112,
                       balance_classes = True, has_noise = True)
# stream = ConceptDriftStream(random_state=123456, position=25000)
# Retrieving one sample
stream.generate_drift()
data = stream.next_sample(2000)
list_data = []
change_point = []
print(data[0].size)
j = 0
for i in range(data[0].size):
    list_data.append(data[0].item(i))
    eddm.add_element(data[0].item(i))
    if eddm.detected_change():
        change_point(j)
    j = j + 1
plt.plot(list_data)


for i in change_point:
    plt.axvline(i, color='black', linestyle='-',linewidth=0.1)
fig= plt.gcf()
fig.set_size_inches(20, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
plt.show()