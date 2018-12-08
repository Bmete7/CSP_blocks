# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:43:58 2018

@author: BurakBey
"""

import cv2
import sys
import constraint as csp
import numpy as np 

problem = csp.Problem()

array = np.zeros((6,8), dtype='int32')

array[5,0]= 1
array[5,1]= 1
array[5,2]= 1
array[5,3]= 1
array[5,6]= 1


array[4,1]= 1
array[4,3]= 1
array[4,6]= 1

array[3,1]= 1
array[3,3]= 1
array[3,6]= 1


array[2,1]= 1
array[2,2]= 1
array[2,3]= 1
array[2,4]= 1
array[2,5]= 1
array[2,6]= 1
array[2,7]= 1

array[1,1]= 1
array[1,2]= 1
array[1,3]= 1
array[1,4]= 1
array[1,5]= 1
array[1,6]= 1

array[0,3]= 1
array[0,4]= 1
array[0,5]= 1


h,w = array.shape
size = h*w
for i in range(h):
    for j in range(w):
        problem.addVariable(i*w + j, [array[i,j]])        


for i in range(h):
    for j in range(w):
        problem.addConstraint(lambda a,b: ((a==0) or (a/w == h-1) or (a==1 and a+w == 1) or (a==1 and a+w == 0 and ((a%w == 0 and a+1 == 1 and a+w+1 == 1) or (a-1 == 1 and a+w-1 == 1 and (( (a-1)%w != 0 and a-2==1) or (a-1%w==0 and a+1==1 and a+w+1 ==1))) ) and (a%w != w-1 and (a+1)%w != w-1 and a+1==1 and a+w+1 == 1 and a+2 == 1 and a+2+w == 1))), (i*w+j,1))

problem.getSolution()
problem._variables
problem._constraints

