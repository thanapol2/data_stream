import matplotlib.pyplot as plt
import numpy as np
import os
from skmultiflow.drift_detection.adwin import ADWIN


def test_sim(input_stream,file_name):
    adwin = ADWIN()
    change_point=[]
    plt.plot(input_stream)

    f = open(os.path.join('results', file_name + ".txt"), "w+")
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
    plt.savefig(os.path.join('image', file_name + "_result.png"), aspect='auto', bbox_inches='tight', dpi=200)
    plt.show(aspect='auto')
    plt.show()

def test_sim_zoom (input_stream,file_name,zoom_start=0,zoom_end=5000,crop_size=0):
    adwin = ADWIN()
    change_point = []
    for i in range(len(input_stream)):
        adwin.add_element(input_stream[i])
        if adwin.detected_change():
            plt.axvline(i, color='r', linestyle='dashed')
            change_point.append(i)
        if zoom_start == 0:
            zoom_start = change_point[0]-100
        if zoom_end == 5000:
            zoom_end = change_point[-1]+100

    xi = list(range(zoom_start, zoom_end))
    plt.plot(xi, input_stream[zoom_start:zoom_end])
    plt.ylabel('value')
    plt.xlabel('Time')
    plt.savefig(os.path.join('image',file_name+"_zoom.png"), aspect='auto', bbox_inches='tight', dpi=200)
    plt.show()

    end_point_crop= change_point[0]+crop_size
    start_point_crop = change_point[0] - 100
    for i in change_point:
        if(i<=end_point_crop):
            plt.axvline(i, color='r', linestyle='dashed')
    crop_stream = input_stream[start_point_crop : end_point_crop]
    zoom_xi = list(range(start_point_crop, end_point_crop))
    plt.plot(zoom_xi,crop_stream)
    plt.ylabel('value')
    plt.xlabel('Time')
    fig = plt.gcf()
    fig.set_size_inches(10, 5.5)
    plt.savefig(os.path.join('image',file_name+ "_result_zoom.png"), aspect='auto', bbox_inches='tight', dpi=200)
    plt.show()
    return change_point

def test_sim_crop (input_stream,file_name,crop_size=0):
    adwin = ADWIN()
    change_point = []
    for i in range(len(input_stream)):
        adwin.add_element(input_stream[i])
        if adwin.detected_change():
            # plt.axvline(i, color='r', linestyle='dashed')
            change_point.append(i)

    end_point_crop= change_point[0]+crop_size
    start_point_crop = change_point[0] - 100
    for i in change_point:
        if(i<=end_point_crop):
            plt.axvline(i, color='r', linestyle='dashed')
    crop_stream = input_stream[start_point_crop : end_point_crop]
    zoom_xi = list(range(start_point_crop, end_point_crop))
    plt.plot(zoom_xi,crop_stream)
    plt.ylabel('value')
    plt.xlabel('Time')
    fig = plt.gcf()
    fig.set_size_inches(10, 5.5)
    plt.savefig(os.path.join('image',file_name+ "_result_zoom.png"), aspect='auto', bbox_inches='tight', dpi=200)
    plt.show()
    return change_point

def sim(input_stream,start_point=0):
    adwin = ADWIN(delta=.3)
    change_point = []
    for i in range(len(input_stream)):
        adwin.add_element(input_stream[i])
        if adwin.detected_change():
            # plt.axvline(i, color='r', linestyle='dashed')
            change_point.append(i+start_point)
            # print('Change detected in data: ' + str(input_stream[i]) + ' - at index: ' + str(i)+'\n\n')

    return change_point