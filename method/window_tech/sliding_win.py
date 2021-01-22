import statistics

class sliding_win():
    def __init__(self, size=100,start_mean = 100,start_variance=400):
        self.reset()
        self._size = size
        self._window = []
        self._variance = start_variance
        self._mean = start_mean

    def reset(self):
        self._size = 0
        self._window = []
        self._variance = 400
        self._mean = 100

    def append(self,data):
        if self._window:
            if len(self._window)>self._size:
                self._window.pop()
        self._window.append(data)

    def get_mean(self):
        mean = self._mean
        if self._window:
            mean = statistics.mean(self._window)
        return mean

    def get_variance(self):
        variance = self._variance
        if len(self._window)>2:
            variance = statistics.variance(self._window)
        return variance

    def get_last_value(self):
        var = 0
        if self._window:
            var = var[-1]
        return var