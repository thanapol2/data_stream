from kalman_playground.kf_book import book_plots as book_plots
import kalman_playground.kf_book.kf_internal as kf_internal
from method.window_tech.sliding_win import sliding_win
import kalman_playground.kalman_method as kalman
import numpy as np
import matplotlib.pyplot as plt

measuerments = [49.95, 49.967, 50.1, 50.106, 49.992, 49.819, 49.933, 50.007]
x = 10
x_var = 10000
model_mean = 0
model_var = 0.01

xs = np.zeros((len(measuerments), 2))
ps = np.zeros((len(measuerments), 2))

for i, measurement in enumerate(measuerments):
    x,x_var = kalman.update(x,x_var,measurement,model_var)
    xs[i] = x, x_var
    x,x_var = kalman.predict(x,x_var,model_mean,model_var)

    ps[i] = x,x_var
book_plots.plot_measurements(measuerments)
book_plots.plot_filter(xs[:, 0], var=ps[:, 1])
# book_plots.show_legend()
plt.show()
print(xs)
print(ps)