import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import os
import statistics
from chebyshev_adwin import chebyshev_adwin as chebyshev
from chebyshev_SEA import chebyshev_SEA as chebyshev
from hoeffding import hoeffding as hoeffding
import sim_adwin as sim

# test_path  = "C:\\Users\\karnk\\git\\data_stream\\NKADA20140920_0230U"
# test_path  = "C:\\Users\\karnk\\git\\data_stream\\1145_1245"
# test_path  = "C:\\Users\\karnk\\git\\data_stream\\a"
# test_path  = "D:\\git_project\\data stream\\1151_1152"


test_path  = "D:\\git_project\\data stream\\test"
k = 3
max_size = 1000
min_size = 400
# chebyshev = chebyshev(max_size = max_size, k=k)
chebyshev = chebyshev(min_size = min_size,max_size = max_size, k=k)

# hoeffding = hoeffding(n=max_size)
test_files = os.listdir(test_path)

# cut_start = 18000
# cut_end = 30000
cut_start = 36000
cut_end = 60000

test_files.sort()
list_point_end_file = []
labels = [label.replace('.txt', '') for label in test_files]
labels = [label.replace('20140927', '') for label in labels]
# labels = [label.replace('20140920', '') for label in labels]
stream_data = []
for test_file in test_files:
    dir = os.path.join(test_path, test_file)
    with open(dir) as txt_lines:
        list_point_end_file.append(len(stream_data))
        for line in txt_lines:
            stream_data.append(int(line.replace('\n', '')))
ax  = plt.subplot(111)
# plt.plot(stream_data)
plt.plot(stream_data[cut_start:cut_end])
print(list_point_end_file)
cut_lable = []
cut_list_point = []

###  change point
change_point = []
for i in range(len(stream_data)):
    chebyshev.add_element(stream_data[i])
    if chebyshev.detected_change():
        change_point.append(i)
print(change_point)
for i in change_point:
    if (i >= cut_start) & (i< cut_end):
        plt.axvline(i-cut_start, color='r', linestyle='--', linewidth=0.3)
###   change point

for i in range(len(list_point_end_file)):
    if(list_point_end_file[i]>=cut_start) & (list_point_end_file[i]<cut_end):
        plt.axvline(list_point_end_file[i]-cut_start, color='black', linestyle='-',linewidth=0.1)
        cut_lable.append(labels[i])
        cut_list_point.append(list_point_end_file[i]-cut_start)
        # print(labels[i])

# ax.set_xticks(list_point_end_file)
# ax.set_xticklabels(labels,rotation=60)
ax.set_xticks(cut_list_point)
ax.set_xticklabels(cut_lable,rotation=60)
fig = plt.gcf()
fig.set_size_inches(18, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
# plt.show()

window = []
list_mean = []
list_up_variance = []
list_low_variance = []
for data in stream_data:
    if len(window) >= max_size:
        window.pop(0)
    window.append(data)
    mean = sum(window)/len(window)
    list_mean.append(mean)
    # variance = sum((i - mean) ** 2 for i in window) / len(window)
    variance =  np.std(window)
    list_up_variance.append(mean+(variance*k))
    list_low_variance.append(mean+(variance*(-k)))


plt.plot(list_mean[cut_start:cut_end],color='green')
plt.plot(list_up_variance[cut_start:cut_end],color='red')
plt.plot(list_low_variance[cut_start:cut_end],color='red')
# # print(list_mean)
# # plt.plot(list_mean,color='green')
# # plt.plot(list_up_variance,color='red')
# # plt.plot(list_low_variance,color='red')
plt.show()
