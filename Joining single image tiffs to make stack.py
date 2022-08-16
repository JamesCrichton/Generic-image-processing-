# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:34:15 2022

@author: jcricht3
"""

#Make composite from Jen's single channel images
import os
from skimage import io
import numpy as np

dir1="//cmvm.datastore.ed.ac.uk/igmm/iadams-lab/Jen/Fluorescent images/Britemac/Zen/150822"
    
for r,d,f in os.walk(dir1):#makes a list for all files in each dir, so must be iterated over again
    img_files=[]#fresh list for each dir
    for i in f:
        if i.endswith(".tif"):                  
            img_files.append(i)
            
    if (len(img_files) == 3):#if there are three files in folder this is the 3channel image folder - assign to channels and make a stack
        for j in img_files:
            if "c0" in j:
                ch0_path=j
            if "c1" in j:
                ch1_path=j
            if "c2" in j:
                ch2_path=j
        
            

            
        
    
        