from method.possion.plot_data_possion import  plot_data as plot_data
from method.window_tech.sliding_win import sliding_win
import kalman_playground.kalman_method as kalman
import numpy as np
from method.change_de.baseline_cheb import chebyshev_base as chebyshev_base


# Kalman setting
x_start = 10
x_var_start = 10000
model_mean = 0
model_variance = 0.01
# ###########################

windows_size = 500
types = ["poisson"]
patterns = ["sq"]
LS = [1,5]
IS = [100]
process_var = 1
process_mean = 0
for type in types:
    for pattern in patterns:
        for L in LS:
            for I in IS:
                data = plot_data(path='C:\\Users\\karnk\\git\\data_stream\\dataset', type=type, pattern=pattern, len=L,
                                 interval=I)
                # data = plot_data(path='D:\\git_project\\data stream\\dataset', type=type, pattern=pattern, len=L,
                #                  interval=I)
                data.load_data_fromfile()

                # cheb
                cheb = chebyshev_base(max_window=500, k=3)
                change_points = []

                #Kalman
                for i in range(data.get_file_lenght()):
                    file_name = data.get_file_name(i)
                    measurements = data.get_dataset_test(i)
                    xs = np.zeros((len(measurements), 2))
                    ps = np.zeros((len(measurements), 2))

                    x = x_start
                    x_var = x_var_start
                    for index, measurement in enumerate(measurements):
                        x, x_var = kalman.update(x, x_var, measurement, model_variance)
                        xs[i] = x,x_var
                        x , x_var = kalman.predict(x, x_var, model_mean, model_variance)
                        ps[i] = x, x_var

                        is_change = cheb.add_element(x)
                        if is_change:
                            change_points.append(index)
                print(change_points)

