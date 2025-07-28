# search-restaurants
Trabalho final (LP)

## 📊 Análise de Estabelecimentos Alimentares de Fortaleza

### `visualizacoes.ipynb`

Este notebook realiza uma **análise abrangente do mercado de estabelecimentos alimentares em Fortaleza**, processando dados de **893 estabelecimentos** distribuídos em **5 categorias** principais:

- 🍽️ **Restaurante**
- 🥖 **Padaria** 
- ☕ **Cafeteria**
- 🚗 **Drive Thru**
- 🛵 **Delivery de Comida**

#### 🎯 Principais Funcionalidades

**1. Panorama Geral do Mercado**
- Distribuição de estabelecimentos por categoria
- Concentração geográfica nos bairros de Fortaleza
- Identificação de segmentos dominantes e oportunidades

**2. Análise de Qualidade por Segmento**
- Rankings gerais de bairros por qualidade
- Análise específica por tipo de estabelecimento
- Identificação dos melhores bairros para cada categoria

**3. Análise de Correlações e Padrões**
- **Matriz de correlação**: Relações entre todas as variáveis numéricas
- **Tempo Mínimo vs Máximo**: Insights sobre consistência operacional
- **Popularidade vs Qualidade**: Padrões por tipo de estabelecimento

**4. Mapeamento Geográfico Interativo**
- **Mapa de Fortaleza**: Distribuição dos estabelecimentos bem avaliados (≥3.5)
- **Interatividade**: Popups com informações detalhadas, controle de camadas
- **Análise de densidade**: Top 10 bairros e distribuição por tipo

#### 📈 Visualizações Geradas

- **Gráficos de barras**: Distribuição por categoria e concentração geográfica
- **Rankings**: Bairros ordenados por qualidade média
- **Heatmaps**: Matriz de correlações entre variáveis
- **Scatter plots**: Relações entre popularidade, qualidade e tempos de entrega
- **Mapa interativo**: Visualização geográfica com Folium

#### 🔍 Insights Principais

- **Concentração geográfica** dos melhores estabelecimentos
- **Padrões operacionais** através de correlações temporais
- **Oportunidades de mercado** baseadas em gaps de qualidade
- **Benchmarking competitivo** para diferentes tipos de estabelecimento
- **Recomendações localizadas** para consumidores e empresários

#### ⚠️ Tratamento de Dados

O notebook inclui análise criteriosa da qualidade dos dados:
- **PONTUACAO**: 226 valores ausentes (25.28%)
- **COMENTARIO**: 226 valores ausentes (25.28%) 
- **TEMPO_ESPERA**: 587 valores ausentes (65.66%)

Aplicação de filtros para garantir confiabilidade nas análises, focando em estabelecimentos com dados válidos.

#### 🛠️ Tecnologias Utilizadas

- **Pandas**: Manipulação e análise de dados
- **Matplotlib/Seaborn**: Visualizações estáticas
- **Folium**: Mapeamento interativo
- **NumPy**: Cálculos estatísticos e correlações
