# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 09:06:25 2020

@author: Cameron

Functions for creating Bayer matrices and Bayer matrix images
"""

import numpy as np
import math

# General recursive function to create Bayer matrices
def recurBayer(m):
  blockLen = int(math.sqrt(m.size))
  matLen = blockLen*2
  
  m = m*4
  b = np.ones((matLen,matLen))
  
  b[0:blockLen,0:blockLen] = m + 1
  b[0:blockLen,blockLen:2*blockLen] = m + 2
  b[blockLen:2*blockLen,0:blockLen] = m + 3
  b[blockLen:2*blockLen,blockLen:2*blockLen] = m
  
  return b

# Input the length of the matrix to be created (must be a power of 2)
def bayer(n):
  if math.ceil(math.log(n,2)) == math.floor(math.log(n,2)):
    # 2x2 Bayer matrix used for recursive function
    m = np.array([[1,2],[3,0]])
    
    if n == 2: 
      return m
    
    else:
      for i in range(int(math.log(n,2)-1)):
        m = recurBayer(m)
        
    return m
  
  else:
    raise ValueError("Invalid input.  Must be a power of 2.")

# Create Bayer Image the size of image dithering is being performed on
def bayerImg(m,r,c):
  mapR, mapC = m.shape
  
  if r % mapR != 0 or c % mapC != 0:
    raise ValueError("Image size must be divisible by map size")
    
  numRMaps = int(r/mapR)
  numCMaps = int(c/mapC)
  
  # Create first Column of Bayer image (width of index matrix)
  colImg = m.copy()
  for i in range(numRMaps-1):
    colImg = np.vstack((colImg,m))
  
  # Copy columns along rows to complete Bayer image
  img = colImg.copy()
  for i in range(numCMaps-1):
    img = np.hstack((colImg,img))
  return img
