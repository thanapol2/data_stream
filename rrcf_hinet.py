import os

import numpy as np
import pandas as pd
import rrcf
import matplotlib.pyplot as plt



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
# ax  = plt.subplot(111)
# plt.plot(stream_data)


# Set tree parameters
num_trees = 40
shingle_size = 4
tree_size = 256

# Create a forest of empty trees
forest = []
for _ in range(num_trees):
    tree = rrcf.RCTree()
    forest.append(tree)

# Use the "shingle" generator to create rolling window
points = rrcf.shingle(stream_data, size=shingle_size)

# Create a dict to store anomaly score of each point
avg_codisp = {}

# For each shingle...
for index, point in enumerate(points):
    # For each tree in the forest...
    for tree in forest:
        # If tree is above permitted size, drop the oldest point (FIFO)
        if len(tree.leaves) > tree_size:
            tree.forget_point(index - tree_size)
        # Insert the new point into the tree
        tree.insert_point(point, index=index)
        # Compute codisp on the new point and take the average among all trees
        if not index in avg_codisp:
            avg_codisp[index] = 0
        avg_codisp[index] += tree.codisp(index) / num_trees

list_point = []
for index, point in avg_codisp.items():
    list_point.append(point)

plt.plot(list_point)
plt.show()

plt.plot(stream_data)
plt.show()