from create_pattern import pattern
import matplotlib.pyplot as plt
import numpy as np
import sim_adwin as sim


input = ['S','I','R']
pattern = pattern()
for i in input:
    (stream_data,file_name) = pattern.create(i)
    # Add random value to pattern
    plt.plot(stream_data)
    plt.ylabel('value')
    plt.xlabel('Time')
    plt.savefig("images/"+ file_name + ".png", aspect='auto', bbox_inches='tight', dpi=200)
    plt.show()
    for j in range(len(stream_data)):
        stream_data[j] = stream_data[j] + np.random.random_sample()
    plt.plot(stream_data)
    plt.ylabel('value')
    plt.xlabel('Time')
    plt.savefig("images/"+file_name+"_input.png", aspect='auto', bbox_inches='tight', dpi=200)
    plt.show()
    sim.test_sim(stream_data,file_name=file_name, zoom=True,range_zoom=1000)
