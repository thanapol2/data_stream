from data_structure.data_stream import data_stream as data_stream
from method.binning import binning as binning
from method.change_de.baseline_cheb import chebyshev_base as chebyshev_base

bin_period = 500
types = ["poisson"]
patterns = ["sq","tr","si"]
LS = [1,3,5]
IS = [100,500,1000]
for type in types:
    for pattern in patterns:
        for L in LS:
            for I in IS:
                # data = data_stream(path='C:\\Users\\karnk\\git\\data_stream\\dataset', type=type, pattern=pattern, len=L,
                #                  interval=I)
                data = data_stream(path='D:\\git_project\\data stream\\dataset', type=type, pattern=pattern, len=L,
                                 interval=I)
                data.load_data_fromfile()

                # # Cheb
                cheb = chebyshev_base(max_window=500,k=3)
                change_points = []
                for i in range(data.get_file_lenght()):
                    file_name = data.get_file_name(i)
                    instances = data.get_dataset_test(i)

                    for index, instance in enumerate(instances):
                        is_change = cheb.add_element(instance)
                        if is_change:
                            change_points.append(index)

                # change_points = [1,200,300]
                data.set_change_points(change_points)

                # print(change_points)
                result_name = '{}_W{}_L{}'.format(type,L,I)

                data.save_result_to_csv(dataset_index=0,threshold_after = 100,L=L,I=I,Algorithm="Base Cheb 500",Dataset_type=type)