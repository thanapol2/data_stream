import numpy as np
import statistics
from skmultiflow.drift_detection.base_drift_detector import BaseDriftDetector

class Ad_cheb(BaseDriftDetector):

    def __init__(self,k=3,delta=.002,max_window = 10000):
        self.window = []
        self.reset()
        self.k = k
        self.delta = delta
        self.count_detect = 0
        self.mean = 0
        self.max_window = max_window


    def reset(self):
        super().reset()
        self.window = []

    def get_count(self):
        return (self.count_detect)

    # def add_element(self, value):
    #     bln_change = False
    #     self.window.append(value)
    #     # if len(self.window)>self.max_window:
    #     #     self.window.pop(0)
    #     # if(len(self.window)==501):
    #     #     print('1')
    #     self.mean = float((self.mean*(len(self.window)-1)+value)/len(self.window))
    #     variance = np.std(self.window)
    #     if abs(value - self.mean) > self.k * variance:
    #         bln_change = True
    #         print("detect len {}".format(len(self.window)))
    #         # self.window = []
    #     # self._width += 1
    #     # else:
    #     #     if len(self.window) > 1000 | bln_change:
    #         adwin_change = self.update_by_adwin(value)
    #         # print("clear len {}".format(len(self.window)))
    #         # if adwin_change&bln_change:
    #         #     self.count_detect = self.count_detect + 1
    #     self.in_concept_change = bln_change
    #     return bln_change

    def add_element(self, value):
        bln_change = False
        self.window.append(value)
        self.mean = float((self.mean*(len(self.window)-1)+value)/len(self.window))
        variance = np.std(self.window)
        if abs(value - self.mean) > self.k * variance:
            bln_change = True
            print("detect len {}".format(len(self.window)))
            self.window = []
        else:
            if len(self.window) > 1000:
                adwin_change = self.update_by_adwin(value)
        self.in_concept_change = bln_change
        return bln_change


    def update_by_adwin(self,value):
        w1 = []
        w2 = self.window[:]
        end_loop = False
        update_window = False
        cursor = 0
        # while len(w2)>self.max_window:
        #     w2.pop(0)
        while not end_loop:
            _max = max(self.window[:])
            _min = min(self.window[:])
            mean_w1 = 0
            self.mean = 0
            n = len(self.window)
            for i in w2:
                w1.append(w2.pop(0))
                if len(w1) > 0:
                    mean_w1 = statistics.mean(w1)
                if len(w2) > 0:
                    self.mean = statistics.mean(w2)
                cal = abs(mean_w1 - self.mean)
                variance = np.std(self.window)
                if cal > 3*variance:
                    end_loop = True
                    # update w
                    self.window = w2[:]
                    update_window = True
                    break
                if len(w2) == 0:
                    end_loop = True
        return update_window