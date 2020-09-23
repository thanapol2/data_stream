from method.plot_data import  plot_data as plot_data
from method.lightcurve_benchmark.change_detection import  change_detection

cheb_windows_size = 100
k = 3
data = plot_data(path='C:\\Users\\karnk\\git\\data_stream\\code',type='test_pca',len = 1,interval = 5,img_path ='tran_img')
data.load_data()

# data.save_image_transient()
for i in range(data.get_file_lenght()):
    test_list = data.get_dataset_test(i)
    answer = data.get_dataset_answer(i)
    start_end = data.get_dataset_answer_st_ed(i)
    cd = change_detection(test_list=test_list,answer=answer,start_end=start_end)
    cd.compute_change(cheb_windows_size=cheb_windows_size,k=k)
    print(cd.get_tran_found())
    print(cd.get_false_count())
    # print("test")