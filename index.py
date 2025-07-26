import streamlit as st

st.sidebar.page_link("index.py", label="🏠 Home")
st.sidebar.page_link("pages/analise.py", label="📊 Análise")
st.sidebar.page_link("pages/search.py", label="🔍 Buscar restaurante")

autores = ["front: Maria Eduarda Roxa Nobre", "dash/metricas: Denise Ramos Soares", "dados: Ana Caroline Vieira Amorim", "engenharia: Carlos Eduardo Oliveira Martins"]

with st.sidebar:
    st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background-color: #f0f2f5;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    "Autores:" 

    for autor in autores:
        st.markdown(f"- {autor}")


st.title("Restaurantes em Fortaleza")

st.header("Sobre", divider=True)

st.text_area("Este é um projeto de análise de dados de restaurantes em Fortaleza, Ceará, Brasil. O objetivo é fornecer uma visão geral dos estabelecimentos, incluindo informações sobre localização, tipo de cozinha e avaliações dos clientes. A análise é baseada em dados coletados de fontes públicas e visa ajudar os usuários a encontrar o restaurante ideal para suas necessidades.")