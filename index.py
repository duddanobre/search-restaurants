
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

st.markdown("""
Este projeto propõe o desenvolvimento de uma aplicação interativa em Streamlit destinada a mapear e explorar a vibrante cena gastronômica de Fortaleza, Ceará. A partir de um conjunto de dados abrangente, que inclui **cafeterias, restaurantes, padarias, serviços de delivery e opções de drive-thru**, a plataforma se posiciona como uma ferramenta essencial para moradores e turistas. A escolha deste tema ampliado se justifica pela força do setor gastronômico como um pilar fundamental para a economia, a cultura e a identidade da cidade.

### **Importância Econômica e Cultural**

O setor gastronômico de Fortaleza é um dos mais dinâmicos do Brasil, uma força econômica que se traduz na geração de milhares de empregos e na movimentação de uma robusta cadeia produtiva. De pequenos negócios familiares a grandes redes de restaurantes e franquias, esses estabelecimentos são essenciais para a vitalidade econômica dos bairros, funcionando como verdadeiros motores do desenvolvimento local.

Do ponto de vista cultural, esses espaços são o coração da vida cotidiana fortalezense. Muito além do valor comercial, eles são pontos de encontro, celebração e trabalho. Essa tradição de transformar locais de consumo em centros de efervescência cultural não é nova. Remonta ao final do século XIX, com a **Padaria Espiritual (1892-1898)**. Este movimento, uma das mais originais agremiações literárias e artísticas do Brasil, foi fundado por jovens intelectuais em um café na Praça do Ferreira. Usando a metáfora de uma padaria para "assar ideias" e "fornecer o pão do espírito" à população, eles provaram que um espaço gastronômico pode ser também um catalisador de ideias, política e identidade cultural. A Padaria Espiritual consolidou o Realismo e o Simbolismo no Ceará, deixando um legado que demonstra como a cultura da cidade sempre floresceu ao redor de uma mesa e um café. Hoje, as padarias, restaurantes e cafeterias da cidade dão continuidade a essa herança, ocupando um lugar afetivo e estratégico no imaginário e na rotina de seus habitantes.

### **A Solução: Conectando Consumidores, Estabelecimentos e Experiências**

A aplicação surge como uma ferramenta estratégica e completa para atender às seguintes necessidades:

- **Para o Cliente:** Em uma cidade com uma oferta tão vasta e diversificada, encontrar o local ideal para cada ocasião pode ser um desafio. Seja uma cafeteria para uma reunião de trabalho, um restaurante para um jantar especial, a padaria do café da manhã, um delivery rápido ou um drive-thru conveniente, nossa plataforma auxiliará diretamente os consumidores. Com filtros por tipo de estabelecimento e localização do usuário no momento da consulta, a ferramenta otimiza o tempo e a experiência de escolha, permitindo-lhes localizar facilmente os pontos mais próximos, planejar rotas e descobrir novas opções gastronômicas em toda a cidade.

- **Para os Estabelecimentos:** O projeto funciona como uma vitrine digital democrática para todo o setor gastronômico. Ele oferece visibilidade crucial, especialmente para negócios recém-inaugurados, de menor porte ou que carecem de recursos para divulgação. Ao serem incluídos no mapa interativo, **restaurantes, cafeterias, padarias** e outros serviços ganham destaque e alcançam um público diversificado, o que potencializa seu crescimento e consolidação em um mercado competitivo.
""")