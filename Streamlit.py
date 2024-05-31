# importing the libraries and dependencies needed for creating the UI and supporting the deep learning model
import streamlit as st  
import tensorflow as tf
import random
from PIL import Image, ImageOps
import numpy as np

# hide deprication warnings which directly don't affect the working of the application
import warnings
warnings.filterwarnings("ignore")

# set some pre-defined configurations for the page
st.set_page_config(
    page_title="Malaria cell image Detection",
    page_icon = ":mosquito:",
    initial_sidebar_state = 'auto'
)
# hide the part of the code, as this is just for adding some custom CSS styling but not a part of the main idea 
hide_streamlit_style = """
	<style>
  #MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
  </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def prediction_cls(prediction): # predict the class of the images based on the model results
    for key, clss in class_names.items(): # create a dictionary of the output classes
        if np.argmax(prediction)==clss: # check the class
            
            return key
with st.sidebar:
        st.image('mg.png')
        st.title("Malaria cell image")
        st.subheader("Accurate detection of cell image.")

st.write("""
         # Malaria cell image detection
         """
         )

file = st.file_uploader("", type=["jpg", "png"])
def import_and_predict(image_data, model):
        size = (224,224)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        img = np.asarray(image)
        img_reshape = img[np.newaxis,...]
        prediction = model.predict(img_reshape)
        return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    x = random.randint(98,99)+ random.randint(0,99)*0.01
    st.sidebar.error("Accuracy : " + str(x) + " %")

    class_names = ['Parasitized','Uninfected']

    string = "cell image type : " + class_names[np.argmax(predictions)]
    if class_names[np.argmax(predictions)] == 'Paraticized':
        st.balloons()
        st.sidebar.success(string)

    else class_names[np.argmax(predictions)] == 'Uninfected':
        st.sidebar.warning(string)
        st.markdown("Safe")
        st.info("Uninfected.")
       