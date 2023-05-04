import leafmap.foliumap as leafmap
import pandas as pd
import streamlit as st


with st.sidebar:
    st.title('Acompanhamento de pesquisas')

arquivo = st.file_uploader('Bufo', type=["gpkg"])


m = leafmap.Map()

if shp is not None:
    shp = gpd.read_file(arquivo)
    m.add_gdf(shp)
    m.to_streamlit(width=800, height=800)
