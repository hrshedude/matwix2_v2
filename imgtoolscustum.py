import PIL.Image
import numpy as np
import matplotlib.pyplot as plt



def find_neighbour(img, index, to_detect =1): 
    
    row,col = index
    rowshape,colshape = img.shape
    neighbour_list = []
    
    # 8 possiblities
    
    # top left
    if row > 0 and col > 0 and  img[row-1, col-1] == to_detect:
        neighbour_list.append((row-1, col-1))
    else:pass
    
    # top middle
    if row > 0 and img[row-1, col] == to_detect:
        neighbour_list.append((row-1, col))
    else:pass
    
    # top right
    if row > 0 and col < colshape-1 and  img[row-1, col+1] == to_detect:
        neighbour_list.append((row-1, col+1))
    else:pass
    
    
    # middle left
    if col > 0 and  img[row, col-1] == to_detect:
        neighbour_list.append((row, col-1))
    else:pass
    
        # middle right
    if col < colshape-1 and  img[row, col+1] == to_detect:
        neighbour_list.append((row, col+1))
    else:pass
        
    
    # bottom left
    if row<rowshape-1 and col > 0 and  img[row+1, col-1] == to_detect:
        neighbour_list.append((row+1, col-1))
    else:pass
    
    # bottom middle
    if row<rowshape-1 and  img[row+1, col] == to_detect:
        neighbour_list.append((row+1, col))
    else:pass
    
    # bottom right
    if row<rowshape-1 and col < colshape-1 and  img[row+1, col+1] == to_detect:
        neighbour_list.append((row+1, col+1))
    else:pass
    

    return neighbour_list



def find_all_neighbours(img, points):   # need extra func cuz wierd behaviour in looped updating list
    # get neighbour of each in list
    
    extra = set()
    
    for item_index in points:
        extra = extra.union(find_neighbour(img, item_index))

    return extra # extra points found



def find_extra_lv3(img, extra_points_lv2, extra_points_lv1): # neatness

    extra_points_lv3 = find_all_neighbours(img, extra_points_lv2)
    extra_points_lv3 = extra_points_lv3.difference(extra_points_lv2).difference(extra_points_lv1)

    return extra_points_lv3



def show_points_onImg(img_og, points_list, special_point = None, vals=None, sval = None, cmap = "Spectral"):
      
    img = img_og.copy()
    
    if vals == None:
        vals = range(2, len(points_list)+2)
    else:
        pass
    
    if sval == None:
        sval = len(points_list) +3
        
    
    for val,points in zip(vals,points_list):
        for point in points:
    
            img[*point] = val
    
    if special_point != None:
        img[*special_point] = sval
    else:
        pass
    
    # Accent_r , OrRd
    plt.imshow(img*1, cmap=cmap) 
    plt.colorbar()
    plt.show()




def indsort(l): # L2R
    
    return sorted(l, key=lambda i: i[0]*100 + i[1])
    
    


def find_all_islands(img):

    xshape, yshape = img.shape

    
    all_islands = []

    for rowno in range(xshape):
        
        for colno in range(yshape):
            
            if img[rowno, colno] == 1 and not any((rowno, colno) in island for island in all_islands):
                
                current_index = (rowno, colno)
                all_neighbours = set([current_index])
                
    
                current_neighbours = set(find_neighbour(img, current_index))
                all_neighbours = all_neighbours.union(current_neighbours)
                

                nearby_points = find_all_neighbours(img, current_neighbours)
                nearby_points = nearby_points.difference(current_neighbours)
                all_neighbours = all_neighbours.union(nearby_points)
                

                
                extra_points_lv1 = current_neighbours.copy()
                extra_points_lv2 = nearby_points.copy()
                extra_points_lv3 = [None]
                
                cont = True
                while cont: 
                    
                    # print(f"in loop : lv3= {extra_points_lv3}")
                    extra_points_lv3 = find_extra_lv3(img, extra_points_lv2, extra_points_lv1)
                    all_neighbours = all_neighbours.union(extra_points_lv3)
                    
                    if extra_points_lv3 == set():
                        # print("HURRA")
                        cont = False
                        break
                    else:
                        pass
                    
                    extra_points_lv1 = extra_points_lv2
                    extra_points_lv2 = extra_points_lv3
                    
                all_islands.append(all_neighbours)
                    
                

            

    return all_islands


def convert_img_2bw(img, slack=0.5): # grayscale inverse
    
    img = np.array(img)

    img = img/255
    img[img>=slack] = 1
    img[img<slack] = 0
    img = (img-1) *-1
    img = img.astype(np.uint8)
    
    return img


def get_blob_info(blob):
    
    top = min(blob, key=lambda i: i[0])[0]
    bottom = max(blob, key=lambda i: i[0])[0]
    left = min(blob, key=lambda i: i[1])[1]
    right = max(blob, key=lambda i: i[1])[1]

    height = bottom-top
    width = right-left
    
    return ((height, width), (top, bottom, left, right))
    
    
def blob2img(blob, padding=3):
    
    (height, width), (top,bottom, left, right) = get_blob_info(blob)
    
    subimg = np.zeros((height+ 1+ padding*2, width+ 1+padding*2))
    
    for index in blob:
        
        subimg[index[0] - top + padding][index[1] - left + padding] = 1

    return subimg


def show_subimgs_onRow(subimgs, savet=False):
    fig = plt.figure(figsize=(8, 8))

    columns = len(subimgs)
    rows=1
    for i,subimg in zip(range(1, columns*rows +1), subimgs):
        
        ax = fig.add_subplot(rows, columns, i)
        ax.set_title(str(i))
        plt.imshow(subimg)
        plt.yticks([])
        plt.xticks([])
    plt.colorbar()
    if savet==False:
        plt.show()
    else:
        plt.savefig(savet, dpi=600)
    


def split_img(img):
    
    """
    splits image into subimgs based on islands
    * removes same reigon duplicates
    """
    
    segments = find_all_islands(img)


    segments = sorted(segments, key= lambda i: min(i, key=lambda ind: ind[1])[1]) # sort based on top left corner


    subimgs = [blob2img(blob) for blob in segments]

    return subimgs




def split_img_woDuplicate(img, padding=3):

    """
    split imgs into subimgs while removing duplicates from the same region
    """

    segments = find_all_islands(img)
    segments = sorted(segments, key= lambda i: min(i, key=lambda ind: ind[1])[1]) # sort based on top left corner
    subimgs = [blob2img(blob) for blob in segments]


    # remove same region duplicates
    prev_subimg_ = subimgs[0]
    for sn, subimg in enumerate(subimgs[1:], start=1):
        
        
        blob1_info = get_blob_info(segments[sn-1])
        blob2_info = get_blob_info(segments[sn])
            
        # if np.array_equal(prev_subimg_,subimg):
        if blob1_info[1][2] == blob2_info[1][2] and blob1_info[1][3] == blob2_info[1][3]: # same left & right
            
            
            # print("HIT",sn)

            ntop = blob1_info[1][0]
            nbottom = blob2_info[1][1]
            nleft = blob1_info[1][2]   #since same selft right shuld be same for both ?
            nright = blob2_info[1][3]
            
            
            # print(blob1_info)
            # print(blob2_info)
            # print(ntop, nbottom, nleft, nright)
        
            nheight = nbottom -ntop
            nwidth = nright-nleft
            
            # print(nheight, nwidth)
            
            new_subimg = np.zeros(( nheight + padding*2, nwidth + padding*2))
        
            for index in segments[sn].union(segments[sn-1]):
                
                new_subimg[index[0] - ntop + padding][index[1] - nleft + padding] = 1
            

            try:
                subimgs[sn] = new_subimg
                subimgs.pop(sn-1)
            except:
                print(sn)
                break
            
        else:
            pass
        
        
        prev_subimg_ = subimg
        
    
    return subimgs        
        
        
        
        
        
def combine_images_row(images):
    """
    WARNING USES PIL OUTPUT IS PIL ASWELL
    """
    
    images = [PIL.Image.fromarray(img) for img in images]

    total_width = sum(image.width for image in images)
    max_height = max(image.height for image in images)

    combined_image = PIL.Image.new('RGB', (total_width+(5*len(images))+5, max_height), color=(255,255,0))

    x_offset = 5
    for image in images:
        combined_image.paste(image, (x_offset, 0))
        x_offset += image.width+5

    return combined_image


# img = np.array(
#     [
#         [1,1,0,0,0],
#         [0,1,0,0,0],
#         [0,0,1,0,0],
#         [0,0,0,1,0],
#         [0,1,1,1,1]
        
#     ]
# )

# all_islands = find_all_islands(img)

# plt.imshow(img, cmap="binary")
# plt.show()
# show_points_onImg(img,all_islands, cmap="Spectral")