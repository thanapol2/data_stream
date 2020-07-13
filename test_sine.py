# Imports
from skmultiflow.data.sine_generator import SineGenerator
import matplotlib.pyplot as plt
from skmultiflow.data import ConceptDriftStream

import numpy as np
# Setting up the stream
# stream = SineGenerator(classification_function = 2, random_state = 112,
#                        balance_classes = False, has_noise = False)
stream = ConceptDriftStream(random_state=123456, position=25000)
# Retrieving one sample
# stream.generate_drift()
a = stream.next_sample(100)
b = []
for i in range(a[0].size):
    b.append(a[0].item(i))

plt.plot(b)
# fig= plt.gcf()
# fig.set_size_inches(20, 5.5)
# plt.ylabel('value')
# plt.xlabel('Time')
# plt.show()

# b=[]
# for i in range(a[1].size):
#     b.append(a[1].item(i))
#
# plt.plot(b,color='r', linestyle='--',linewidth=0.3)
fig= plt.gcf()
fig.set_size_inches(20, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
plt.show()