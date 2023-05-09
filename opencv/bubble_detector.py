import cv2
from data import data



def bubble_parse(fileIndex, image):

    col = data[fileIndex]['col']
    bubble = data[fileIndex]['bubble']
    minR = data[fileIndex]['minR']
    maxR = data[fileIndex]['maxR']


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,27,3)
    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]


    # Calculating unit
    minX = 10000
    maxX = 0
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        minX = min(x, minX)
        maxX = max(x, maxX)

    unit = (maxX - minX) / 100


    # Correcting the columns
    for colIndex in range(len(col)):
        for oneCol in range(col[colIndex] - 10, col[colIndex] + 10):
            count = 0
            for c in cnts:
                x, y, w, h = cv2.boundingRect(c)
                ratio = w/h
                ((x, y), r) = cv2.minEnclosingCircle(c)
                x /= unit
                y /= unit
                r /= unit

                if minR <= r <= maxR and ratio > 1 and round(x) == oneCol and y > 20:
                    # cv2.circle(image, (int(x * unit), int(y * unit)), int(r * unit), (36, 255, 12), -1)
                    count+=1
        
            if count >= bubble[colIndex]:
                col[colIndex] = oneCol
                # print("Adjusted Column: " + str(col[colIndex]))
        

    # Detecting the bubbles
    for oneCol in col:
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            ratio = w/h
            ((x, y), r) = cv2.minEnclosingCircle(c)
            x /= unit
            y /= unit
            r /= unit

            if minR <= r <= maxR and ratio > 1 and round(x) == oneCol and y > 20:
                cv2.circle(image, (int(x * unit), int(y * unit)), int(r * unit), (36, 255, 12), -1)


    return image


