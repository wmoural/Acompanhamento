import leafmap.foliumap as leafmap
import pandas as pd
import streamlit as st


with st.sidebar:
    st.title('Acompanhamento de pesquisas')
    st.selectbox('1','2','3')
 

with st.columns(1):
        
    m = leafmap.Map()
    
    m.to_streamlit(width=800)
