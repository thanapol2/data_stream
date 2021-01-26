from data_structure.data_stream import data_stream as data_stream
import kalman_playground.kalman_method as kalman
import numpy as np
from method.change_de.adwin_cheb import adwin_cheb as adwin

# Kalman setting
x_start = 10
x_var_start = 10000
model_mean = 0
model_variance = 0.01
# ###########################

windows_size = 500
types = ["poisson"]
patterns = ["sq","tr","si"]
LS = [1,3,5]
IS = [100,500,1000]
process_var = 1
process_mean = 0
for type in types:
    for pattern in patterns:
        for L in LS:
            for I in IS:
                # data = data_stream(path='C:\\Users\\karnk\\git\\data_stream\\dataset', type=type, pattern=pattern, len=L,
                #                  interval=I)
                data = data_stream(path='D:\\git_project\\data stream\\dataset', type=type, pattern=pattern, len=L,
                                 interval=I)
                data.load_data_fromfile()

                # cheb
                cheb = adwin(max_window=500,k=3)
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

                data.set_change_points(change_points)
                # print(change_points)
                result_name = '{}_W{}_L{}'.format(type, L, I)

                data.save_result_to_csv(dataset_index=0, threshold_after=100, L=L, I=I, Algorithm="Kalman ADWIN",
                                        Dataset_type=type,pattern=pattern)
