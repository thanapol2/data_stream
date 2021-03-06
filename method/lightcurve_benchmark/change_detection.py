from chebyshev_adwin import chebyshev_adwin as chebyshev
from method.dm_ver1 import dm_ver1 as dm_method


class change_detection():

    def __init__(self, method_type="0", test_list=[], answer="", start_end=[]):
        self.reset()
        self.method_type = method_type
        self.test_list = test_list
        self.answer = answer
        self.start_end = start_end
        self.index_change_point = []
        self.isnot_count = True
        self.count_found = 0
        self.tran_found = False

    def reset(self):
        self.method_type = ""
        self.test_list = []
        self.answer = ""
        self.start_end = []
        self.index_change_point = []
        self.isnot_count = True
        self.count_found = 0
        self.tran_found = False

    def get_change_points(self):
        return self.index_change_point

    def compute_change(self, cheb_windows_size, k):
        ineq = chebyshev(max_window=cheb_windows_size, k=k)
        if self.method_type == 2:  # dm
            dm = dm_method()
        for i in range(len(self.test_list)):
            ineq.add_element(self.test_list[i])
            if self.method_type == 0:  # dm
                if ineq.detected_change():
                    self.index_change_point.append(i)
            elif self.method_type == 2:
                dm.add_element(ineq.detected_change())
                if dm.detected_change():
                    self.index_change_point.append(i)
        print(self.index_change_point)
        self.isnot_count = True

    def get_true_count(self):
        if self.isnot_count:
            self.count_found = 0
            for i in self.start_end:
                start = i[0]
                end = i[1]
                for change_point in self.index_change_point:
                    if (change_point >= start) & (change_point <= end):
                        self.count_found = self.count_found + 1
                if self.count_found > 0:
                    self.tran_found = True
                else:
                    self.tran_found = False
            # self.isnot_count = False
        return self.count_found

    def get_tran_found(self):
        if self.isnot_count:
            self.get_true_count()
        return self.tran_found

    def get_false_count(self):
        if self.isnot_count:
            self.get_tran_found()
        false_count = len(self.index_change_point) - self.count_found
        return false_count
