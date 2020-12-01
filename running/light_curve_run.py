from method.plot_data import  plot_data as plot_data
from method.lightcurve_benchmark.change_detection import  change_detection

cheb_windows_size = 50
k = 3
types = ["pca"]
LS = [1,5]
IS = [5,10,30,60]
# types = ["test"]
# LS = [5]
# IS = [5,10]
for type in types:
    for L in LS:
        for I in IS:
            data = plot_data(path='D:\\git_project\\data stream\\', type=type, len = L, interval = I)
            data.load_data()

            # data.save_image_transient()
            # data.save_image_transient(is_tranline = False,img_path ='tran_img_noline')
            count_found = 0
            count_false = 0
            for i in range(data.get_file_lenght()):
                file_name = data.get_file_name(i)
                test_list = data.get_dataset_test(i)
                answer = data.get_dataset_answer(i)
                start_end = data.get_dataset_answer_st_ed(i)
                cd = change_detection(method_type=0,test_list=test_list,answer=answer,start_end=start_end)
                cd.compute_change(cheb_windows_size=cheb_windows_size,k=k)
                count_found = count_found + cd.get_true_count()
                count_false = count_false + cd.get_false_count()
                data.save_result_csv(type=type, pattern='SQ', I=I, L=L, index=i, algorithm="Cheb size 50", count_true=count_found,
                                     count_false=count_false, tran_found=cd.get_tran_found(), csv_file="base")
                # data.save_image_changepoint(change_point_list=cd.get_change_points(),index=i)
                # data.save_image_changepoint_with_tran(change_point_list=cd.get_change_points(), index=i)
            # data.save_result(count_found,count_false)
                # print("test")