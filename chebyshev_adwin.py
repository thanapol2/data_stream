import numpy as np

from skmultiflow.drift_detection.base_drift_detector import BaseDriftDetector


class chebyshev_adwin(BaseDriftDetector):

    def __init__(self, max_size = 200 , min_size = 100, warning_level=2.0, out_control_level=3.0):
        super().__init__()
        self.sample_count = None
        self._width = 0
        self.k = None
        self._total = None
        # self._mean = None
        self._variance = None
        self.max_size = max_size
        self.min_size = min_size
        self.warning_level = warning_level
        self.out_control_level = out_control_level
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


    def add_element(self, value):
        self._width += 1
        self.__insert_element_bucket(0, value, self.list_row_bucket.first)

        incremental_variance = 0

        if self._width > 1:
            incremental_variance = (self._width - 1) * (value - self._total / (self._width - 1)) * \
                                   (value - self._total / (self._width - 1)) / self._width

        self._variance += incremental_variance
        self._total += value

    