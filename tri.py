import skimage
import cv2
import matplotlib.pyplot as plt
import numpy as np
import imgtoolscustum as imtc
import os
import random
from collections import Counter


fold_path = "sym_data"
img_path = f"{fold_path}/{random.choice(os.listdir(fold_path))}"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
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

neighboured_img = get_neighboured_img(img_sk)

neighbour_info = Counter(neighboured_img.flatten())
print(neighbour_info)

def line_bw_furthest_points(nimg):

    # first point
    inds = np.where(nimg==1)

    f_ind = (inds[0][0],inds[1][0])
    l_ind = (inds[0][-1],inds[1][-1])

    res = np.zeros_like(nimg)


ex_ln_img = line_bw_furthest_points(neighboured_img)

# plt.set_cmap('jet')
plt.rcParams['image.cmap'] = 'Dark2'
imtc.show_subimgs_onRow([img, img_sk, neighboured_img])
