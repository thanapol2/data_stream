from method.possion.plot_data_possion import  plot_data as plot_data
from method.window_tech.sliding_win import sliding_win
import kalman_playground.kalman_method as kalman
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
                data.load_data_fromfile()
                window = sliding_win(windows_size)
                for i in range(data.get_file_lenght()):
                    file_name = data.get_file_name(i)
                    measurements = data.get_dataset_test(i)
                    x_mean = 0
                    x_variance = 400
                    for measurement in measurements:
                        prior_mean = window.get_mean()
                        prior_variance = window.get_variance()
                        window.append(measurement)
                        measurement_mean = window.get_mean()
                        measurement_variance = window.get_variance()
                        prior_mean, prior_variance = kalman.predict(x_mean,x_variance,process_mean,process_var)
                        x_mean, x_variance = kalman.update(prior_mean,prior_variance,measurement_mean,measurement_variance)
                        print ('a')
