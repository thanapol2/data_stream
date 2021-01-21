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
LS = [5]
IS = [1000]
model_var = 1
model_mean = 0
for type in types:
    for pattern in patterns:
        for L in LS:
            for I in IS:
                # data = plot_data(path='C:\\Users\\karnk\\git\\data_stream\\dataset', type=type, pattern=pattern, len=L,
                #                  interval=I)
                data = plot_data(path='D:\\git_project\\data stream\\dataset', type=type, pattern=pattern, len=L,
                                 interval=I)
                data.load_data_fromfile()
                window = sliding_win(windows_size)
                for i in range(data.get_file_lenght()):
                    file_name = data.get_file_name(i)
                    measurements = data.get_dataset_test(i)[0:40000]
                    x = 10
                    x_var = 10000
                    model_mean = 0
                    model_var = 0.01
                    xs = np.zeros((len(measurements), 2))
                    ps = np.zeros((len(measurements), 2))

                    for i, measurement in enumerate(measurements):
                        x, x_var = kalman.update(x, x_var, measurement, model_var)
                        xs[i] = x, x_var
                        x, x_var = kalman.predict(x, x_var, model_mean, model_var)

                        ps[i] = x, x_var

                    fig = plt.gcf()

                    fig.set_size_inches(20, 9)

                    # book_plots.plot_measurements(measurements)
                    book_plots.plot_filter(xs[:, 0])
                    # book_plots.show_legend()
                    plt.gca().set_xlim(27500, 29500)
                    plt.show()
                    # print(xs)
                    print(ps)