from method.possion.plot_data_possion import  plot_data as plot_data
from method.window_tech.sliding_win import sliding_win
import kalman_playground.kalman_method as kalman
windows_size = 500
types = ["poisson"]
patterns = ["sq"]
LS = [1,5]
IS = [100]
for type in types:
    for pattern in patterns:
        for L in LS:
            for I in IS:
                data = plot_data(path='D:\\git_project\\data stream\\dataset', type=type, pattern=pattern, len=L,
                                 interval=I)
                data.load_data_fromfile()
                window = sliding_win(windows_size)
                for i in range(data.get_file_lenght()):
                    file_name = data.get_file_name(i)
                    measurements = data.get_dataset_test(i)
                    for measurement in measurements:
                        mean_cur = window.get_mean()
                        variance_cur = window.get_variance()
                        kalman.predict()
