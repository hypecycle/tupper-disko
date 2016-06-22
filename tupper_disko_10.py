# -*- coding: utf-8 -*-
import cv2
import sys
import time
from sklearn.cluster import KMeans
import argparse
import utils
from qhue import Bridge # Hue Bridge handling

#based on mainc03.py

# construct  argument parser and parse 
ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-c", "--clusters", required = True, type = int,
	help = "# of clusters")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

# Starting qhue
probierstube = Bridge("192.168.104.112", "2897756c17c8c8b257343a121ee17d7") #Bridge handling


while True:

    ret, frame = cap.read() # Capture frame-by-frame
    img = frame
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    print(time.strftime("%H:%M:%S"))


    # reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))


    # cluster the pixel intensities
    clt = KMeans(n_clusters = args["clusters"])
    
    #print("Mark")
    clt.fit(image)

    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = utils.centroid_histogram(clt)
    values = utils.plot_colors(hist, clt.cluster_centers_)

    print("Return")

    for (h, s, v) in values:
        print(h,s,v)
        #probierstube.lights(i, 'state', bri=v, hue=h, sat=s)

    #cv2.cv.Flip(frame, None, 1)
    #cv2.imshow('Tupper-Disko', frame)
    c = cv2.cv.WaitKey(7) % 0x100
    if c == 27:
        print("esc")
        break

cap.release()
cv2.destroyAllWindows()
    
print 'exit'
stopFlag.set()   
