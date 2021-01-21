from method.possion.plot_data_possion import  plot_data as plot_data
from method.window_tech.sliding_win import sliding_win
import kalman_playground.kalman_method as kalman
import numpy as np
from kalman_playground.kf_book import book_plots as book_plots
import kalman_playground.kf_book.kf_internal as kf_internal
import matplotlib.pyplot as plt

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
                window = sliding_win(windows_size)
                for i in range(data.get_file_lenght()):
                    file_name = data.get_file_name(i)
                    measurements = data.get_dataset_test(i)[:50]
                    xs, priors = np.zeros((len(measurements), 2)), np.zeros((len(measurements), 2))
                    x_mean = 100
                    x_variance = 400
                    for index,measurement in enumerate(measurements):
                        prior_mean, prior_variance = kalman.predict(x_mean, x_variance, process_mean, process_var)

                        window.append(measurement)
                        measurement_mean = window.get_mean()
                        measurement_variance = window.get_variance()
                        x_mean, x_variance = kalman.update(prior_mean,prior_variance,measurement_mean,measurement_variance)

                        priors[index] = [prior_mean, prior_variance]
                        xs[index] = [x_mean, x_variance]

                    book_plots.plot_measurements(measurements)
                    book_plots.plot_filter(xs[:, 0], var=priors[:, 1])
                    book_plots.plot_predictions(priors[:, 0])
                    book_plots.show_legend()
                    kf_internal.print_variance(xs)
                    plt.show()