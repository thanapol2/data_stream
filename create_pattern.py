
class create_pattern():

    HIGH = 10
    LOW = 0

    def __init__(self,range_size=5000):
        self.LOW = 0
        self.HIGH = 10
        self.RANGE_SIZE = range_size

    def reset(self):
        self.__init__()

    def invest(self,invest=False):
        if(invest):
            self.reset()
            temp = self.LOW
            self.LOW = self.HIGH
            self.HIGH = temp
        else:
            self.reset()
        print('LOW ',self.LOW)
        print('High ',self.HIGH)


    def get_data(type=1,range_size=5000):
        data = []
        return data


    def sudden_gen(self,number_peak=2):
        data_stream = []
        point_change = int((self.RANGE_SIZE-800)/number_peak)
        print(point_change)
        data = self.LOW
        for i in range(self.RANGE_SIZE):
            if ((i%point_change==0)&(i!=0)):
                if data == self.LOW:
                    data = self.HIGH
                else:
                    data = self.LOW
            data_stream.append(data)
        self.reset()
        return data_stream

    def incremental(self,range_curve = 1000):
        data_stream = []
        data = self.LOW
        slope = self.HIGH/range_curve
        start_curve = int((self.RANGE_SIZE/2) - (range_curve/2))
        end_curve = int((self.RANGE_SIZE/2) + (range_curve/2))
        for i in range(start_curve):
            data_stream.append(data)
        for i in range(start_curve,end_curve):
            data = data + slope
            data_stream.append(data)
        for i in range(end_curve,self.RANGE_SIZE):
            data_stream.append(data)
        self.reset()
        return data_stream