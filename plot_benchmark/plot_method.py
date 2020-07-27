import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import os
import statistics
# from chebyshev_SEA import chebyshev_SEA as chebyshev
from chebyshev_adwin import chebyshev_adwin as chebyshev
from skmultiflow.drift_detection.adwin import ADWIN

def plotbench(_len=100,_width=1,min_len_cal=0,max_len_cal=1800000,
              cheb_windows_size = 500,
              xlim_min = 0,
              xlim_max = 6000):
    result = []
    fig, axs = plt.subplots(3)
    fig = plt.gcf()
    fig.set_size_inches(18, 9)

    _len = _len
    patterns = [("si", 0, "SIN pattern"), ("sq", 1, "Square pattern"), ("tr", 2, "Triangle pattern")]
    _width = _width
    min_len_cal = min_len_cal
    max_len_cal = max_len_cal
    cheb_windows_size = cheb_windows_size
    k = 3
    xlim_min = 0
    xlim_max = 6000

    _path = "D:\\git_project\\data stream\\dataset\\"
    # _path = "C:\\Users\\karnk\\git\\data_stream\\dataset\\"
    raw = _path + "training\\poisson_train.txt"
    for pattern, num_graph, pattern_name in patterns:
        test = _path + "test\\poisson_test_" + pattern + "_w" + str(_width) + "_i" + str(_len) + ".txt"
        answer = _path + "answer\\poisson_ans_" + pattern + "_w" + str(_width) + "_i" + str(_len) + ".txt"

        # test =  _path + "test\\hinet_test_si_w1_i100.txt"
        # answer = _path + "answer\\hinet_ans_"+pattern+"_w"+str(w)+"_i"+str(size)+".txt"

        test_list = []
        answer_lists = []
        answer_st_ed_list = []

        cheb_test = chebyshev(max_size=cheb_windows_size, k=k)
        cheb_test_list = []

        with open(test) as txt_lines:
            for line in txt_lines:
                test_list.append(int(line.replace('\n', '')))

        with open(answer) as txt_lines:
            for line in txt_lines:
                answer_lists.append(int(line.replace('\n', '')) * _len)
        for i in answer_lists:
            start = i
            end = i + _len
            # if start<= max_len_cal:
            #     if  end > max_len_cal:
            #         end = max_len_cal-1
            xa = range(start, end)
            answer_st_ed_list.append((start, end))
            ya = [160] * _len  # Fix high of area
            # axs[num_graph].axvline(start, color='red', linestyle='-', linewidth=0.7)
            axs[num_graph].fill_between(xa, ya, alpha=0.30, color='orange')

        data_lists = test_list[min_len_cal:max_len_cal]
        for i in range(len(data_lists)):
            cheb_test.add_element(data_lists[i])
            # adwin.add_element(data_lists[i])
            if cheb_test.detected_change():
            # if adwin.detected_change():
                cheb_test_list.append(i)

        for i in cheb_test_list:
            axs[num_graph].axvline(i, color='red', linestyle='-', linewidth=0.7)

        axs[num_graph].plot(test_list)
        axs[num_graph].set_ylim(55, 155)
        axs[num_graph].set_xlim(xlim_min, xlim_max)
        axs[num_graph].set_ylabel('value')
        axs[num_graph].set_xlabel('Time')
        # axs[1].ylabel('value')
        # axs[1].xlabel('Time')
        # fig.suptitle(pattern+" Width = "+ str(_width)+" Length ", fontsize=20)
        # fig.suptitle("Chev with max_size = "+str(max_size)+" min_size =  "+str(min_size), fontsize=20)
        # fig.suptitle("Chev with max_size = 3000", fontsize=20)

        # plt.plot(list_mean,color='green',linewidth=1)
        # plt.plot(list_up_variance,color='red')
        # plt.plot(list_low_variance,color='red')
        tittle = "{}: Width = {} Length = {}".format(pattern_name, _width, _len)
        # axs[num_graph].set_title(pattern_name+": Width = "+ str(_width)+" Length =" + str(_len), fontsize=20)
        axs[num_graph].set_title(tittle, fontsize=20)
        #     acc cal
        transit_count = len(answer_st_ed_list)
        count = 0
        for start, end in answer_st_ed_list:
            found = False
            i = 0
            while (i < len(cheb_test_list)) & (not found):
                if (start <= cheb_test_list[i]) & (cheb_test_list[i] <= end):
                    count = count + 1
                    found = True
                i = i + 1
        print("acc  {} w = {} i ={} trans_num = {} found = {} rate = {}"
              .format(pattern_name,
                      _width,
                      _len,
                      transit_count,
                      count,
                      (float(count) / float(transit_count) * 100)))
        data_dic = {
            'pattern_name':pattern_name,
            'w':_width,
            'i':_len,
            'acc': (float(count) / float(transit_count) * 100),
            'found' : count,
            'test' : transit_count
        }
        result.append(data_dic)
    plt.show()