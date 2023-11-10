import streamlit as st
from PIL import Image

st.subheader("Convert Color camera photo to grayscale")

with st.expander("Upload Image"):
    user_image = st.file_uploader("Upload your Image")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Click a photo")

if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)
elif user_image:
    img = Image.open(user_image)
    gray_image = img.convert("L")
    st.image(gray_image)


