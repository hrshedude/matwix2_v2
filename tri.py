import skimage
import cv2
import matplotlib.pyplot as plt
import numpy as np
import imgtoolscustum as imtc
import os
import random
from collections import Counter
import scipy

fold_path = "sym_data"
img_path = f"{fold_path}/{random.choice(os.listdir(fold_path))}"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (60,50))
img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)[1]
img = ~img
img = img/255
img = img.astype(np.uint8)
# Now 1 is black 0 is white

img_sk = skimage.morphology.skeletonize(img)
img_sk = img_sk.astype(np.uint8)

def get_neighboured_img(skimg):
    res = np.zeros_like(skimg)
    for r, row in enumerate(skimg):
        for c, px in enumerate(row):

            if px ==1:
                neighbours_list = imtc.find_neighbour(skimg, (r,c), 1)
                res[r][c] = len(neighbours_list)
    return res

neighboured_img_sk = get_neighboured_img(img_sk)
neighboured_img = get_neighboured_img(img)

neighbour_info = Counter(neighboured_img.flatten())
print(neighbour_info)

def line_bw_furthest_points(nimg):

    # first point
    inds = np.where(nimg==1)

    f_ind = (inds[0][0],inds[1][0])
    l_ind = (inds[0][-1],inds[1][-1])

    res = np.zeros_like(nimg)
    line_coors = skimage.draw.line(*f_ind, *l_ind)
    res[*line_coors] = 1

    return res.astype(np.uint8)
ex_ln_img = line_bw_furthest_points(neighboured_img_sk)


img_dist = cv2.distanceTransform(img, cv2.DIST_L2, 5)

comb_img = (img_sk+img_dist).astype(np.uint8)

# comb_thresh = cv2.adaptiveThreshold(comb_img, 0,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1)
def rmv_lwst_val(nimg):

    __nimg = nimg.copy()
    __nimg[__nimg==0] = 255
    _min = np.min(__nimg)
    __nimg[__nimg==255] = 0
    print(_min)
    __nimg[__nimg == _min] = 0

    return __nimg 

def binarify_max_thresh(img):
    img[img!=0] = 1
    return img.astype(np.uint8)

def local_dimming(nimg):
    __nimg = nimg.copy()
    _max = np.max(__nimg)

    max_inds = __nimg[__nimg==_max]


r_img = rmv_lwst_val(comb_img)
r_img = get_neighboured_img(binarify_max_thresh(r_img))
dr_img = cv2.distanceTransform(r_img, cv2.DIST_L2, 5)



# plt.set_cmap('jet')
# plt.rcParams['image.cmap'] = 'Dark2'
# plt.rcParams['image.cmap'] = 'Greys
plt.rcParams['image.cmap'] = 'viridis'
imtc.show_subimgs_onRow([neighboured_img, neighboured_img_sk, img_dist, comb_img, r_img, dr_img])
