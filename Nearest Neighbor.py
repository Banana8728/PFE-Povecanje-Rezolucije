#Potrebno za import

#from __future__ import print_function
#from pylab import *
#
#from ipywidgets import interact, interactive, fixed, interact_manual
#import ipywidgets as widgets
#
#import skimage
#from skimage import *
#from skimage.color import *
#from skimage import io
#import numpy as np


def NearestNeighbor(img, scaleFac):

    #Rezolucija slike
    imgShape = img.shape
    widht = imgShape[0]
    height = imgShape[1]

    #Rezolucija nove slike
    widhtScaled  = int(widht * scaleFac)
    heightScaled  = int(height * scaleFac)

    #Menjanje faktora uvecavanja zbog boljeg prikaza
    scaleFac = (widhtScaled - 1) / (widht - 1)

    #Nisam nasao bolji nacin da napravim int matricu
    imgNew = np.random.randint( 5, size = (widhtScaled, heightScaled, 3) )

    #Za svaki pixel
    for j in range(0, heightScaled):
        for i in range(0, widhtScaled):

            #Koordinate tacke koja se racuna kada bi bila na originalnoj slici
            x = i/scaleFac
            y = j/scaleFac

            #4 tacke potrebne za izracunavanje
            x1 = int(x)
            x2 = x1 + 1
            y1 = int(y)
            y2 = y1 + 1

            #U slucaju da tacke izlaze iz okvira, sluze za matricu
            x2ind = x2
            y2ind = y2

            #Vracanje tih tacaka na manju vrednost zbog matrice
            if x2 >= widht:
                x2ind = x2-1
            if y2 >= height:
                y2ind = y2-1

            #Glavno izracunavanje 
            if x - x1 < 0.5 :
                if y - y1 < 0.5:
                    newPix = img[x1, y1]
                else:
                    newPix = img[x1, y2ind]
            else:
                if y - y1 < 0.5:
                    newPix = img[x2ind, y1]
                else:
                    newPix = img[x2ind, y2ind]
            
            #Izgleda da je glupo, ali nekad PNG ima 4 stvari umesto 3 (za boje)
            imgNew[i, j, 0] = newPix[0]
            imgNew[i, j, 1] = newPix[1]
            imgNew[i, j, 2] = newPix[2]         

    return imgNew