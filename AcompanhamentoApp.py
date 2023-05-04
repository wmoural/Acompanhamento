import leafmap.foliumap as leafmap
import pandas as pd
import streamlit as st


with st.sidebar:
    st.title('Acompanhamento de pesquisas')

shp = st.fileuploader('Bufo', type=["gpkg"])

m = leafmap.Map()

if shp is not None:
    m.add_gdf(shp)
    m.to_streamlit(width=800, height=800)
