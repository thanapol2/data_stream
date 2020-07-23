import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import os
import statistics
# from chebyshev_SEA import chebyshev_SEA as chebyshev
from chebyshev_adwin import chebyshev_adwin as chebyshev
from skmultiflow.drift_detection.adwin import ADWIN

fig, axs = plt.subplots(2)
fig = plt.gcf()
fig.set_size_inches(18, 6)

_len = 100
pattern = "si"
_width = 1
_path  = "D:\\git_project\\data stream\\dataset\\"
raw = _path+"training\\poisson_train.txt"
test =  _path + "test\\poisson_test_"+pattern+"_w"+str(_width)+"_i"+str(_len)+".txt"
answer = _path + "answer\\poisson_ans_"+pattern+"_w"+str(_width)+"_i"+str(_len)+".txt"

# test =  _path + "test\\hinet_test_si_w1_i100.txt"
# answer = _path + "answer\\hinet_ans_"+pattern+"_w"+str(w)+"_i"+str(size)+".txt"

raw_list = []
test_list = []
answer_lists = []
min_len = 0
max_len = 10000
windows_size = 1000
k = 3
cheb_raw= chebyshev(max_size = windows_size, k=k)
cheb_test= chebyshev(max_size = windows_size, k=k)
cheb_raw_list = []
cheb_test_list = []


with open(raw) as txt_lines:
    for line in txt_lines:
        raw_list.append(int(line.replace('\n', '')))

with open(test) as txt_lines:
    for line in txt_lines:
        test_list.append(int(line.replace('\n', '')))

with open(answer) as txt_lines:
    for line in txt_lines:
        answer_lists.append(int(line.replace('\n', ''))*_len)

for i in answer_lists:
    if(i<=max_len) & (min_len<=i):
        xa = range(i,i+_len)
        ya = [160]*_len
        plt.fill_between(xa, ya,alpha=0.30,color='orange')

data_lists = test_list[0:max_len]
for i in range(len(data_lists)):
    cheb_test.add_element(data_lists[i])
    # adwin.add_element(data_lists[i])
    if cheb_test.detected_change():
    # if adwin.detected_change():
        cheb_test_list.append(i)

data_lists = raw_list[0:max_len]
for i in range(len(data_lists)):
    cheb_raw.add_element(data_lists[i])
    # adwin.add_element(data_lists[i])
    if cheb_raw.detected_change():
    # if adwin.detected_change():
        cheb_raw_list.append(i)

axs[0].plot(raw_list)
axs[0].set_ylim(55, 155)
axs[0].set_xlim(0, max_len)
axs[1].plot(test_list)
# axs[1].ylabel('value')
# axs[1].xlabel('Time')
fig.suptitle(pattern+" Width = "+ str(_width)+" Length ", fontsize=20)
# fig.suptitle("Chev with max_size = "+str(max_size)+" min_size =  "+str(min_size), fontsize=20)
# fig.suptitle("Chev with max_size = 3000", fontsize=20)

# plt.plot(list_mean,color='green',linewidth=1)
# plt.plot(list_up_variance,color='red')
# plt.plot(list_low_variance,color='red')
for i in cheb_raw_list:
    if (i <= max_len) & (min_len <= i):
        axs[0].axvline(i - min_len, color='red', linestyle='-', linewidth=0.7)
for i in cheb_test_list:
    if (i <= max_len) & (min_len <= i):
        axs[1].axvline(i - min_len, color='red', linestyle='-', linewidth=0.7)

axs[1].set_ylim(55, 155)
axs[1].set_xlim(0, max_len)
plt.show()