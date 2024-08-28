from PIL import Image
import os
import numpy as np
import cv2

kernel = np.ones((3,3),np.uint8)

def img_forms(mspath, imgname, mdpath):

    img = cv2.imread(mspath+imgname)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(img,150,200)
    imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
    imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

    imgn = imgname.replace(".png","_")
    cv2.imwrite(f"{mdpath}{imgn}raw.png",img)
    cv2.imwrite(f"{mdpath}{imgn}gray.png",imgGray)
    cv2.imwrite(f"{mdpath}{imgn}canny.png",imgCanny)
    cv2.imwrite(f"{mdpath}{imgn}dil.png",imgDialation )
    cv2.imwrite(f"{mdpath}{imgn}ero.png",imgEroded)
    # return (img, imgGray, imgCanny, imgDialation, imgEroded)


mspath = "C:/Users/alima/OneDrive/Documents/GitHub/Ai-proj-mthsymb/aipart/data/htmlsynthdata_sym_raw/"
mdpath = "C:/Users/alima/OneDrive/Documents/GitHub/Ai-proj-mthsymb/aipart/data/htmlsynthdata_sym_ripe/"

sfolds = os.listdir(mspath)
sfolds.remove("ZZZZZallstuff")

for fold in sfolds:
    
    for fle in os.listdir(mspath+fold):

        print(fold, fle)
        print(mspath+fold+'/', fle, mdpath+fold+'/')
        img_forms(mspath+fold+'/', fle, mdpath+fold+'/')
        print()

