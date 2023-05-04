import leafmap.foliumap as leafmap
import pandas as pd
import streamlit as st

m = leafmap.Map()

m.to_streamlit(width=800)