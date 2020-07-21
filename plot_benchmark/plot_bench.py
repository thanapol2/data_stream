import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import os
import statistics
# from chebyshev_SEA import chebyshev_SEA as chebyshev
from chebyshev_adwin import chebyshev_adwin as chebyshev
from skmultiflow.drift_detection.adwin import ADWIN

adwin = ADWIN()

max_size = 1000
min_size = 500
size = 100
pattern = "si"
w = 1
_path  = "D:\\git_project\\data stream\\dataset\\"
test =  _path + "test\\hinet_test_si_w1_i100.txt"
# test =  _path + "test\\poisson_test_si_w1_i100.txt"
answer = _path + "answer\\hinet_ans_"+pattern+"_w"+str(w)+"_i"+str(size)+".txt"
# answer = _path + "answer\\poisson_ans_"+pattern+"_w"+str(w)+"_i"+str(size)+".txt"
data_lists = []
answer_lists = []
# min_len = 0
# max_len = 1800000
min_len = 1270000
max_len = 1290000

k = 3
# cheb = chebyshev(max_size = max_size, min_size = min_size, k=k)
cheb= chebyshev(max_size = 3000, k=k)

with open(test) as txt_lines:
    for line in txt_lines:
        data_lists.append(int(line.replace('\n', '')))

ax  = plt.subplot(111)


with open(answer) as txt_lines:
    for line in txt_lines:
        answer_lists.append(int(line.replace('\n', ''))*size)

# for i in range(len(data_lists)):
#     cheb.add_element(data_lists[i])
#     # adwin.add_element(data_lists[i])
#     if cheb.detected_change():
#     # if adwin.detected_change():
#         answer_lists.append(i)

for i in answer_lists:
    if(i<=max_len) & (min_len<=i):
        plt.axvline(i-min_len, color='red', linestyle='-',linewidth=0.5)



plt.plot(data_lists[min_len:max_len])
fig = plt.gcf()
fig.set_size_inches(18, 3)
plt.ylabel('value')
plt.xlabel('Time')
fig.suptitle(pattern+" W = "+ str(w), fontsize=20)
# fig.suptitle("Chev with max_size = "+str(max_size)+" min_size =  "+str(min_size), fontsize=20)
# fig.suptitle("Chev with max_size = 3000", fontsize=20)
plt.show()