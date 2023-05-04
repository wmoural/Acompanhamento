import leafmap.foliumap as leafmap
import pandas as pd
import streamlit as st


with st.sidebar:
    st.title('Acompanhamento de pesquisas')

    
m = leafmap.Map()
coluna1 = st.columns([1])

with coluna1:
    m.to_streamlit(width=800, height=800)
