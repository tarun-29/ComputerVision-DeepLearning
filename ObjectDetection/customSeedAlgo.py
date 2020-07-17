import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

road = cv2.imread("../DATA/road_image.jpg")
road_copy = np.copy(road)
marker_image = np.zeros(road.shape[:2], dtype=np.int32)
segments = np.zeros(road.shape,dtype=np.int8)

n_markers = 10
current_marker = 1
marks_updated = False

def create_rgb(i):
    return tuple(np.array(cm.tab10(0)[:3])*255)

def mouse_callback(event, x, y, flags, param):
    global marks_updated

    if event==cv2.EVENT_LBUTTONDOWN :
        #markers passed to the watershed algo
        cv2.circle(marker_image,(x,y),10,(current_marker), -1)

        #user sees on the road image
        cv2.circle(road_copy, (x,y), 10, colors[current_marker], -1)

        marks_updated =  True

colors = []
for i in range(10):
    colors.append(create_rgb(i))


#while TRUE 
cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image', mouse_callback)

while True:

    cv2.imshow('Watershed Segments', segments)
    cv2.imshow('Road Image', road_copy)

    #CLose all window
    k = cv2.waitKey(1)
    if k == 27 :
        break

    #clear all the colors
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2], dtype=np.int32)
        segments = np.zeros(road.shape, dtype=np.uint8)

    #update color choice
    elif k>0 and chr(k).isdigit() :
        current_marker = int(chr(k))

    #update the markings
    if marks_updated : 
        marker_image_copy = marker_image.copy()
        cv2.watershed(road, marker_image_copy)

        segments = np.zeros(road.shape, dtype=np.uint8)

        for color_ind in range(n_markers):
            #coloring segment numpy call
            segments[marker_image_copy == (color_ind)] = colors[color_ind]