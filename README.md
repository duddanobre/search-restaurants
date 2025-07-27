# search-restaurants
Trabalho final (LP)


🧹 Projeto de Tratamento e Geolocalização de Dados

📁 Visão Geral
    Este projeto realiza duas etapas principais com base em dados de endereços:
    Limpeza e tratamento dos dados brutos (data_cleaning.py)
    Geocodificação dos endereços para obter latitude e longitude (data_geolytic.py)

🔧 Estrutura do Projeto
    .
    ├── data_cleaning.py      # Etapa 1: Limpeza e padronização dos dados
    ├── data_geolytic.py      # Etapa 2: Geolocalização usando ArcGIS
    ├── data_inferencias.py      # Etapa 2: Geolocalização usando ArcGIS
    ├── database/
    │   ├── dadosbrutos/      # Dados de entrada (originais)
    │   ├── dadostratados/    # Dados limpos e geolocalizados
    ├── README.md             # Documentação

📌 Etapas
    1. data_cleaning.py
        Lê os arquivos da pasta dadosbrutos
        Remove inconsistências, campos inválidos, caracteres especiais, etc.
        Salva o arquivo limpo na pasta dadostratados como df_final_semGeo.csv
    2. data_geolytic.py
        Carrega o df_final_semGeo.csv tratado
        Usa a API ArcGIS (Esri) para buscar as coordenadas geográficas (LAT, LNG) de cada endereço
        Salva o resultado final na mesma pasta
    3. data_inferencias.ipynb
        Carrega o df_final_comGeo.csv tratado
        Cria varias inferencias de teste de integridade e usabilidade dos dados
