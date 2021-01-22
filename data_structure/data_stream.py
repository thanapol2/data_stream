from datetime import datetime
import math
import matplotlib.pyplot as plt
import os
import csv

class data_stream():

    def __init__(self, pattern='sq',path='none',len = 1,interval = 5,type='pca',is_limit = True):
        self.reset()
        self.reset_dataset()
        self.is_limit = is_limit
        self._path = path
        self._pattern = pattern
        self._len = len
        self._interval = interval
        self._type = type
        self._testfile = "{}_test_{}_w{}_i{}.txt".format(self._type,self._pattern,self._len,self._interval)
        self._ansfile = "{}_ans_{}_w{}_i{}.txt".format(self._type, self._pattern, self._len, self._interval)
        self.test_path = "{}\\test".format(self._path)
        self.ans_path =  "{}\\answer".format(self._path)

        self.text_file = "{}\\{}_result.txt".format(self._path,self._testfile)
        self.test_files_list = []
        self.ans_files_list = []
        self.name_list = []
        self.dataset_test_list = []
        self.dataset_answer_list = []
        self.dataset_answer_st_ed_list = []
        self.change_points = []

    def reset(self):
        self.is_limit = True
        self._path = ""
        self._pattern = ""
        self._len = 0.0
        self._interval = 0.0
        self._type = ""
        self._folder_pattern = ""
        self.test_path = ""
        self.ans_path =  ""
        self.text_file = ""
        self.change_points = []


    def reset_dataset(self):
        self.test_files_list = []
        self.ans_files_list = []
        self.name_list = []
        self.dataset_test_list = []
        self.dataset_answer_list = []
        self.dataset_answer_st_ed_list = []
        self.change_points = []

    def get_dataset_test(self,index):
        return self.dataset_test_list[index]

    def get_dataset_answer(self,index):
        return self.dataset_answer_list[index]

    def get_dataset_answer_st_ed(self,index):
        return self.dataset_answer_st_ed_list[index]

    def get_file_lenght(self):
        print(len(self.name_list))
        return int(len(self.name_list))

    def get_file_name(self,index):
        return self.name_list[index]

    def set_change_points(self,change_points):
        self.change_points = change_points

    def load_data(self):
        self.reset_dataset()
        print("#### start open file {} l :{} i: {}".format(self._pattern, self._len, self._interval))
        print("Load : {}".format(self.test_path))
        for r, d, f in os.walk(self.test_path):
            self.name_list.append(self._file)
            self.test_files_list.append(os.path.join(r, self._file))

        for r, d, f in os.walk(self.ans_path):
            for file in f:
                self.ans_files_list.append(os.path.join(r, file))
        print("#### End load file {} l :{} i: {}".format(self._pattern, self._len, self._interval))

        for index in range(len(self.test_files_list)):
            test_list = []
            answer_lists = []
            answer_st_ed_list = []
            print("#### start file {}    ###########".format(self.name_list[index]))
            with open(self.test_files_list[index]) as txt_lines:
                for line in txt_lines:
                    test_list.append(int(line.replace('\n', '')))

            with open(self.ans_files_list[index]) as txt_lines:
                for line in txt_lines:
                    answer_lists.append(int(line.replace('\n', ''))*self._interval)
                    print ("{} .... {}".format(int(line.replace('\n', '')) ,int(line.replace('\n', '')) * self._interval))
            for i in answer_lists:
                start = i
                end = i + self._interval
                answer_st_ed_list.append([start, end])
            self.dataset_test_list.append(test_list)
            self.dataset_answer_list.append(answer_lists)
            self.dataset_answer_st_ed_list.append(answer_st_ed_list)

            print("#### end file test_files[index]    ###########")

    def load_data_fromfile(self):
        self.reset_dataset()
        print("#### start open file {} l :{} i: {}".format(self._pattern, self._len, self._interval))
        print("Load : {}".format(self.test_path))
        for r, d, f in os.walk(self.test_path):
            self.name_list.append(self._testfile)
            self.test_files_list.append(os.path.join(r, self._testfile))

        for r, d, f in os.walk(self.ans_path):
            self.ans_files_list.append(os.path.join(r, self._ansfile))
        print("#### End load file {} l :{} i: {}".format(self._pattern, self._len, self._interval))

        for index in range(len(self.test_files_list)):
            test_list = []
            answer_lists = []
            answer_st_ed_list = []
            print("#### start file {}    ###########".format(self.name_list[index]))
            with open(self.test_files_list[index]) as txt_lines:
                for line in txt_lines:
                    test_list.append(int(line.replace('\n', '')))

            with open(self.ans_files_list[index]) as txt_lines:
                for line in txt_lines:
                    answer_lists.append(int(line.replace('\n', ''))*self._interval)
                    print ("{} .... {}".format(int(line.replace('\n', '')) ,int(line.replace('\n', '')) * self._interval))
            for i in answer_lists:
                start = i
                end = i + self._interval
                answer_st_ed_list.append([start, end])
            self.dataset_test_list.append(test_list)
            self.dataset_answer_list.append(answer_lists)
            self.dataset_answer_st_ed_list.append(answer_st_ed_list)

            print("#### end file test_files[index]    ###########")

    def save_image_transient(self,is_tranline = True,img_path ='tran_img'):
        image_tran_path = "{}\\{}".format(self._path,img_path)
        if not os.path.exists(image_tran_path):
            print("######## Create folder image###############")
            os.mkdir(image_tran_path)
        print("#### start save image {} l :{} i: {}".format(self._pattern, self._len, self._interval))
        for index in range(len(self.test_files_list)):

            test_list = self.dataset_test_list[index]
            start_end = self.dataset_answer_st_ed_list[index]
            start = start_end[0][0]
            end = start_end[0][1]
            min_ylim = min(test_list) - 100
            max_ylim = max(test_list) + 100
            fig = plt.gcf()
            fig.set_size_inches(18, 9)
            plt.plot(test_list)
            plt.gca().set_ylim(min_ylim, max_ylim)
            if self.is_limit:
                plt.gca().set_xlim(start - 200, end + 200)
            if is_tranline:
                plt.axvline(start, color='green', linestyle='dashdot', linewidth=1)
                plt.axvline(end, color='green', linestyle='dashdot', linewidth=1)
            plt.gca().set_ylabel('value')
            plt.gca().set_xlabel('Time')
            plt.savefig(os.path.join(image_tran_path, "{}.png".format(self.name_list[index])))
            plt.clf()
        print("#### END save image {} l :{} i: {}".format(self._pattern, self._len, self._interval))

        def save_result_changepoint(self,result_list):
            self.result_data_set = result_list
            print("#### save result_complete   ###########")

