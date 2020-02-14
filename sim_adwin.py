import matplotlib.pyplot as plt
import numpy as np
from skmultiflow.drift_detection.adwin import ADWIN

def test_sim(input_stream,file_name='result',zoom=False,zoom_start=0,zoom_end=5000,range_zoom=0):
    adwin = ADWIN()
    change_point=[]
    plt.plot(input_stream)
    f = open("results/" + file_name + ".txt", "w+")
    for i in range(len(input_stream)):
        adwin.add_element(input_stream[i])
        if adwin.detected_change():
            plt.axvline(i, color='r', linestyle='dashed')
            change_point.append(i)

            # print('Change detected in data: ' + str(input_stream[i]) + ' - at index: ' + str(i)+'\n\n')
            f.write('Change detected in data: ' + str(input_stream[i]) + ' - at index: ' + str(i)+'\n\n')
    f.close()
    plt.ylabel('value')
    plt.xlabel('Time')
    plt.savefig("images/"+file_name+"_result.png", aspect='auto', bbox_inches='tight', dpi=200)
    plt.show(aspect='auto')
    if(zoom):
        if zoom_start == 0:
            zoom_start = change_point[0]-100
        if zoom_end == 5000:
            if range_zoom ==0:
                zoom_end = change_point[-1]+100
            else:
                zoom_end = zoom_start+range_zoom
        xi = list(range(zoom_start, zoom_end))
        plt.plot(xi, input_stream[zoom_start:zoom_end])
        plt.ylabel('value')
        plt.xlabel('Time')
        plt.savefig("images/" + file_name + "_zoom.png", aspect='auto', bbox_inches='tight', dpi=200)
        for i in change_point:
            if(i<=zoom_end):
                plt.axvline(i, color='r', linestyle='dashed')
        plt.ylabel('value')
        plt.xlabel('Time')
        plt.savefig("images/"+file_name+"_result_zoom.png", aspect='auto', bbox_inches='tight', dpi=200)
        plt.show()