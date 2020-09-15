import numpy as np
import statistics
from skmultiflow.drift_detection.base_drift_detector import BaseDriftDetector


class dm_ver1(BaseDriftDetector):

    def __init__(self,k=3,decision_size=4,expectation_rate = 0.25):
        self.decision_window = []
        # self.prior_window = []
        self.reset()
        self.k = k
        self.count_detect = 0
        self.decision_size = decision_size
        # self.prior_size = prior_size
        self.expectation_rate = expectation_rate


    def reset(self):
        super().reset()
        self.decision_window = []

    def get_count(self):
        return (self.count_detect)

    def add_element(self, new_decision):
        bln_change = False
        count_true = 0
        if new_decision:
            self.decision_window(new_decision)
            if (len(self.decision_window) == self.decision_size):
                self.decision_window.pop(0)
            for is_change in self.decision_window:
                if is_change:
                    count_true = count_true + 1
            true_rate = float(count_true)/float(self.decision_size)
            if true_rate >= self.expectation_rate:
                bln_change = True
        self.in_concept_change = bln_change
        return bln_change
