import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Drawable Canvas")
st.markdown(
    """
Draw on the canvas, get the image data back into Python !
* Doubleclick to remove the selected object when not in drawing mode
"""
)
st.sidebar.header("Configuration")

# Specify brush parameters and drawing mode
stroke_width = st.sidebar.slider("Stroke width: ", 1, 100, 10)
stroke_color = st.sidebar.beta_color_picker("Stroke color hex: ")
bg_color = st.sidebar.beta_color_picker("Enter background color hex: ", "#eee")
drawing_mode = st.sidebar.selectbox(
    "Drawing mode", ("freedraw", "line", "rect", "transform")
)

# Create a canvas component
canvas_result = st_canvas(
    "rgba(255, 165, 0, 0.3)", # Fixed fill color with some opacity
    stroke_width,
    stroke_color,
    bg_color,
    height=150,
    drawing_mode=drawing_mode,
    key="canvas",
)

# Do something interesting with the image data
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
    st.json(canvas_result.json_data)
