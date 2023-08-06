#Potrebno za import

import numpy as np


def BiLinear(img, scaleFac):
    
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
                for k in range(0, 3):
                    fxy1 = (x2 - x) * img[x1, y1, k] + (x - x1) * img[x2ind, y1, k]
                    fxy2 = (x2 - x) * img[x1, y2ind, k] + (x - x1) * img[x2ind, y2ind, k]
                    imgNew[i, j, k] = int((y2 - y) * fxy1 + (y - y1) * fxy2)

    return imgNew