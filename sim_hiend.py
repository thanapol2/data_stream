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
for i in range(len(list_point_end_file)):
    plt.axvline(list_point_end_file[i], color='black', linestyle='-',linewidth=0.1)

ax.set_xticks(list_point_end_file)
ax.set_xticklabels(labels,rotation=60)
plt.ylabel('value')
plt.xlabel('Time')

plt.show()
window_size = 6000
loop = int(len(stream_data)/window_size)+1
print(loop)
start_point = 0
end_point = 0
print(len(stream_data))
change_points = []
for i in range(int(loop)):
    ax = plt.subplot(111)
    if(i == 0):
        start_point = 0
        end_point = window_size
        plt.axvline(list_point_end_file[i], color='black', linestyle='-', linewidth=1)
        plt.axvline(list_point_end_file[i+1], color='black', linestyle='-', linewidth=1)
        ax.set_xticks(list_point_end_file[i:i+2])
        ax.set_xticklabels(labels[i:i+2], rotation=60)
    else:
        crop_labels = []
        crop_point = []
        start_point = (i*window_size)-1000
        label_start_point = list_point_end_file[i]-(i*window_size)+1000
        plt.axvline(label_start_point, color='black', linestyle='-', linewidth=1)
        crop_labels.append(labels[i])
        crop_point.append(label_start_point)
        print(i)
        if(i==loop-1):
            end_point = len(stream_data)
            label_end_point = list_point_end_file[i] - (i * window_size) + 1000
            plt.axvline(len(stream_data), color='black', linestyle='-', linewidth=1)
        else:
            end_point = (i*window_size)+window_size
            # label_end_point = list_point_end_file[i+1] - (i*window_size) + 1000
            label_end_point = label_start_point+6000
            plt.axvline(label_end_point , color='black', linestyle='-', linewidth=1)
            crop_labels.append(str(int(labels[i])+1))
            crop_point.append(label_end_point)
        ax.set_xticks(crop_point)
        ax.set_xticklabels(crop_labels, rotation=60)
    change_point = sim.sim_adwin(stream_data[start_point:end_point])
    # print(change_point)
    plt.plot(stream_data[start_point:end_point])
    for j in change_point:
        plt.axvline(j, color='r', linestyle='--',linewidth=0.3)
    plt.ylabel('value')
    plt.xlabel('Time')
    fig = plt.gcf()
    fig.set_size_inches(15, 5.5)
    plt.ylim(-4000,4000)
    plt.savefig(os.path.join('hinet', labels[i] + "_input.png"), aspect='auto', bbox_inches='tight', dpi=200)
    plt.show()

# for change_point in change_points:
#
