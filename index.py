
import streamlit as st

from components.sidebar import sidebar

sidebar()

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
Este projeto propõe o desenvolvimento de uma aplicação interativa em Streamlit destinada a mapear e explorar a vibrante cena gastronômica de Fortaleza, Ceará. A partir de um conjunto de dados abrangente, que inclui **cafeterias, restaurantes, padarias, serviços de delivery e opções de drive-thru**, a plataforma se posiciona como uma ferramenta essencial para moradores e turistas que desejam descobrir, avaliar e tomar decisões informadas sobre onde comer na capital cearense.

### **🔍 O Que Você Pode Explorar**

Nossa aplicação oferece uma análise completa e interativa do ecossistema gastronômico fortalezense:

- **📊 Análise de Mercado Completa**: Descubra padrões de distribuição, concentração geográfica e tendências de qualidade através de visualizações detalhadas
- **🗺️ Mapeamento Geográfico Interativo**: Explore estabelecimentos bem avaliados através de mapas dinâmicos com filtros personalizáveis
- **🏆 Rankings de Qualidade por Região**: Identifique os melhores bairros para cada tipo de estabelecimento baseado em avaliações reais
- **🔗 Análise de Correlações**: Compreenda as relações entre popularidade, qualidade, tempos de entrega e localização
- **💡 Insights Estratégicos**: Recomendações personalizadas para consumidores, empresários e investidores

### **Importância Econômica e Cultural**

O setor gastronômico de Fortaleza é um dos mais dinâmicos do Brasil, uma força econômica que se traduz na geração de milhares de empregos e na movimentação de uma robusta cadeia produtiva. De pequenos negócios familiares a grandes redes de restaurantes e franquias, esses estabelecimentos são essenciais para a vitalidade econômica dos bairros, funcionando como verdadeiros motores do desenvolvimento local.

Do ponto de vista cultural, esses espaços são o coração da vida cotidiana fortalezense. Muito além do valor comercial, eles são pontos de encontro, celebração e trabalho. Essa tradição de transformar locais de consumo em centros de efervescência cultural não é nova. Remonta ao final do século XIX, com a **Padaria Espiritual (1892-1898)**. Este movimento, uma das mais originais agremiações literárias e artísticas do Brasil, foi fundado por jovens intelectuais em um café na Praça do Ferreira. Usando a metáfora de uma padaria para "assar ideias" e "fornecer o pão do espírito" à população, eles provaram que um espaço gastronômico pode ser também um catalisador de ideias, política e identidade cultural. A Padaria Espiritual consolidou o Realismo e o Simbolismo no Ceará, deixando um legado que demonstra como a cultura da cidade sempre floresceu ao redor de uma mesa e um café. Hoje, as padarias, restaurantes e cafeterias da cidade dão continuidade a essa herança, ocupando um lugar afetivo e estratégico no imaginário e na rotina de seus habitantes.

Na atualidade, os vários polos gastronômicos de Fortaleza seguem sendo destino de mentes inquietas e inconformadas que se reúnem para moldar novos padrões para a arte contemporânea, mantendo o legado de movimentos como os da Padaria Espiritual ainda vivos. É fundamento do ser humano a associação entre o compartilhar o alimento do corpo e aquele que agita o espírito, processo no qual Fortaleza segue sendo referência, colorindo o mosaico de tendências intelectuais com ampla oferta de polos gastronômicos onde fermentar essas mudanças.

É na intenção de contribuir para a identificação daqueles locais que mais conversam com o perfil de cada grupo que essa aplicação foi desenvolvida. Através de uma interface intuitiva e rica em dados, buscamos não apenas mapear, mas também analisar e compreender a complexidade do setor gastronômico de Fortaleza, oferecendo uma ferramenta que vai além da simples listagem de estabelecimentos.
            
### **A Solução: Conectando Dados, Decisões e Experiências**

A aplicação surge como uma ferramenta estratégica e completa para atender às seguintes necessidades:

- **Para o Consumidor:** Em uma cidade com uma oferta tão vasta e diversificada, encontrar o local ideal para cada ocasião pode ser um desafio. Nossa plataforma utiliza **análise de dados baseada em evidências** para auxiliar diretamente os consumidores. Com rankings de qualidade por bairro, mapas interativos filtráveis por pontuação e análises de correlação entre popularidade e qualidade, você pode tomar decisões mais informadas sobre onde comer, considerando não apenas a proximidade, mas também a reputação e padrões de qualidade de cada estabelecimento.

- **Para os Estabelecimentos:** O projeto funciona como uma vitrine digital democrática para todo o setor gastronômico, mas vai além da simples exposição. Através de **análises de concentração de mercado, padrões geográficos e benchmarking competitivo**, oferecemos insights valiosos para proprietários entenderem seu posicionamento no mercado, identificarem oportunidades de melhoria e desenvolverem estratégias baseadas em dados reais do setor.

- **Para Pesquisadores e Gestores Públicos:** Nossa análise quantitativa fornece uma visão clara dos **padrões de distribuição urbana, concentração econômica e dinâmicas territoriais** do setor gastronômico, contribuindo para políticas públicas mais eficazes e estudos acadêmicos sobre desenvolvimento urbano e economia local.

### **🚀 Comece Sua Exploração**

Navegue pelas abas do menu lateral para descobrir insights únicos sobre a gastronomia fortalezense. Cada seção oferece perspectivas diferentes e ferramentas interativas para uma experiência completa de análise e descoberta.
""")