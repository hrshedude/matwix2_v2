import PIL.Image

import sys
import os

sys.path.insert(1, "C:/Users/senlab4/codesali/schoolstuff/prac/gitstuff/matwix2_v2/")
import helperlibs.imgtoolscustum as imgtools

import PIL
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint


og_img = PIL.Image.open('img_2)6433[multiply]8_goofrmv33.png').convert('L')
# og_img = PIL.Image.open(r'C:\Users\senlab4\codesali\schoolstuff\prac\gitstuff\matwix2\aipart\datapart\preprocessing\eqs\img_9=70[divideforward]7_goofrmv4.png').convert('L')



img = imgtools.convert_img_2bw(og_img, 0.5)


plt.imshow(img)
plt.show()

subimgs = imgtools.split_img_woDuplicate(img)


if len(subimgs) < 5:
    img = imgtools.convert_img_2bw(og_img, 0.01)
    plt.imshow(img)
    plt.show()
    subimgs = imgtools.split_img_woDuplicate(img)
    

imgtools.show_subimgs_onRow(subimgs)

    
    









