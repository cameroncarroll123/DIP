# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:26:42 2020

@author: Cameron
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open('C:/Users/Cameron/Documents/Code/Images/frog.bmp'))

# Display original image
plt.figure()
plt.imshow(img,cmap='gray')

# L is number of grayscale values
L = 256

# Allocate memory for histogram variables
h = np.zeros(L)
h2 = np.zeros(L)

# Calculate and plot historgram values
vals, count = np.unique(img, return_counts=True)
h[vals] = count

plt.figure()
plt.bar(range(np.size(h)),h)

# Calculate and plot cumulative distribution function (cdf) of histogram 
cdf = np.cumsum(h)

plt.figure()
plt.plot(cdf)

# General histogram equalization formula from wikipedia (towards the bottom)
cdfMin = np.min(cdf)
MxN = img.size
equImg = np.round(((cdf[img]-cdfMin)/(MxN - cdfMin))*(L-1)).astype(int)

# Display equalized image
plt.figure()
plt.imshow(equImg, cmap='gray')

# Calculate and plot historgram values
vals2, count2 = np.unique(equImg,return_counts=True)
h2[vals2] = count2

plt.figure()
plt.bar(range(np.size(h2)),h2)

# Calculate and plot cumulative distribution function (cdf) of histogram 
cdf2 = np.cumsum(h2)

plt.figure()
plt.plot(cdf2)