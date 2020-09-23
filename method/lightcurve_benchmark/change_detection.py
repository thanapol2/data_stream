from chebyshev_adwin import chebyshev_adwin as chebyshev

class change_detection():

    def __init__(self,method_type="0",test_list=[],answer="",start_end=[]):
        self.reset()
        self.method_type = method_type
        self.test_list = test_list
        self.answer = answer
        self.start_end = start_end
        self.index_change_point = []
        self.isnot_count = True
        self.count_found = 0

    def reset(self):
        self.method_type = ""
        self.test_list = []
        self.answer = ""
        self.start_end = []
        self.index_change_point = []
        self.isnot_count = True
        self.count_found = 0

    def compute_change(self,cheb_windows_size,k):
        cheb_ineq = chebyshev(max_size=cheb_windows_size, k=k)
        for i in range(len(self.test_list)):
            cheb_ineq.add_element(self.test_list[i])
            if cheb_ineq.detected_change():
                self.index_change_point.append(i)
        print(self.index_change_point)
        self.isnot_count = True

    def get_tran_found(self):
        if self.isnot_count:
            self.count_found = 0
            for i in self.start_end:
                start = i[0]
                end = i[1]
                for change_point in self.index_change_point:
                    if (change_point >= start) & (change_point<=end):
                        self.count_found = self.count_found + 1
            self.isnot_count = False
        return self.count_found

    def get_false_count(self):
        if self.isnot_count:
            self.get_tranfound()
        false_count = len(self.index_change_point) - self.count_found
        return false_count