import matplotlib.pyplot as plt
import glob
import matplotlib.axes as ax
import numpy as np
import os
import statistics
from method.Ad_cheb import Ad_cheb as ad_cheb
from datetime import datetime
from os import listdir
from os.path import isfile, join

# Fix parameter
# _path = "C:\\data stream\\data_stream\\dataset\\"
_path = "D:\\git_project\\data stream\\dataset\\"
_prefix = "poisson"
# _prefix = "hinet"
# _path = "C:\\Users\\karnk\\git\\data_stream\\dataset\\"
raw = _path + "training\\"+_prefix+"\\_train.txt"
_text_file = _path+"image\\"+_prefix+"\\result.txt"
patterns = [("si", 0, "SIN pattern"), ("sq", 1, "Square pattern"), ("tr", 2, "Triangle pattern")]
# patterns = [("si", 0, "SIN pattern"), ("sq", 1, "Square pattern")]
# patterns = [("si", 0, "SIN pattern")]


class plot_data():

    def __init__(self, pattern='sq',path='none',len = 1,interval = 5,type='pca'):
        self._path = path
        self._pattern = pattern
        self._len = len
        self._interval = interval
        self._type = type
        self._folder_pattern = "{}_L{}_I{}".format(self._pattern,self._len,self._interval)
        self.test_path = "{}\\lightcurve_benchmark\\{}\\{}\\test".format(self._path,self._type,self._folder_pattern)
        self.ans_path =  "{}\\lightcurve_benchmark\\{}\\{}\\answer".format(self._path, self._type,self._folder_pattern)
        self.image_tran_path = "{}\\lightcurve_benchmark\\{}\\{}\\tran_img".format(self._path, self._type,self._folder_pattern)

    def load_data(self):
        print("#### start open file {} l :{} i: {}".format(self._pattern, self._len, self._interval))
        test_files_list = []
        ans_files_list = []
        name_list = []
        print("Load : {}".format(self.test_path))
        for r, d, f in os.walk(self.test_path):
            for file in f:
                name_list.append(file)
                test_files_list.append(os.path.join(r, file))

        for r, d, f in os.walk(self.ans_path):
            for file in f:
                ans_files_list.append(os.path.join(r, file))
        print("#### End load file {} l :{} i: {}".format(self._pattern, self._len, self._interval))
        for index in range(len(test_files_list)):
            test_list = []
            answer_lists = []
            answer_st_ed_list = []
            print("#### start file test_files[index]    ###########")
            with open(test_files_list[index]) as txt_lines:
                for line in txt_lines:
                    test_list.append(int(line.replace('\n', '')))

            with open(ans_files_list[index]) as txt_lines:
                for line in txt_lines:
                    answer_lists.append(int(line.replace('\n', '')) * self._interval)

            for i in answer_lists:
                start = i
                end = i + self._interval
                answer_st_ed_list.append((start, end))

            min_ylim = min(test_list) - 100
            max_ylim = max(test_list) + 100
            fig = plt.gcf()
            fig.set_size_inches(18, 9)
            plt.plot(test_list)
            plt.gca().set_ylim(min_ylim, max_ylim)
            plt.gca().set_xlim(start - 500, end + 500)
            plt.axvline(start, color='green', linestyle='dashdot', linewidth=1)
            plt.axvline(end, color='green', linestyle='dashdot', linewidth=1)
            plt.gca().set_ylabel('value')
            plt.gca().set_xlabel('Time')
            plt.savefig(os.path.join(self.image_tran_path,"{}.png".format(name_list[index])))
            plt.clf()
            print("#### end file test_files[index]    ###########")




    def plotbench(_len=100,_width=1,min_len_cal=0,max_len_cal=1800000,
                  cheb_windows_size = 500,
                  xlim_min = 0,
                  xlim_max = 6000,
                  max_window = 500):
        result = []
        plot_resource = []
        # fig, axs = plt.subplots(3)
        # fig = plt.gcf()
        # fig.set_size_inches(18, 9)

        _len = _len

        _width = _width
        min_len_cal = min_len_cal
        max_len_cal = max_len_cal
        cheb_windows_size = cheb_windows_size
        k = 3
        xlim_min = 0
        xlim_max = 6000



        for pattern, num_graph, pattern_name in patterns:
            start_time = datetime.now()
            print("#### start file {} w :{} i: {}".format(pattern, _width, _len))
            test = _path + "test\\"+_prefix+"_test_" + pattern + "_w" + str(_width) + "_i" + str(_len) + ".txt"
            answer = _path + "answer\\"+_prefix+"_ans_" + pattern + "_w" + str(_width) + "_i" + str(_len) + ".txt"

            # test =  _path + "test\\hinet_test_si_w1_i100.txt"
            # answer = _path + "answer\\hinet_ans_"+pattern+"_w"+str(w)+"_i"+str(size)+".txt"

            test_list = []
            answer_lists = []
            answer_st_ed_list = []

            cheb_test = ad_cheb(max_window = 500)

            cheb_result_list = []

            with open(test) as txt_lines:
                for line in txt_lines:
                    test_list.append(int(line.replace('\n', '')))

            with open(answer) as txt_lines:
                for line in txt_lines:
                    answer_lists.append(int(line.replace('\n', '')) * _len)
            for i in answer_lists:
                start = i
                end = i + _len
                answer_st_ed_list.append((start, end))



            data_lists = test_list[min_len_cal:max_len_cal]

            print("#### start check cheb #######")
            for i in range(len(data_lists)):
                cheb_test.add_element(data_lists[i])
                # adwin.add_element(data_lists[i])
                if cheb_test.detected_change():
                # if adwin.detected_change():
                    cheb_result_list.append(i)

            print("#### end check cheb #######")
            print("#### plot  cheb #######")
            # for i in cheb_result_list:
            #     axs[num_graph].axvline(i, color='red', linestyle='-', linewidth=0.7)
            #
            # axs[num_graph].plot(test_list)
            # axs[num_graph].set_ylim(55, 155)
            # axs[num_graph].set_xlim(xlim_min, xlim_max)
            # axs[num_graph].set_ylabel('value')
            # axs[num_graph].set_xlabel('Time')

            tittle = "{}: Width = {} Length = {}".format(pattern_name, _width, _len)
            # axs[num_graph].set_title(tittle, fontsize=20)
            #     acc cal
            transit_count = len(answer_st_ed_list)
            count = 0
            true_count = 0
            print("#### cal result  cheb #######")
            for start, end in answer_st_ed_list:
                found = False
                for cheb_result in cheb_result_list:
                    if (start <= cheb_result) & (cheb_result <= end):
                        true_count = true_count + 1
                        if not found:
                            count = count + 1
                            found = True
            alert_count = len(cheb_result_list)
            false_count = alert_count-true_count
            print("ADW & CHEB = {}".format(cheb_test.get_count()))
            print("acc  {} w = {} i ={} trans_num = {} tran_found = {} "
                  "rate = {} alert_count = {},false_count ={} false_rate ={}"
                  .format(pattern_name,
                          _width,
                          _len,
                          transit_count,
                          count,
                          (float(count) / float(transit_count) * 100),
                          alert_count,
                          false_count,
                          float(false_count)/(float(alert_count)+1)*100)
                  )

            with open(_text_file, "a") as myfile:
                end_time = datetime.now()
                myfile.write("\n=============ADWIN================\n")
                myfile.write("file : {}  start time : {} end time {} \n".format(_prefix,str(start_time),str(end_time)))
                myfile.write("acc  {} w = {} i ={} trans_num = {} tran_found = {} "
                  "rate = {} alert_count = {},false_count ={} false_rate ={}"
                  .format(pattern_name,
                          _width,
                          _len,
                          transit_count,
                          count,
                          (float(count) / float(transit_count) * 100),
                          alert_count,
                          false_count,
                          float(false_count)/float(alert_count)*100)
                  )
                myfile.write("\n=============ADWIN================\n")
                myfile.close()

            data_dic = {
                'pattern_name':pattern_name,
                'pattern_shot':pattern,
                'w':_width,
                'i':_len,
                'acc': (float(count) / float(transit_count) * 100),
                'found' : count,
                'test' : transit_count,
                'test_list':test_list,
                'answer_st_ed_list':answer_st_ed_list,
                'cheb_result_list':cheb_result_list,
                # 'list_up_variance' : list_up_variance,
                # 'list_low_variance' :list_low_variance,
                'tittle_graph': tittle
            }
            result.append(data_dic)

        # plt.show()
        return(result)

    def plot_result(results):
        for result in results:
            pattern_shot = result['pattern_shot']
            pattern_name= result['pattern_name']
            _width = result['w']
            _len = result['i']
            _acc = result['acc']
            _found = result['found']
            _transit_count = result['test']
            test_list = result['test_list']
            answer_st_ed_list = result['answer_st_ed_list']
            cheb_result_list = result['cheb_result_list']
            tittle= result['tittle_graph']
            # list_up_variance = result['list_up_variance']
            # list_low_variance = result['list_low_variance']
            count_image = 0
            min_ylim = min(test_list)-100
            max_ylim = max(test_list)+100
            folder_image = _path + "image\\"+_prefix+"\\{}\\w{}\\{}\\".format(pattern_shot, _width, _len)
            # folder_image = _path + "image\\" + _prefix + "_ad\\{}\\w{}\\{}\\".format(pattern_shot, _width, _len)
            print(len(answer_st_ed_list))
            print(folder_image)
            for start,end in answer_st_ed_list:
                image_name = "w{}_i{}_image{}.png".format(_width,_len,count_image)
                print("------save file {}".format(image_name))
                fig = plt.gcf()
                fig.set_size_inches(18, 9)
                plt.plot(test_list)
                # plt.plot(list_up_variance,color='red')
                # plt.plot(list_low_variance,color='red')
                plt.gca().set_ylim(min_ylim, max_ylim)
                plt.gca().set_xlim(start-500, end+500)
                plt.axvline(start, color='green', linestyle='dashdot', linewidth=1)
                plt.axvline(end, color='green', linestyle='dashdot', linewidth=1)
                plt.gca().set_ylabel('value')
                plt.gca().set_xlabel('Time')
                for cheb in cheb_result_list:
                    plt.axvline(cheb, color='red', linestyle='-', linewidth=0.7)
                plt.savefig(folder_image+image_name)
                # plt.show()
                plt.clf()
                count_image = count_image + 1

