import streamlit as st

def sidebar():
    with st.sidebar:
        st.page_link("index.py", label="🏠 Home")
        st.page_link("pages/analise.py", label="📊 Análise")
        st.page_link("pages/search.py", label="🔍 Buscar restaurante")
