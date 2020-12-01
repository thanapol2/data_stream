import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import os
import statistics
# from chebyshev_SEA import chebyshev_SEA as chebyshev
from chebyshev_adwin import chebyshev_adwin as chebyshev
from skmultiflow.drift_detection.adwin import ADWIN

adwin = ADWIN()

# max_size = 1000
# min_size = 500
size = 100
pattern = "si"
w = 1
_path  = "D:\\git_project\\data stream\\dataset\\"
# test =  _path + "test\\hinet_test_si_w1_i100.txt"
test =  _path + "test\\poisson_test_si_w1_i100.txt"
# answer = _path + "answer\\hinet_ans_"+pattern+"_w"+str(w)+"_i"+str(size)+".txt"
answer = _path + "answer\\poisson_ans_"+pattern+"_w"+str(w)+"_i"+str(size)+".txt"
data_lists = []
answer_lists = []
# min_len = 0
# max_len = 1800000
min_len = 0
max_len = 40000

k = 3
# cheb = chebyshev(max_size = max_size, min_size = min_size, k=k)
cheb= chebyshev(max_window= size, k=k)

with open(test) as txt_lines:
    for line in txt_lines:
        data_lists.append(int(line.replace('\n', '')))

data_lists = data_lists[0:max_len]
ax  = plt.subplot(111)


with open(answer) as txt_lines:
    for line in txt_lines:
        answer_lists.append(int(line.replace('\n', ''))*size)

cheb_list = []
for i in range(len(data_lists)):
    cheb.add_element(data_lists[i])
    # adwin.add_element(data_lists[i])
    if cheb.detected_change():
    # if adwin.detected_change():
        cheb_list.append(i)

for i in answer_lists:
    if(i<=max_len) & (min_len<=i):
        xa = range(i,i+size)
        ya = [160]*size
        plt.fill_between(xa, ya,alpha=0.30,color='orange')

        # plt.axvline(i-min_len, color='red', linestyle='-',linewidth=0.5)

for i in cheb_list:
    if (i <= max_len) & (min_len <= i):
        plt.axvline(i - min_len, color='red', linestyle='-', linewidth=0.7)

window = []
list_mean = []
list_up_variance = []
list_low_variance = []
for data in data_lists:
    if len(window) >= size:
        window.pop(0)
    window.append(data)
    mean = sum(window)/len(window)
    list_mean.append(mean)
    # variance = sum((i - mean) ** 2 for i in window) / len(window)
    variance =  np.std(window)
    list_up_variance.append(mean+(variance*k))
    list_low_variance.append(mean+(variance*(-k)))




# plt.plot(data_lists[min_len:max_len])
plt.plot(data_lists)
fig = plt.gcf()
fig.set_size_inches(18, 3)
plt.ylabel('value')
plt.xlabel('Time')
fig.suptitle(pattern+" W = "+ str(w), fontsize=20)

plt.plot(list_mean,color='green',linewidth=1)
plt.plot(list_up_variance,color='red')
plt.plot(list_low_variance,color='red')
# fig.suptitle("Chev with max_size = "+str(max_size)+" min_size =  "+str(min_size), fontsize=20)
# fig.suptitle("Chev with max_size = 3000", fontsize=20)
plt.ylim(55, 155)
plt.xlim(0, 10000)
plt.show()