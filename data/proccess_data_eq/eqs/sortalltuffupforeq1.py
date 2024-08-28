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


mdpath = "C:/Users/senlab4/codesali/schoolstuff/prac/gitstuff/matwix2/aipart/datapart/datasets/setEQSPLIT/"

# symbs = "1234567890+-/*=()"
symbs = ["1","2","3","4","5","6","7","8","9","0","+","-","[divideforward]","[multiply]","=","(", ")"]
symbs.extend("abcdefghijklmnopqrstuvwxyz")

tmppath = "C:/Users/senlab4/codesali/schoolstuff/prac/gitstuff/matwix2/aipart/datapart/datasets/tmp/"

for symb in symbs:
    os.mkdir(mdpath+"val_"+symb)

img_whole_name_list = os.listdir(tmppath)


for img_whole_name_og in img_whole_name_list:
    
    img_whole_name = img_whole_name_og.split("_")[1]
    img_whole_name = img_whole_name.replace("[multiply]", "*").replace("[divideforward]", "/")
    # img_whole_name = list(img_whole_name)
    img_whole_name = [i if i != "*" else "[multiply]" for i in img_whole_name]
    img_whole_name = [i if i != "/" else "[divideforward]" for i in img_whole_name]
    
    
    # print(img_whole_name)
    
    og_img = PIL.Image.open(tmppath+img_whole_name_og).convert('L')
    
    img = imgtools.convert_img_2bw(og_img, 0.7)
    subimgs = imgtools.split_img_woDuplicate(img)

    subimgs = [subimg for subimg in subimgs if subimg.size > 100]
    
    
    if len(subimgs) == len(img_whole_name):
        
            
        for s, (imgname, subimg) in enumerate(zip(img_whole_name,subimgs)):
            
            img = PIL.Image.fromarray((((subimg -1)*-1)*255).astype(np.uint8))
            
            sn = len(os.listdir(f"{mdpath}val_{imgname}/")) + 1
            
            savepath = f"{mdpath}val_{imgname}/img_{sn}.png"
            
            
            img.save(savepath)
            
        print(img_whole_name)
        
    else:
        print("miss ", len(subimgs) - len(img_whole_name), img_whole_name)
        
        
            
    
    
    
    

    
