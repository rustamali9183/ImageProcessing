import numpy as np
import PIL
import cv2
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

def applyMask(img,mask,denominator,i,j):
    u,v,w=0,0,0
    for x in range(-1,2):
        for y in range(-1,2):
            if(i+x>=0 and i+x<len(img) and j+y>=0 and j+y<len(img[0])):
                r,g,b=img[i+x,j+y]
                u+=int(r)*mask[x+1][y+1]
                v+=int(g)*mask[x+1][y+1]
                w+=int(b)*mask[x+1][y+1]
    u=min(u,255)
    v=min(v,255)
    w=min(w,255)
    u=max(u,0)
    v=max(v,0)
    w=max(w,0)
    u=u//denominator
    v=v//denominator
    w=w//denominator
    return u,v,w

def box_Filter(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    mask=[[1,1,1],[1,1,1],[1,1,1]]
    for i in range(height):
        for j in range(width):
            r,g,b=applyMask(image,mask,9,i,j)
            MaskedImage[i,j]=[r,g,b]
    
    return MaskedImage


def weighted_average(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    mask=[[1,2,1],[2,4,2],[1,2,1]]
    for i in range(height):
        for j in range(width):
            r,g,b=applyMask(image,mask,16,i,j)
            MaskedImage[i,j]=[r,g,b]
    
    return MaskedImage

def laplacian_1(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    mask=[[0,-1,0],[-1,4,-1],[0,-1,0]]
    for i in range(height):
        for j in range(width):
            r,g,b=applyMask(image,mask,1,i,j)
            MaskedImage[i,j]=[r,g,b]
    
    return MaskedImage

def laplacian_2(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    mask=[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    for i in range(height):
        for j in range(width):
            r,g,b=applyMask(image,mask,1,i,j)
            MaskedImage[i,j]=[r,g,b]
    
    return MaskedImage

def horizontal_sobel(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    mask=[[-1,-2,-1],[0,0,0],[1,2,1]]
    for i in range(height):
        for j in range(width):
            r,g,b=applyMask(image,mask,1,i,j)
            MaskedImage[i,j]=[r,g,b]
    
    return MaskedImage

    
def vertical_sobel(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    mask=[[-1,0,1],[-2,0,2],[-1,0,1]]
    for i in range(height):
        for j in range(width):
            r,g,b=applyMask(image,mask,1,i,j)
            MaskedImage[i,j]=[r,g,b]
    
    return MaskedImage


def horizontal_prewitt(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    mask=[[-1,-1,-1],[0,0,0],[1,1,1]]
    for i in range(height):
        for j in range(width):
            r,g,b=applyMask(image,mask,1,i,j)
            MaskedImage[i,j]=[r,g,b]
    
    return MaskedImage

def vertical_prewitt(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    mask=[[-1,0,1],[-1,0,1],[-1,0,1]]
    for i in range(height):
        for j in range(width):
            r,g,b=applyMask(image,mask,1,i,j)
            MaskedImage[i,j]=[r,g,b]
    
    return MaskedImage


def applyMed(img,i,j):
    u,v,w=[],[],[]
    for x in range(-1,2):
        for y in range(-1,2):
            if(i+x>=0 and i+x<len(img) and j+y>=0 and j+y<len(img[0])):
                r,g,b=img[i+x,j+y]
                u.append(r)
                v.append(g)
                w.append(b)
            else:
                u.append(0)
                v.append(0)
                w.append(0)
                
    return sorted(u)[4],sorted(v)[4],sorted(w)[4]    
    
def median_filter(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    for i in range(height):
        for j in range(width):
            r,g,b=applyMed(image,i,j)
            MaskedImage[i,j]=[r,g,b]
    return MaskedImage

def applyMin(img,i,j):
    u,v,w=255,255,255
    for x in range(-1,2):
        for y in range(-1,2):
            if(i+x>=0 and i+x<len(img) and j+y>=0 and j+y<len(img[0])):
                r,g,b=img[i+x,j+y]
                u=min(u,r)
                v=min(v,r)
                w=min(w,r)
    
    return u,v,w

def min_filter(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    for i in range(height):
        for j in range(width):
            r,g,b=applyMin(image,i,j)
            MaskedImage[i,j]=[r,g,b]
    return MaskedImage

def applyMax(img,i,j):
    u,v,w=0,0,0
    for x in range(-1,2):
        for y in range(-1,2):
            if(i+x>=0 and i+x<len(img) and j+y>=0 and j+y<len(img[0])):
                r,g,b=img[i+x,j+y]
                u=max(u,r)
                v=max(v,r)
                w=max(w,r)
    
    return u,v,w

def max_filter(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    for i in range(height):
        for j in range(width):
            r,g,b=applyMax(image,i,j)
            MaskedImage[i,j]=[r,g,b]
    return MaskedImage

def embossing_filter(image):
    MaskedImage=image.copy()
    height,width,x=image.shape
    mask=[[-2,-1,0],[-1,1,1],[0,1,2]]
    for i in range(height):
        for j in range(width):
            r,g,b=applyMask(image,mask,1,i,j)
            MaskedImage[i,j]=[r,g,b]
    
    return MaskedImage

def motion_blur(image,n):
    MaskedImage=image.copy()
    height,width,x=image.shape
    mask=[[1,0,0],[0,1,0],[0,0,1]]
    for i in range(height):
        for j in range(width):
            r,g,b=applyMask(image,mask,n,i,j)
            MaskedImage[i,j]=[r,g,b]
    return MaskedImage

def histogram_equalization(image):
    equalized_image = cv2.equalizeHist(image)
    return equalized_image
