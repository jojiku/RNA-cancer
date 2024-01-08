import streamlit as st
import hydralit_components as hc
from joblib import load
import pandas as pd

model = load('direct_model')

st.set_page_config(
    page_title="SidePage",
    page_icon="👨‍🔬",
)

st.title(":blue[Non-invasive diagnosis of brain tumors]")

st.header(
    "To use this service please upload RNAs of a patient in csv format below:"
)

uploaded_file = st.file_uploader("", type="csv")
if uploaded_file is not None:   
    if st.button("Get results"):
        with hc.HyLoader('Thinking...', hc.Loaders.standard_loaders, index=[5]):
                data = pd.read_csv(uploaded_file)
                result = model.predict(data)
                if result == 0:
                    st.markdown("<p style='background-color: green; font-size: 20px; display: inline; padding: 0.2em 0.5em; border-radius: 0.5em;'>Patient is healthy</p>", unsafe_allow_html=True)
                else:
                    st.markdown("<p style='background-color: red; font-size: 20px; display: inline; padding: 0.2em 0.5em; border-radius: 0.5em;'>Patient is sick</p>", unsafe_allow_html=True)


st.sidebar.success("Statistics on given data")


