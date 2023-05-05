import leafmap.foliumap as leafmap
import pandas as pd
import streamlit as st
import geopandas as gpd


#Configurando Página
st.set_page_config(layout="wide")

#Lendo lotes
@st.cache_data  #
def LerBD(url):
    df = pd.read_excel(url)
    return df

Edificacoes = LerBD('https://docs.google.com/spreadsheets/d/1byWj7N81GRfk2mB3TfyTELGQJ8azDodk/export?format=xlsx&ouid=107947539613079650789&rtpof=true&sd=true')


if Edificacoes is not None:

    Edificacoes['geometry'] = gpd.GeoSeries.from_wkt(Edificacoes['geometry'])
    shp = gpd.GeoDataFrame(Edificacoes, geometry=Edificacoes['geometry'], crs='31984')


#Títulos
st.title(':green[Acompanhamento de pesquisas]')
st.markdown('Serviço de acompanhamento e análise de realização de pesquisas de campo em domicílios urbanos ou rurais.')


#-------------------MenuPrincial--------------------------

tab1, tab2 = st.tabs(['Pesquisa', 'Charts'])

#Barra lateral
with tab1:
    with st.sidebar:
        st.title(':orange[Métricas] :dart:')
        
        col_sidebar1, col_sidebar2, col_sidebar3 = st.columns([1,1,1])
        
        with col_sidebar1:
            st.metric('Concluídos', value=10, delta='20%')
        with col_sidebar2:
            st.metric('Andamento', value=13, delta='12%')
        with col_sidebar3:
            st.metric('Faltam', value=6, delta='-1%')
        
        st.title(':orange[Datas] :calendar:')
    
        st.metric('Data de início', value='05/05/2023')
    
        st.metric('Data prevista de término', value='10/05/2023')
    
        st.metric(':red[Atraso (dias)]', value=20)
            
        #arquivo = st.file_uploader('Insira valores:',type=["gpkg"])
    
    coluna1, coluna2 = st.columns([5,1])
    
    #Mapa da coluna 1:
    def mapacoluna1(shapefile):
        with coluna1:
            st.markdown(':orange[Domicílios vistados]')
    
            if Edificacoes is not None:
                m = leafmap.Map()
                m.add_basemap(basemap='HYBRID')
                m.add_gdf(shapefile, layer_name='Domicilios', fill_colors='red', zoom_to_layer=True)
                m.to_streamlit()
                
    with coluna2:
        st.markdown(':orange[Comandos]')
        
        if Edificacoes is not None:
            
            Lista = ['Todos','Concluídos','Iniciados', 'A iniciar', 'Problemáticos']
            CaixaSelecao = st.selectbox('Filtros', Lista, index=0)
            if CaixaSelecao == 'Todos':
                mapacoluna1(shp)
            else:
                shp_filtrado = shp[shp['situacao'] == CaixaSelecao]
                mapacoluna1(shp_filtrado)

with tab2:
    col1, col2, col3 = st.columns([25,25,25])
    
    with col1:
        st.line_chart(shp['area'])
    with col2:
        st.bar_chart(shp['situacao'], use_container_width=True)
    with col3:
        st.area_chart(shp['altura'], use_container_width=True)
