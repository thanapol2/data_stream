import math

import numpy as np

from skmultiflow.drift_detection.base_drift_detector import BaseDriftDetector

"""
ref : https://scikit-multiflow.github.io/
"""

class chebyshev_base(BaseDriftDetector):

    MAX_BUCKETS = 5

    def __init__(self, max_window = 500, min_size = 100, k=3):
        super().__init__()
        self.window = []
        self.sample_count = None
        self._width = 0
        self.k = k
        self._total = None
        # self._mean = None
        self._variance = None
        self.max_size = max_window
        self.min_size = min_size
        # self.warning_level = warning_level
        # self.out_control_level = out_control_level
        self.count_detect = 0
        self.reset()

    def reset(self):
        """ reset

        Resets the change detector parameters.

        """
        super().reset()
        self.sample_count = 1
        # self.mean = 1.0
        self._total = 0.0
        self._variance = 0.0
        self._width = 0
        self.window = []

    def get_count(self):
        return (self.count_detect)

    def add_element(self, value):
        bln_change = False
        self.window.append(value)
        mean = sum(self.window) / len(self.window)
        variance = np.std(self.window)
        if abs(value - mean) > self.k * variance:
            bln_change = True
        # self._width += 1
        if len(self.window) >= self.max_size:
            self.window.pop(0)
        self.in_concept_change = bln_change
        return bln_change