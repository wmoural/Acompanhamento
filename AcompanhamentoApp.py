import leafmap.foliumap as leafmap
import pandas as pd
import streamlit as st


with st.sidebar:
    st.title('Acompanhamento de pesquisas')

    
col1 = st.columns(1)

with col1:
    m = leafmap.Map()
    m.to_streamlit(width=800)
