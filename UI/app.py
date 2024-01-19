import logging
import streamlit as st
import pandas as pd
from PIL import Image, ImageEnhance
import joblib
import base64


logging.basicConfig(level=logging.INFO)

# Streamlit Page Configuration
st.set_page_config(
    page_title="Brain tumors diagnosis",
    page_icon="icon.jpg",
    layout="wide",
    initial_sidebar_state="expanded",

)

# Streamlit Updates and Expanders
st.title("Non-invasive diagnosis of brain tumors")

API_DOCS_URL = "https://docs.streamlit.io/library/api-reference"

@st.cache_data(show_spinner=False)
def load_and_enhance_image(image_path, enhance=False):
    """
    Load and optionally enhance an image.

    Parameters:
    - image_path: str, path of the image
    - enhance: bool, whether to enhance the image or not

    Returns:
    - img: PIL.Image.Image, (enhanced) image
    """
    img = Image.open(image_path)
    if enhance:
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.8)
    return img

def img_to_base64(image_path):
    """Convert image to base64"""
    with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

def main():
    """
    Display Streamlit updates and handle the chat interface.
    """
    # Inject custom CSS for glowing border effect
    st.markdown(
        """
        <style>
        .cover-glow {
            width: 75%;
            height: 20;
            padding: 3px;
            box-shadow: 
                0 0 5px #000033,
                0 0 10px #000066,
                0 0 15px #000099,
                0 0 20px #0000CC,
                0 0 25px #0000FF,
                0 0 30px #3333FF,
                0 0 35px #6666FF;
            position: relative;
            z-index: -1;
            border-radius: 30px;  /* Rounded corners */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Function to convert image to base64
    def img_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    # Load and display sidebar image with glowing effect
    img_path = "icon.jpg"
    img_base64 = img_to_base64(img_path)
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
        unsafe_allow_html=True,
    )
    st.sidebar.markdown("---")
    
    # Sidebar for Mode Selection
    mode = st.sidebar.radio("Select Mode:", options=["Tumour prediction with RNA", "Recommendations based on given data"], index=1)
    
    st.sidebar.markdown("---")
    # Toggle checkbox in the sidebar for basic interactions
    show_basic_info = st.sidebar.toggle("Service Usage Instructions", value=True)

    # Display the st.info box if the checkbox is checked
    if show_basic_info:
        st.sidebar.markdown("""
        ### Basic Interactions
        - **What format data should be?**: csv file example is located here: .
        - **How to upload data?**: Use keywords like 'code example', 'syntax', or 'how-to' to get relevant code snippets.
        - **Other question ...**: .
        """)
    if mode == "Tumour prediction with RNA":
    # Code for Tumour prediction with RNA mode
        uploaded_file = st.file_uploader("Patient's sequenced RNA in csv format:", type="csv")
        if uploaded_file is not None:
            # Read the CSV file using pandas
            data = pd.read_csv(uploaded_file)

            # Reads in saved classification model
            model_path = 'direct_model'
            with open(model_path, 'rb') as model_file:
                model = joblib.load(model_file) 
            # Apply model to make predictions
            prediction = model.predict(data)
            st.subheader("Model's prediction:")

            if prediction[0] == 0:
                st.markdown("<p style='background-color: green; font-size: 20px; display: inline; padding: 0.2em 0.5em; border-radius: 0.5em;'>NO EVIDENCE OF BRAIN TUMOUR</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p style='background-color: red; font-size: 20px; display: inline; padding: 0.2em 0.5em; border-radius: 0.5em;'>HIGH CHANCE OF BRAIN TUMOUR</p>", unsafe_allow_html=True)

    
        else:
            st.title(" ")
     


    


    elif mode == "Recommendations based on given data":
    # Code for Recommendations based on given data mode
        st.write("Recommendations based on your data")

        

if __name__ == "__main__":
    main()