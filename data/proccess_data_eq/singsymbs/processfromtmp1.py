import os
import shutil
from pprint import pprint

import sys

import PIL.Image
sys.path.insert(1, "C:/Users/senlab4/codesali/schoolstuff/prac/gitstuff/matwix2/")
import helperlibs.imgtoolscustum as imgtools

import PIL
import numpy as np
import matplotlib.pyplot as plt


mdpath = "C:/Users/senlab4/codesali/schoolstuff/prac/gitstuff/matwix2/aipart/datapart/datasets/setCOMBINED/"

symbs = "1234567890+-/*=()"
symbs = ["1","2","3","4","5","6","7","8","9","0","+","-","[divideforward]","[multiply]","=","(", ")"]


tmppath = "C:/Users/senlab4/codesali/schoolstuff/prac/gitstuff/matwix2/aipart/datapart/datasets/tmp/"


img_whole_name_list = os.listdir(tmppath)


for img_whole_name_og in img_whole_name_list:
    
    img_whole_name = img_whole_name_og.split("_")[1]
    # img_whole_name = img_whole_name.replace("[multiply]", "*").replace("[divideforward]", "/")
    # # img_whole_name = list(img_whole_name)
    # img_whole_name = [i if i != "*" else "[multiply]" for i in img_whole_name]
    # img_whole_name = [i if i != "/" else "[divideforward]" for i in img_whole_name]
    
    
    # print(img_whole_name)
    
    og_img = PIL.Image.open(tmppath+img_whole_name_og).convert('L')
    
    
    print(img_whole_name)
    
    img1 = imgtools.convert_img_2bw(og_img, 0.001)
    if not (img1==0).all() :
        img1 = imgtools.split_img_woDuplicate(img1)
    else:
        img1 = [None, None]
    
    img2 = imgtools.convert_img_2bw(og_img, 0.9)
    if not (img2==0).all() :
        img2 = imgtools.split_img_woDuplicate(img2)
    else:
        img2 = [None, None]
    
    img3 = imgtools.convert_img_2bw(og_img, 0.5)
    if not (img3==0).all() :
        img3 = imgtools.split_img_woDuplicate(img3)
    else:
        img3 = [None, None]
    
    imgs = [img1,img2,img3]

    for img in imgs:    
        
        if len(img) == 1:
            
            img = img[0]
            imgname = img_whole_name
            
            img = PIL.Image.fromarray((((img -1)*-1)*255).astype(np.uint8))
            
            sn = len(os.listdir(f"{mdpath}val_{imgname}/")) + 1
            
            savepath = f"{mdpath}val_{imgname}/img_{sn}.png"
            
            img.save(savepath)
                
            # print(img_whole_name)
            
        else:
            print("miss ", len(img) - 1, img_whole_name)
        
        
            
    
    
    
    

    
