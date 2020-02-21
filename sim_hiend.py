import matplotlib.pyplot as plt
import numpy as np
import os

import sim_adwin as sim

# test_path  = "C:\\Users\\karnk\\git\\data_stream\\NKADA20140920_0230U"
test_path  = "C:\\Users\\karnk\\git\\data_stream\\1140_1200"

test_files = os.listdir(test_path)

test_files.sort()

stream_data = []
for test_file in test_files:
    dir = os.path.join(test_path, test_file)
    with open(dir) as txt_lines:
        for line in txt_lines:
            stream_data.append(int(line.replace('\n', '')))
plt.plot(stream_data)
plt.ylabel('value')
plt.xlabel('Time')
# plt.savefig("images/"+ file_name + ".png", aspect='auto', bbox_inches='tight', dpi=200)
# plt.show()
loop = int(len(stream_data)/20000)+1
start_point = 0
end_point = 0
change_points = []
for i in range(int(loop)):
    if(i == 0):
        start_point = 0
        end_point = 20000
    else:
        start_point = (i*20000)-1000
        if(i==loop-1):
            end_point = len(stream_data)
        else:
            end_point = (i*20000)+20000
    change_points.append(sim.test_sim(stream_data[start_point:end_point]))

# change_point = sim.test_sim(stream_data, zoom=False,range_zoom=1000)
print(change_point)