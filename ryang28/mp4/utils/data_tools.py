"""Implements feature extraction and other data processing helpers.
(This file will not be graded).
"""

import numpy as np
import skimage
from skimage import color


def preprocess_data(data, process_method='default'):
    """Preprocesses dataset.

    Args:
        data(dict): Python dict loaded using io_tools.
        process_method(str): processing methods needs to support
          ['raw', 'default'].
        if process_method is 'raw'
          1. Convert the images to range of [0, 1] by dividing by 255.
          2. Remove dataset mean. Average the images across the batch dimension.
             This will result in a mean image of dimension (8,8,3).
          3. Flatten images, data['image'] is converted to dimension (N, 8*8*3)
        if process_method is 'default':
          1. Convert images to range [0,1]
          2. Convert from rgb to gray then back to rgb. Use skimage
          3. Take the absolute value of the difference with the original image.
          4. Remove dataset mean. Average the absolute value differences across
             the batch dimension. This will result in a mean of dimension (8,8,3).
          5. Flatten images, data['image'] is converted to dimension (N, 8*8*3)

    Returns:
        data(dict): Apply the described processing based on the process_method
        str to data['image'], then return data.
    """
    if process_method == 'raw':
        pass
        N = (data['image'].shape)[0]
        temp_img = (data['image']/255.0)
        mean_img = np.mean(temp_img, axis=0)
        for img in temp_img:
            img -= mean_img
        data['image'] = np.reshape(temp_img, (N, 192))

    elif process_method == 'default':
        pass
        N = (data['image'].shape)[0]
        temp_img = (data['image']/255.0)
        converted_img = color.gray2rgb(color.rgb2gray(temp_img))        
        temp_img = np.absolute(temp_img - converted_img)
        mean_img = np.mean(temp_img, axis = 0)
        for img in temp_img:
            img -= mean_img
        data['image'] = np.reshape(temp_img, (N, 192))

    elif process_method == 'custom':
        # Design your own feature!
        pass
    return data


def compute_image_mean(data):
    """ Computes mean image.

    Args:
        data(dict): Python dict loaded using io_tools.

    Returns:
        image_mean(numpy.ndarray): Avaerage across the example dimension.
    """
    image_mean = None
    pass
    return image_mean


def remove_data_mean(data):
    """Removes data mean.

    Args:
        data(dict): Python dict loaded using io_tools.

    Returns:
        data(dict): Remove mean from data['image'] and return data.
    """
    pass
    return data
