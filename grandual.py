from create_pattern import pattern
import matplotlib.pyplot as plt
import numpy as np
import sim_adwin as sim


file_name = 'gradual_data'
pattern = pattern()
stream_data = pattern.gradual()
plt.plot(stream_data)
plt.show()
for i in range(len(stream_data)):
    stream_data[i] = stream_data[i] + np.random.random_sample()
plt.plot(stream_data)
plt.ylabel('value')
plt.xlabel('Time')
plt.savefig("image/"+file_name+"_input.png", aspect='auto', bbox_inches='tight', dpi=200)
plt.show()

xi = list(range(1900,2500))
plt.plot(xi, stream_data[1900:2500])
plt.ylabel('value')
plt.xlabel('Time')
plt.savefig("image/gradual_zoom.png", aspect='auto', bbox_inches='tight', dpi=200)
plt.show()
sim.test_sim(stream_data,file_name,zoom=True)