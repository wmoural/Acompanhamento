import leafmap.foliumap as leafmap
import pandas as pd
import streamlit as st


with st.sidebar:
    st.title('Acompanhamento de pesquisas')

    
m = leafmap.Map()

with st.container():
    m.to_streamlit(width=1200, width=1000)
