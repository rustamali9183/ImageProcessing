import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
import filters as ft
import point_operations as po
import functions as f
global col3
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit.runtime.media_file_storage import MediaFileStorageError



# Main function
def main():
    st.markdown("<h2 style='text-align: center;'>Image Processing</h2>", unsafe_allow_html=True)

    # File uploader
    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Default image
    if uploaded_file is None:
        image = Image.open("default_image.png")
    else:
        image = Image.open(uploaded_file)
    image=np.array(image)
    col1, col2 = st.columns(2)
    # Display original image
    with col1:
        st.text("Original Image")
        f.display_image(image)

    # Function selector
    functions = [None, "thresholding", "digital_negative", 'log_transformation', 'clipping', 'identity_filter', 'histogram','box_filter','weighted_average','laplacian_1','laplacian_2','horizontal_sobel','vertical_sobel','horizontal_prewitt','vertical_prewitt','median_filter','min_filter','max_filter','embossing_filter','motion_blur','histogram_equalization']

    selected_function = st.sidebar.selectbox("Functions", functions)


    if selected_function == "digital_negative":
        manipulated_image = po.digital_negative(image)
        description = po.digital_negative.__doc__

    elif selected_function == "thresholding":
        t = st.sidebar.slider("T Value", 0, 255, 2)
        manipulated_image = po.thresholding(image, t)
        description = po.thresholding.__doc__

    elif selected_function == 'log_transformation':
        manipulated_image = po.log_transformation(image)
        description = po.log_transformation.__doc__

    elif selected_function == 'clipping':
        r1 = st.sidebar.slider('r1 value', 0, 255, 1)
        r2 = st.sidebar.slider('r2 value', 0, 255, 1)
        if r1>r2:
            st.sidebar.error('Bhai r1 ko r2 se kam rakh')
        manipulated_image = po.clipping(image, r1, r2)
        description =  po.clipping.__doc__

    elif selected_function == 'identity_filter':
        size = st.sidebar.slider('Specify the size of the filter', 3, 11, 3, 2)
        diagonal_value = st.sidebar.slider('Specify the diagonal value of the filter', 1, 255, 255)
        manipulated_image = ft.identity_filter(image, size, diagonal_value)
        description = ft.identity_filter.__doc__

    elif selected_function == 'box_filter':
        manipulated_image = po.box_Filter(image)

    elif selected_function == 'weighted_average':
        manipulated_image = po.weighted_average(image)

    elif selected_function == 'laplacian_1':
        manipulated_image = po.laplacian_1(image)

    elif selected_function == 'laplacian_2':
        manipulated_image = po.laplacian_2(image)

    elif selected_function == 'horizontal_sobel':
        manipulated_image = po.horizontal_sobel(image)

    elif selected_function == 'vertical_sobel':
        manipulated_image = po.vertical_sobel(image)

    elif selected_function == 'horizontal_prewitt':
        manipulated_image = po.horizontal_prewitt(image)

    elif selected_function == 'vertical_prewitt':
        manipulated_image = po.vertical_prewitt(image)

    elif selected_function == 'median_filter':
        manipulated_image = po.median_filter(image)

    elif selected_function == 'min_filter':
        manipulated_image = po.min_filter(image)

    elif selected_function == 'max_filter':
        manipulated_image = po.max_filter(image)

    elif selected_function == 'embossing_filter':
        manipulated_image = po.embossing_filter(image)

    elif selected_function == 'motion_blur':
        n = st.sidebar.slider('constant', 0, 255, 1)
        manipulated_image = po.motion_blur(image,n)

    elif selected_function == 'histogram_equalization':
        manipulated_image = po.histogram_equalization(image)

    
    

    # Display manipulated image
    with col2:
        if selected_function is not None:
            st.text(str(selected_function))
            try:
                f.display_image(manipulated_image)
            except:
                st.text('Please select some operation')
        else:
            st.text('To kaese hain aap log \n Chaliye shuru krte hain \n koi function choose kariye sidebar se')

    col3, col4 = st.columns(2)

    if selected_function == "identity_filter":
        with col3:
            st.text("Filter")
            st.image(np.array(ft.filter)/255.0, use_container_width=True)
        with col4:
            st.text("Filter Matrix:")
            st.write(ft.filter)
    elif selected_function == 'histogram':
        with col3:
            try:
                image = np.array(image)
                bins = st.sidebar.slider('Select the number of bins', 1, 256, 255, 1)
                fig, ax = plt.subplots()
                ax.hist(image.flatten(), bins=bins)
                st.pyplot(fig)
            except:
                pass

    # Display description
    st.subheader("Description")
    try:
        st.write(description)
    except:
        st.write("Daya kuch to gadbad hai")



if __name__ == "__main__":
    main()

