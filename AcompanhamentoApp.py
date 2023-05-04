import leafmap.foliumap as leafmap
import pandas as pd
import streamlit as st


with st.sidebar:
    st.title('Acompanhamento de pesquisas')

shp = st.fileuploader('Bufo')

m = leafmap.Map()

try:
    m.add_gdf(shp)
    m.to_streamlit(width=800, height=800)
except:
  pass  
