# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:12:09 2020

@author: Cameron

Ordered Dithering using Bayer matrix
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import BayerMatGen as bmg


img = np.array(Image.open('C:/Users/Cameron/Documents/Code/Images/frog.bmp'))
plt.figure()
plt.imshow(img,cmap="gray")

m = bmg.bayer(512)
r, c = img.shape
m = np.round(255*(m+.5)/m.size)

bayerImg = bmg.bayerImg(m, r, c)
dithImg = np.zeros((r,c))
dithImg[img>bayerImg] = 255

plt.figure()
plt.imshow(dithImg,cmap="gray")


