# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 00:26:58 2018

@author: BurakBey
"""

import numpy as np
import cv2
import sys

array =np.zeros((10,10), dtype='int32')
def savePoints(event,x,y,flags,param):
        
        if event == cv2.EVENT_LBUTTONDOWN:
            baseX = int(x/50)
            baseY = int(y/50)
            array[baseY,baseX] = 1
            baseX *= 50
            baseY *= 50
            for i in range(baseX, baseX+50):
                for j in range(baseY,baseY+50):
                    mat[j,i,0] = (30)
                    mat[j,i,1] = (30)
                    mat[j,i,2] = (230)
                    cv2.imshow('select',mat)
            
            
cv2.namedWindow('select')
cv2.setMouseCallback('select',savePoints)
mat = 255 * np.ones((650,550,3), dtype='uint8')
mat2 = mat.copy()
for i in range(11):
        cv2.line(mat, (i*50,0), (i*50,499), (5,5,5), 1, cv2.LINE_AA, 0)
        cv2.line(mat, (0,i*50), (499,i*50), (5,5,5), 1, cv2.LINE_AA, 0)

cv2.putText(mat,'Please select the building shape', 
    (5,555), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    1,
    (5,5,5),
    2)

cv2.putText(mat,'I will build it for you!', 
    (5,600), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    1,
    (5,5,5),
    2)



while(True):
    
    cv2.imshow('select', mat)
    k = cv2.waitKey(0)
    if k == 27:
        break
cv2.destroyAllWindows()
    