from datetime import datetime
import math
import matplotlib.pyplot as plt
import os
import csv

class plot_data():

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


    def reset_dataset(self):
        self.test_files_list = []
        self.ans_files_list = []
        self.name_list = []
        self.dataset_test_list = []
        self.dataset_answer_list = []
        self.dataset_answer_st_ed_list = []

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

    def save_image_changepoint_with_tran(self,change_point_list,index,range_per_file=500,img_path ='tran_img'):
        # folder_changepoint_path = "{}\\lightcurve_benchmark\\{}\\{}\\{}\\{}".format(self._path, self._type, self._folder_pattern,
        #                                                                 img_path,self.name_list[index])
        image_tran_path = "{}\\{}\\".format(self._path, self._type)
        if not os.path.exists(image_tran_path):
            print("######## Create folder image###############")
            os.mkdir(image_tran_path)
        image_tran_path = "{}\\{}\\{}\\".format(self._path, self._type, self._pattern)
        if not os.path.exists(image_tran_path):
            print("######## Create folder image###############")
            os.mkdir(image_tran_path)
        image_tran_path = "{}\\{}\\{}\\{}".format(self._path, self._type, self._pattern,
                                                  self._len)
        if not os.path.exists(image_tran_path):
            print("######## Create folder image###############")
            os.mkdir(image_tran_path)
        image_tran_path = "{}\\{}\\{}\\{}\\{}".format(self._path, self._type, self._pattern,
                                                  self._len,self._interval)
        if not os.path.exists(image_tran_path):
            print("######## Create folder image###############")
            os.mkdir(image_tran_path)


        print("#### start save image {} l :{} i: {}".format(self._pattern, self._len, self._interval))
        test_list = self.dataset_test_list[index]
        min_ylim = min(test_list) - 100
        max_ylim = max(test_list) + 100
        num_image = math.ceil(len(test_list)/range_per_file)
        st_ed_tran = self.get_dataset_answer_st_ed(index)
        for i in range(len(st_ed_tran)):
            st_tran = st_ed_tran[i][0]
            ed_tran = st_ed_tran[i][1]
            plt.axvline(st_tran, color='green', linewidth=1)
            plt.axvline(ed_tran, color='green', linewidth=1)
            fig = plt.gcf()
            fig.set_size_inches(8, 5)
            plt.rc('xtick', labelsize=13)
            plt.rc('ytick', labelsize=13)
            plt.rc('axes', labelsize=15)
            plt.plot(test_list)
            plt.gca().set_ylim(min_ylim, max_ylim)
            plt.gca().set_ylabel('value')
            plt.gca().set_xlabel('Time')
            plt.gca().set_xlim(st_tran - 200, ed_tran + 200)
            for change_point in change_point_list:
                plt.axvline(change_point, color='red', linewidth=1)
            plt.savefig(os.path.join(image_tran_path, "{}_{}_t.png".format(self.name_list[index],i)))
            plt.clf()
            print("####  save image {}_{}_t.png".format(self.name_list[index],i))

        print("#### END save image {} l :{} i: {}".format(self._pattern, self._len, self._interval))

    def save_image_changepoint(self,change_point_list,index,range_per_file=500,img_path ='tran_img'):
        image_tran_path = "{}\\lightcurve_benchmark\\{}\\{}\\{}".format(self._path, self._type, self._folder_pattern,
                                                                        img_path)
        folder_changepoint_path = "{}\\lightcurve_benchmark\\{}\\{}\\{}\\{}".format(self._path, self._type, self._folder_pattern,
                                                                        img_path,self.name_list[index])
        if not os.path.exists(image_tran_path):
            print("######## Create folder image###############")
            os.mkdir(image_tran_path)
        if not os.path.exists(folder_changepoint_path):
            print("######## Create folder image {}###############".format(folder_changepoint_path))
            os.mkdir(folder_changepoint_path)
        print("#### start save image {} l :{} i: {}".format(self._pattern, self._len, self._interval))
        test_list = self.dataset_test_list[index]
        min_ylim = min(test_list) - 100
        max_ylim = max(test_list) + 100
        num_image = math.ceil(len(test_list)/range_per_file)
        for change_point in change_point_list:
            plt.axvline(change_point, color='red', linewidth=1)
        st_ed_tran = self.get_dataset_answer_st_ed(index)
        st_tran = st_ed_tran[0][0]
        ed_tran = st_ed_tran[0][1]
        plt.axvline(st_tran, color='green', linewidth=1)
        plt.axvline(ed_tran, color='green', linewidth=1)
        fig = plt.gcf()
        fig.set_size_inches(18, 9)
        plt.plot(test_list)
        plt.gca().set_ylim(min_ylim, max_ylim)
        plt.gca().set_ylabel('value')
        plt.gca().set_xlabel('Time')
        for index_image in range(num_image):
            start = 0 + (range_per_file*index_image)
            end = 500 + range_per_file*index_image
            plt.gca().set_xlim(start, end)
            plt.savefig(os.path.join(folder_changepoint_path, "{}_{}.png".format(self.name_list[index],index_image)))
        plt.clf()

        print("#### END save image {} l :{} i: {}".format(self._pattern, self._len, self._interval))

    def save_result(self,count_found,count_false):
        with open(self.text_file, "a+") as txtfile:
            timestamp = datetime.now()
            txtfile.write("\n============={}================\n".format(timestamp))
            txtfile.write("Type  : {} pattern : {} L = {} I ={} \n"
              .format(self._type,self._pattern,self._len,self._interval))
            txtfile.write("Num Tran  : {} Tran Found : {} False Found ={} \n"
                          .format(self.get_file_lenght(), count_found, count_false))
            txtfile.write("\n============={}================\n".format(timestamp))
            txtfile.close()



    def save_result_csv(self,type,pattern,I,L,index,algorithm,tran_found,count_true,count_false,csv_file="result"):
        file_csv_name = "{}.csv".format(csv_file)
        with open(file_csv_name, mode='a', newline="") as file:
            attribute_name = ['TYPE', 'PATTERN', 'L', 'I', 'file_name', 'algorithm', 'True_alert',
                              'false_alert', 'total_alert',  'tran_found','DATE_TIME']
            writer = csv.DictWriter(file, fieldnames=attribute_name)
            # if not os.path.exists(file_csv_name):
            #     writer.writeheader()

            writer.writerow({'TYPE': type,
                             'PATTERN': pattern,
                             'L': L,
                             'I': I,
                             'file_name': self.get_file_name(index),
                             'algorithm': algorithm,
                             'True_alert': str(count_true),
                             'false_alert': str(count_false),
                             'total_alert': str(count_true+count_false),
                             'tran_found': str(tran_found),
                             'DATE_TIME': str(datetime.now())})

        print("#### END save image {} l :{} i: {}".format(self._pattern, self._len, self._interval))