import numpy as np
import PIL
import streamlit as st
import functions as f
# Function for Digital Negative
def digital_negative(image):
    """
    Digital negative refers to the inverse of an original image.
    This means that the dark areas in the original image become light, and the light areas become dark.
    :param image:
    :return:
    """
    image = np.array(image)
    image = 255-image
    f.display_formula('255-(image)')
    return image

# Function for thresholding the image
def thresholding(image, t):
    """
    Thresholding is a fundamental technique in digital image processing that involves converting a
    grayscale image in to binary image. This is achieved by selecting a threshold value and classifying
    each pixel on its intensity level relative to this threshold.
    :param image:
    :param t:
    :return:
    """
    image = np.array(image)
    image = np.where(image>t, 255, 0)
    f.display_formula(r"""
L = \begin{cases} 
255, & \text{if } r \geq t, \\
0, & \text{if } r < t.
\end{cases}
""")
    return image

# Function for clipping the image
def clipping(image, r1, r2):
    """
    clipping is used to strip the particular range of values in the image and
    the rest values will become zero
    :param image:
    :param r1:
    :param r2:
    :return:
    """
    image = np.array(image)
    image = np.where((image>=r1) & (image<=r2), image, 0)
    f.display_formula(r'''
    L = \begin{cases}
    image, & \text{if } r1<=image<=r2, \\
    0, &  otherwise
    \end{cases}
    ''')
    return image

# Function for Log Transformation
def log_transformation(image):
    """
    This technique is used for applying a logarithm function to the intensity values.
    This transformation is particulary useful for compressing the dynamic range of an image,
    especially when dealing with images that have a wide range of intensity values.
    :param image:
    :return:
    """
    image = np.array(image)
    c = 255 / (np.log(1 + np.max(image)))
    image =  c * np.log(1 + image)
    f.display_formula(
        r"""
    c = 255 / np.log(1 + np.max(image)) \newline
    c * np.log(1 + image)
    """
    )
    return np.uint8(image)
