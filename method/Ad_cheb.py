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
        self.max_window = max_window


    def reset(self):
        super().reset()
        self.window = []

    def get_count(self):
        return (self.count_detect)

    def add_element(self, value):
        bln_change = False
        self.window.append(value)
        # if(len(self.window)==501):
        #     print('1')
        mean = sum(self.window) / len(self.window)
        variance = np.std(self.window)
        if abs(value - mean) > self.k * variance:
            bln_change = True
            print("detect len {}".format(len(self.window)))
            # self.window = []
        # self._width += 1
        # else:
        if len(self.window) > 1000:
            adwin_change = self.update_by_adwin(value)
            print("clear len {}".format(len(self.window)))
            # if adwin_change&bln_change:
            #     self.count_detect = self.count_detect + 1
        # if len(self.window)>10000:
        #     self.window.pop(0)
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
            mean_w2 = 0
            n = len(self.window)
            for i in w2:
                w1.append(w2.pop(0))
                if len(w1) > 0:
                    mean_w1 = statistics.mean(w1)
                if len(w2) > 0:
                    mean_w2 = statistics.mean(w2)
                cal = abs(mean_w1 - mean_w2)
                # m = (1. / (len(w1) + 1)) + (1. / (len(w2) + 1))
                # dd = np.log(2*np.log(n)/self.delta)
                variance = np.std(self.window)
                # epsilon = np.sqrt(2 * m * variance * dd) + 1. * 2 / 3 * dd * m
                # print ("cal {} var {}".format(cal,variance))
                if cal > 3*variance/(np.sqrt(statistics.harmonic_mean(self.window))):
                    end_loop = True
                    # update w
                    self.window = w2[:]
                    update_window = True
                    break
                if len(w2) == 0:
                    end_loop = True
        return update_window