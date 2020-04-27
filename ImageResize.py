# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:20:42 2020

@author: Cameron

Image resizing
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d
import math
# Load image from file
img = np.array(Image.open('C:/Users/Cameron/Documents/Code/Images/bluejay.bmp'))
plt.figure()
plt.imshow(img,cmap="gray")

ratioR = 2
ratioC = 2

oldR, oldC = img.shape

# oldR = 2
# oldC = 2

newR = math.floor(ratioR * oldR)
newC = math.floor(ratioC* oldC)

# newImg = np.zeros((newR,newC))

stepR = (newR-1) / oldR
startR = stepR / 2

stepC = (newC-1) / oldC
startC = stepC / 2

# gridX, gridY = np.meshgrid(range(newR),range(newC))

meshVecR = np.arange(startR, newR, stepR)[:oldR]
meshVecC = np.arange(startC, newC, stepC)[:oldC]


# gridR, gridC = np.meshgrid(meshVecR, meshVecC)

# newImg = griddata(gridR, gridC, (gridX, gridY), method='cubic')
linImgFunc = interp2d(meshVecC,meshVecR,img, kind='linear')
linNewImg = linImgFunc(range(newC),range(newR))

cubImgFunc = interp2d(meshVecC,meshVecR,img, kind='cubic')
cubNewImg = cubImgFunc(range(newC),range(newR))

plt.figure()
plt.imshow(linNewImg,cmap="gray")
plt.figure()
plt.imshow(cubNewImg,cmap="gray")
plt.figure()
plt.imshow(np.abs(linNewImg - cubNewImg),cmap='gray')
