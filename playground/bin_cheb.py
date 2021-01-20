from method.possion.plot_data_possion import  plot_data as plot_data



bin_period = 500
types = ["poisson"]
patterns = ["sq"]
LS = [1,5]
IS = [100]
for type in types:
    for pattern in patterns:
        for L in LS:
            for I in IS:
                data = plot_data(path='C:\\Users\\karnk\\git\\data_stream\\dataset', type=type, pattern=pattern, len=L,
                                 interval=I)
                # data = plot_data(path='D:\\git_project\\data stream\\dataset', type=type, pattern=pattern, len=L,
                #                  interval=I)
                data.load_data_fromfile()

                # binning process
                for i in range(data.get_file_lenght()):
                    file_name = data.get_file_name(i)
                    data_stream = data.get_dataset_test(i)
                    print(1)