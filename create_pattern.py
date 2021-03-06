import random

class pattern():

    HIGH = 10
    LOW = 0

    def __init__(self,range_size=5000):
        self.LOW = 1
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

    def create(self,type):
        data_stream = []
        file_name = ''
        if(type=='S'):
            data_stream = self.sudden_gen()
            file_name = 'sudden'
        elif(type=='I'):
            data_stream = self.incremental()
            file_name = 'incremental'
        elif(type=='R'):
            data_stream = self.reoccuring_concept()
            file_name = 'reoccuring concept'
        elif(type=='G'):
            data_stream = self.gradual()
            file_name = 'gradual concept'
        return data_stream,file_name

    def sudden_gen(self):
        data_stream = []
        point_change = int((self.RANGE_SIZE-800)/2)
        print(point_change)
        data = self.LOW
        for i in range(self.RANGE_SIZE):
            if(i>=point_change):
                data = self.HIGH
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

    def gradual(self,start_pulse=2000,end_pulse=2400,size_per_pulse=5):
        data_stream = []
        print(end_pulse)
        data = self.LOW
        counter = 0
        for i in range(self.RANGE_SIZE):
            if (start_pulse<i)&(i<end_pulse):
                if (counter==0):
                    if(random.randrange(2)==0):
                        data = self.LOW
                    else:
                        data = self.HIGH
                    counter = counter + 1
                elif (counter==size_per_pulse):
                    counter=0
                else:
                    counter = counter + 1
            elif (i >= end_pulse):
                data = self.HIGH
            data_stream.append(data)
        self.reset()
        return data_stream

    def reoccuring_concept(self,number_peak=2):
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