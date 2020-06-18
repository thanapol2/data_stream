import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import os
import statistics

import sim_adwin as sim

# test_path  = "C:\\Users\\karnk\\git\\data_stream\\NKADA20140920_0230U"
test_path  = "C:\\Users\\karnk\\git\\data_stream\\1140_1200"
test_path  = "C:\\Users\\karnk\\git\\data_stream\\a"
# test_path  = "D:\\git_project\\data stream\\1151_1152"
# test_path  = "D:\\git_project\\data stream\\1140_1150"

test_files = os.listdir(test_path)
max_size = 400

test_files.sort()
list_point_end_file = []
labels = [label.replace('.txt', '') for label in test_files]
# labels = [label.replace('20140927', '') for label in labels]
labels = [label.replace('20140920', '') for label in labels]
stream_data = []
for test_file in test_files:
    dir = os.path.join(test_path, test_file)
    with open(dir) as txt_lines:
        list_point_end_file.append(len(stream_data))
        for line in txt_lines:
            stream_data.append(int(line.replace('\n', '')))
ax  = plt.subplot(111)
plt.plot(stream_data[30000:40000])
print(list_point_end_file)
# for i in range(len(list_point_end_file)):
#     plt.axvline(list_point_end_file[i], color='black', linestyle='-',linewidth=0.1)
#
# ax.set_xticks(list_point_end_file)
# ax.set_xticklabels(labels,rotation=60)
fig = plt.gcf()
fig.set_size_inches(15, 5.5)
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
    list_up_variance.append(mean+(variance*2))
    list_low_variance.append(mean+(variance*(-2)))

print(list_mean)
plt.plot(list_mean[30000:40000],color='green')
plt.plot(list_up_variance[30000:40000],color='red')
plt.plot(list_low_variance[30000:40000],color='red')
plt.show()
