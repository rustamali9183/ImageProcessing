import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import main
import seaborn as sns


# Function to display image
def display_image(image):
    st.image(image)

# Function to display the description
def display_description(description):
    st.text(description)

def histogram(image):
    image = np.histogram(image)
    return image

# Function to display the formula used
def display_formula(latex):
    st.sidebar.markdown("<h2 style='text-align: center;'>Formula Used</h2>", unsafe_allow_html=True)
    st.sidebar.latex(latex)

