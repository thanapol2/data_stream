from data_structure.data_stream import data_stream as data_stream
from method.change_de.adwin_cheb import adwin_cheb as adwin

bin_period = 500
types = ["poisson"]
patterns = ["sq"]
LS = [1,5]
IS = [100]
for type in types:
    for pattern in patterns:
        for L in LS:
            for I in IS:
                # data = data_stream(path='C:\\Users\\karnk\\git\\data_stream\\dataset', type=type, pattern=pattern, len=L,
                #                  interval=I)
                data = data_stream(path='D:\\git_project\\data stream\\dataset', type=type, pattern=pattern, len=L,
                                 interval=I)
                data.load_data_fromfile()

                # binning process
                cheb = adwin(max_window=500,k=3)
                change_points = []
                for i in range(data.get_file_lenght()):
                    file_name = data.get_file_name(i)
                    instances = data.get_dataset_test(i)

                    for index, instance in enumerate(instances):
                        is_change = cheb.add_element(instance)
                        if is_change:
                            change_points.append(index)

                data.set_change_points(change_points)
                print(change_points)
                csv_path = 'D:\\git_project\\data stream\\result\\{}_W{}_L{}'