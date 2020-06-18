import statistics

import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import os

import sim_adwin as sim

# test_path  = "C:\\Users\\karnk\\git\\data_stream\\NKADA20140920_0230U"
# test_path  = "C:\\Users\\karnk\\git\\data_stream\\1140_1200"
test_path  = "D:\\git_project\\data stream\\1151_1152"
# test_path  = "D:\\git_project\\data stream\\1140_1150"

test_files = os.listdir(test_path)

test_files.sort()
list_point_end_file = []
labels = [label.replace('.txt', '') for label in test_files]
labels = [label.replace('20140927', '') for label in labels]
stream_data = []
for test_file in test_files:
    dir = os.path.join(test_path, test_file)
    with open(dir) as txt_lines:
        list_point_end_file.append(len(stream_data))
        for line in txt_lines:
            stream_data.append(int(line.replace('\n', '')))
ax  = plt.subplot(111)
plt.plot(stream_data)
print(list_point_end_file)
# for i in range(len(list_point_end_file)):
#     plt.axvline(list_point_end_file[i], color='black', linestyle='-',linewidth=0.1)
#
# ax.set_xticks(list_point_end_file)
# ax.set_xticklabels(labels,rotation=60)
fig= plt.gcf()
fig.set_size_inches(10, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
plt.show()
# test
ax  = plt.subplot(111)
plt.plot(stream_data[4500:5000])
fig= plt.gcf()
fig.set_size_inches(10, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
plt.axhline(statistics.mean(stream_data[4700:4800]), color='r', linestyle='--',linewidth=2)
print(statistics.mean(stream_data[4700:4800]))
print(statistics.variance(stream_data[4700:4800]))
# change_point = sim.sim_adwin(stream_data[4500:5000])
detected_warning,change_point = sim.sim_ddm(stream_data[4500:5000])
print(change_point)
# crop_point = [0,50,100,150,200,250,300]
# crop_labels = [900,950,1000,1050,1100,1150,1200]
# ax.set_xticks(crop_point)
# ax.set_xticklabels(crop_labels)
# change_point_crop = []
for i in change_point:
    # if(i>=900)&(i<=1200):
    #     plt.axvline(i-900, color='r', linestyle='--',linewidth=0.3)
    plt.axvline(i, color='r', linestyle='--', linewidth=0.3)
plt.show()

plt.plot(stream_data[4500:5000])
fig= plt.gcf()
fig.set_size_inches(10, 5.5)
plt.ylabel('value')
plt.xlabel('Time')
for i in detected_warning:
    # if(i>=900)&(i<=1200):
    #     plt.axvline(i-900, color='r', linestyle='--',linewidth=0.3)
    plt.axvline(i, color='b', linestyle='--', linewidth=0.3)
plt.show()