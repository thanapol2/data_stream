import numpy as np
import statistics
from skmultiflow.drift_detection.base_drift_detector import BaseDriftDetector


class binning():
    def __init__(self, bin_period=10):
        self.is_full = False
        self.bin_period = bin_period
        self.bin = []

    def rest(self):
        self.bin_period = 0
        self.bin = []

    def reset_bin(self):
        self.bin = []

    def get_bin(self):
        return self.bin

    def add_instance(self,instance):
        if not self.can_add_bin():
            self.bin.append(instance)
        return(self.can_add_bin())

    def can_add_bin(self):
        return not self.is_full()

    def is_full(self):
        self.is_full = False
        if (len(self.bin) % self.bin_period) == 0:
            self.is_full = True
        return self.is_full