import numpy as np
import scipy
import functions as f
import main
filter = None

def identity_filter(image, size, diagonal_value):
    """
    An identity filter, also known as an identity matrix filter or a unity filter, is a type of filter that doesn't change the original image. It's a square matrix where all the elements of the principal diagonal are ones, and the rest of the elements are zeros.
Mathematical Representation:
A 3x3 identity filter looks like this:
[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
How it Works:
When you apply an identity filter to an image, it multiplies each pixel value by the corresponding filter coefficient. Since the filter coefficients are either 0 or 1, the pixel values remain unchanged.
    :param image:
    :param size:
    :param diagonal_value:
    :return:
    """
    global filter
    image = np.array(image)
    if size>image.shape[0] or size>image.shape[1]:
        raise ValueError('Filter size is larger than image size, please select minimum value')
    filter = np.zeros((size, size))
    np.fill_diagonal(filter, diagonal_value)
    if len(image.shape) == 2:
        filter_image = scipy.ndimage.convolve(image, filter, mode='nearest')
        # If the image is color, apply the filter to each color channel separately
    else:
        filter_image = np.zeros_like(image)
        for i in range(image.shape[2]):
            filter_image[:, :, i] = scipy.ndimage.convolve(image[:, :, i], filter, mode='nearest')

    return filter_image