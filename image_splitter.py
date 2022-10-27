from matplotlib import image
from matplotlib import pyplot
import numpy as np
import pandas as pd
import random 

def split_img(np_arr, rand=False, axis=0, num_slices=40, n_pictures=1) -> list:
    """
    np_arr: np.array 
        of RGB picture, shape (x,y,3).
    rand: bool
         if slices should be randomized order.
    axis: int
         0 for x axis, 1 for y axis.
    num_slices: int
         how much slices should be made
    n_pictures: int 
        how much pictures should be returned
    """

    new_index = np.arange(0,np_arr.shape[axis],round(np_arr.shape[axis]/num_slices))
    new_slices = [(i,new_index[index+1]) for index, i in enumerate(new_index.tolist()) if index<new_index.shape[0]-1]
    if rand:
        random.shuffle(new_slices)
    if axis==0:
        new_arrs = [np_arr[slice[0]:slice[1]] for slice in new_slices]
    else: 
        new_arrs = [np_arr[:,slice[0]:slice[1]] for slice in new_slices]
    l = []
    if n_pictures>1:
        for i in range(n_pictures):
            new_list = new_arrs[i::n_pictures]
            l.append(new_list)
        outputs = [np.concatenate(new_arrs, axis=axis) for new_arrs in l]
        return outputs
    else:
        return [np.concatenate(new_arrs, axis=axis)]


img = image.imread(r"...")

img_new = split_img(img,n_pictures=3, axis=0)

for image in img_new:
    pyplot.imshow(image)
    pyplot.show()