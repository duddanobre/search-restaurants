# 🍽️ Search Restaurants - Análise da Gastronomia de Fortaleza

**Aplicação Streamlit para análise completa do ecossistema gastronômico de Fortaleza, Ceará**

## 📊 Sobre o Projeto

Uma aplicação interativa desenvolvida em **Streamlit** que mapeia e analisa a vibrante cena gastronômica de Fortaleza. Com dados de **894 estabelecimentos** distribuídos em 5 categorias principais, oferece insights estratégicos para consumidores, proprietários e pesquisadores.

### 🏢 Categorias Analisadas

- 🍽️ **Restaurante** 
- 🥖 **Padaria**
- ☕ **Cafeteria**
- 🚗 **Drive Thru**
- 🛵 **Delivery de Comida**

## 🚀 Funcionalidades da Aplicação

### 📈 **Análise Completa de Mercado**
- **Panorama Geral**: Distribuição de estabelecimentos por categoria e concentração geográfica
- **Rankings de Qualidade**: Identificação dos melhores bairros por tipo de estabelecimento
- **Análise de Correlações**: Padrões entre popularidade, qualidade, tempos de entrega e localização
- **Insights Estratégicos**: Recomendações personalizadas para diferentes públicos

### 🗺️ **Mapeamento Geográfico Interativo**
- Visualização dos estabelecimentos bem avaliados (≥3.5) em mapa interativo
- Filtros dinâmicos por pontuação e tipo de estabelecimento
- Popups informativos com dados detalhados
- Análise de densidade por bairros

### � **Visualizações Avançadas**
- Gráficos de distribuição por categoria
- Rankings de bairros por qualidade média
- Heatmaps de correlações
- Scatter plots para análise de padrões
- Métricas de concentração de mercado

## 🎯 Públicos-Alvo

### 👥 **Consumidores**
- Rankings de qualidade por bairro e categoria
- Mapas interativos para descoberta de novos locais
- Análises baseadas em evidências para decisões informadas

### 🏪 **Estabelecimentos**
- Análises de concentração de mercado
- Benchmarking competitivo
- Insights para posicionamento estratégico

### 🔬 **Pesquisadores e Gestores Públicos**
- Padrões de distribuição urbana
- Dinâmicas territoriais do setor gastronômico
- Dados para políticas públicas

## 📁 Estrutura do Projeto

```
search-restaurants/
├── pages/
│   └── analise.py          # Página principal de análise
├── components/
│   └── sidebar.py          # Componente de navegação
├── database/
│   └── dadosTratados/
│       └── df_final_comGeo.csv  # Dataset principal
├── index.py                # Página inicial
└── README.md
```

## 🛠️ Tecnologias Utilizadas

- **Frontend**: Streamlit
- **Análise de Dados**: Pandas, NumPy
- **Visualizações**: Matplotlib, Seaborn, Plotly
- **Mapas Interativos**: Folium, Streamlit-Folium
- **Dados**: CSV com 894 estabelecimentos georreferenciados

## 📊 Qualidade dos Dados

O dataset inclui tratamento específico para:
- **PONTUACAO**: 226 valores ausentes (25.28%)
- **COMENTARIO**: 226 valores ausentes (25.28%) 
- **TEMPO_ESPERA**: 587 valores ausentes (65.66%)

Aplicação de filtros criteriosos para garantir confiabilidade nas análises.

## 🏃‍♂️ Como Executar

1. **Clone o repositório**
```bash
git clone https://github.com/duddanobre/search-restaurants.git
cd search-restaurants
```

2. **Instale as dependências**
```bash
pip install streamlit pandas numpy matplotlib seaborn folium streamlit-folium plotly
```

3. **Execute a aplicação**
```bash
streamlit run index.py
```

4. **Acesse no navegador**: `http://localhost:8501`

## 👥 Equipe

- **Front-end**: Maria Eduarda Roxa Nobre
- **Dashboard/Métricas**: Denise Ramos Soares  
- **Dados**: Ana Caroline Vieira Amorim
- **Engenharia**: Carlos Eduardo Oliveira Martins


