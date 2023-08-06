#Potrebno za import

import numpy as np


def BiCubic(img, scaleFac):
    
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

                #Za lakse racunanje (sluzi za 16 tacaka)
                xn = np.zeros(4)
                yn = np.zeros(4)
                Y = np.zeros(4)
                
                #16 tacaka za izracunavanje
                xn[1] = int(x)
                xn[2] = xn[1] + 1
                xn[3] = xn[1] + 2
                xn[0] = xn[1] - 1

                yn[1] = int(y)
                yn[2] = yn[1] + 1
                yn[3] = yn[1] + 2
                yn[0] = yn[1] - 1

                #Vracanje na manju vrednost ako viri iz okvira slike
                if xn[2] >= widht:
                    xn[2] = xn[2]-1
                if xn[3] >= widht:
                    xn[3] = xn[2]
                if xn[0] < 0:
                    xn[0] = 0
                if yn[2] >= height:
                    yn[2] = yn[2]-1
                if yn[3] >= widht:
                    yn[3] = yn[2]
                if yn[0] < 0:
                    yn[0] = 0

                #Za izracunavanje
                xOff = x - xn[1]
                yOff = y - yn[1]

                #Sluzi za izracunavanje, koeficijenti za Catmull-Rom krive
                Q0x = (-xOff**3 + 2 * xOff**2 - xOff)/2
                Q1x = (3 * xOff**3 - 5 * xOff**2 + 2)/2
                Q2x = (-3 * xOff**3 + 4 * xOff**2 + xOff)/2
                Q3x = (xOff**3 - xOff**2)/2

                Q0y = (-yOff**3 + 2 * yOff**2 - yOff)/2
                Q1y = (3 * yOff**3 - 5 * yOff**2 + 2)/2
                Q2y = (-3 * yOff**3 + 4 * yOff**2 + yOff)/2
                Q3y = (yOff**3 - yOff**2)/2

                #Glavno izracunavanje
                for c in range (3):
                    for k in range (4):
                        Y[k] = img[int(xn[0]), int(yn[k]), c] * Q0x + img[int(xn[1]), int(yn[k]), c] * Q1x + img[int(xn[2]), int(yn[k]), c] * Q2x + img[int(xn[3]), int(yn[k]), c] * Q3x
                    imgNew[i, j, c] = int(Y[0] * Q0y + Y[1] * Q1y + Y[2] * Q2y + Y[3] * Q3y)
                

    return imgNew