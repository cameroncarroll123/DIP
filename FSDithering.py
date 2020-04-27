# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:17:48 2020

@author: Cameron

Floyd-Steinberg dithering
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load image from file
img = np.array(Image.open('C:/Users/Cameron/Documents/Code/Images/frog.bmp'))
plt.figure()
plt.imshow(img,cmap="gray")


# Set threshold (higher the number the darker the resulting dithImg) and 
# make range of image from 0 to 1
thresh = .9
img = img/255

# Allocate memory
rows, cols = img.shape
newImg = np.zeros((rows, cols))

# Add a blank row and column to image because the algo accesses img(r+1,c+1)
zRow = np.zeros((1,cols))
zCol = np.zeros((rows+1,1))
img = np.vstack((img,zRow))
img = np.hstack((img,zCol))

# Loop through each pixel and compare to thersh then change pixels in original
# image based on the difference (error) between the new pixel value and the
# old pixel value.
for r in range(rows):
  for c in range(cols):
    oldPix = img[r,c]
    
    if oldPix < thresh: 
      newPix = 0
    else: 
      newPix = 1
    
    newImg[r,c] = newPix
    error = oldPix - newPix
    img[r+1,c] = img[r+1,c] + 7/16 * error
    if r > 1: img[r-1,c+1] = img[r-1,c+1] + 3/16 * error
    img[r, c+1] = img[r,c+1] + 5/16 * error
    img[r+1,c+1] = img[r+1,c+1] + 1/16 * error

# Plot Floyd-Steinberg dithering
plt.figure()
plt.imshow(newImg,cmap='gray')