import cv2


image = cv2.imread('./input.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,27,3)
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]


for c in cnts:
    area = cv2.contourArea(c)
    x,y,w,h = cv2.boundingRect(c)
    ratio = w/h
    ((x, y), r) = cv2.minEnclosingCircle(c)
    
		# Input1 - ESS_paper_ballot
    if r < 9 and r > 7 and ratio > 1.3 and ((x>400 and x<450) or (x>800 and x<830)) and y > 100:
        
		# Input2 - CHIL bubbleballot
    # if r < 100 and r > 10 and ratio > 1 and ((x<80) or (x>200 and x<300) or (x>500 and x<550)) and y > 200:
        
		# Input3 - ClearBallot_paper_ballot
    # if r < 15 and r > 10 and ratio > 1 and ((x>300 and x<400) or (x>700 and x<730)) and y > 200:
        
		# Input 4
    # if r < 25 and r > 22 and y > 200:
        
		# Input 5
    # if r < 25 and r > 15 and y > 450 and y < 1500 and ((x<100) or (x>700 and x<730)):
    	cv2.circle(image, (int(x), int(y)), int(r), (36, 255, 12), -1)


cv2.imwrite('output.png', image)

