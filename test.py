from create_pattern import create_pattern
import matplotlib.pyplot as plt

print('hello')
a = create_pattern()
plt.plot(a.sudden_gen())
plt.show(aspect='auto')
plt.plot(a.incremental())
plt.show(aspect='auto')