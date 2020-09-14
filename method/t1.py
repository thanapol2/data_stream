import numpy as np
import statistics
import queue
from skmultiflow.drift_detection.adwin import ADWIN
# Simulating a data stream as a normal distribution of 1's and 0's
np.random.seed(30)
data_stream = np.random.randint(3,  size=50)
# Changing the data concept from index 999 to 2000
for i in range(25, 50):
    data_stream[i] = np.random.randint(4, high=20)
# b = ['a','b','c']
w = []
count = 0
print(data_stream)
for instace in data_stream:
    print(count)
    w.append(instace)
    w1 = []
    w2 = w[:]
    end_loop = False
    cursor = 0
    print(w)
    while not end_loop:

        _max = max(w)
        _min = min(w)
        mean_w1 = 0
        mean_w2 = 0
        for i in w2:
            count = count + 1
            variance = np.std(w)
            w1.append(w2.pop(0))
            if len(w1)>0:
                mean_w1 = statistics.mean(w1)
            if len(w2)>0:
                mean_w2 = statistics.mean(w2)
            cal = abs(mean_w1-mean_w2)
            if cal > 2*variance:
                end_loop = True
                # update w
                w = w2[:]
                # break

            # = (*th^2)/(max-min)^2

            if len(w2) == 0:
                end_loop = True

            print("w1 = {} and w2 = {} mean_w1 = {} mean_w2 = {}".format(w1, w2, mean_w1, mean_w2))
        count = count +1
    print("****end loop**")