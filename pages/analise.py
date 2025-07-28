import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import folium
from streamlit_folium import folium_static

from components.sidebar import sidebar

sidebar()

# Configuração da página
st.set_page_config(page_title="Análise de Mercado", layout="wide")

# Título principal
st.title("📊 Análise Completa do Mercado de Estabelecimentos Alimentares em Fortaleza")

# Carregamento dos dados
@st.cache_data
def load_data():
    return pd.read_csv('database/dadosTratados/df_final_comGeo.csv')

try:
    df_final = load_data()
    
    # Sidebar com filtros
    st.sidebar.header("Filtros de Análise")
    tipos_selecionados = st.sidebar.multiselect(
        "Tipos de Estabelecimento:",
        options=df_final['TIPO'].unique(),
        default=df_final['TIPO'].unique()
    )
    
    # Filtrar dados
    df_filtrado = df_final[df_final['TIPO'].isin(tipos_selecionados)]
    
    # Abas principais
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Panorama Geral", 
        "🏆 Qualidade por Região", 
        "🔍 Análise de Correlações", 
        "🗺️ Mapeamento Geográfico",
        "📋 Insights e Recomendações"
    ])
    
    with tab1:
        st.header("Panorama Geral do Mercado")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total de Estabelecimentos", len(df_filtrado))
        with col2:
            st.metric("Bairros Únicos", df_filtrado['BAIRRO'].nunique())
        with col3:
            st.metric("Pontuação Média", f"{df_filtrado['PONTUACAO'].mean():.2f}")
        with col4:
            zeros = len(df_filtrado[df_filtrado['PONTUACAO'] == 0])
            st.metric("Dados Ausentes", f"{100*zeros/len(df_filtrado):.1f}%")
        
        st.markdown("---")
        
        # Gráfico 1: Distribuição por categoria
        st.subheader("Distribuição de Estabelecimentos por Categoria")
        
        fig1, ax1 = plt.subplots(figsize=(12, 6))
        tipo_counts = df_filtrado['TIPO'].value_counts()
        bars = ax1.bar(tipo_counts.index, tipo_counts.values, 
                      color=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#593E2E'])
        
        for bar, value in zip(bars, tipo_counts.values):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
                    str(value), ha='center', va='bottom', fontweight='bold')
        
        ax1.set_title('Distribuição de Estabelecimentos por Categoria', fontweight='bold')
        ax1.set_xlabel('Categoria de Estabelecimento')
        ax1.set_ylabel('Quantidade')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig1)
        
        st.markdown(f"""
        **Insights de Mercado:**
        -  **Segmento dominante**: {tipo_counts.index[0]} com {tipo_counts.iloc[0]} unidades
        -  **Menor representação**: {tipo_counts.index[-1]} com {tipo_counts.iloc[-1]} unidades
        -  **Diferença de mercado**: {tipo_counts.iloc[0] - tipo_counts.iloc[-1]} unidades entre maior e menor segmento
        """)
        
        st.markdown("---")
        
        # Gráfico 2: Concentração geográfica
        st.subheader("Concentração Geográfica dos Estabelecimentos")
        
        fig2, ax2 = plt.subplots(figsize=(12, 8))
        bairro_counts = df_filtrado['BAIRRO'].value_counts().head(15)
        bars2 = ax2.barh(range(len(bairro_counts)), bairro_counts.values, 
                        color=plt.cm.viridis(np.linspace(0, 1, len(bairro_counts))))
        
        for i, (bar, value) in enumerate(zip(bars2, bairro_counts.values)):
            ax2.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
                    str(value), ha='left', va='center', fontweight='bold')
        
        ax2.set_yticks(range(len(bairro_counts)))
        ax2.set_yticklabels(bairro_counts.index)
        ax2.set_title('Top 15 Bairros por Volume de Estabelecimentos', fontweight='bold')
        ax2.set_xlabel('Quantidade de Estabelecimentos')
        ax2.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig2)
        
        concentracao = (bairro_counts.sum() / len(df_filtrado)) * 100
        st.markdown(f"""
        **Análise de Concentração:**
        -  **Bairro líder**: {bairro_counts.index[0]} com {bairro_counts.iloc[0]} estabelecimentos
        -  **Concentração**: Top 15 bairros representam {concentracao:.1f}% do mercado total
        -  **Padrão**: Mercado altamente concentrado nos centros urbanos
        """)
    
    with tab2:
        st.header("🏆 Análise de Qualidade por Região")
        
        # Ranking geral
        st.subheader("Ranking Geral de Bairros por Qualidade")
        
        bairro_analysis = df_filtrado.groupby('BAIRRO').agg({
            'PONTUACAO': 'mean',
            'NOME': 'count'
        }).reset_index()
        bairro_analysis = bairro_analysis[bairro_analysis['NOME'] >= 10].sort_values('PONTUACAO', ascending=True)
        
        fig3, ax3 = plt.subplots(figsize=(12, 10))
        bars3 = ax3.barh(range(len(bairro_analysis)), bairro_analysis['PONTUACAO'], 
                        color=plt.cm.RdYlGn(bairro_analysis['PONTUACAO']/5))
        
        ax3.set_yticks(range(len(bairro_analysis)))
        ax3.set_yticklabels(bairro_analysis['BAIRRO'], fontsize=10)
        ax3.set_xlabel('Pontuação Média')
        ax3.set_title('Ranking Geral de Bairros por Qualidade (min. 3 estabelecimentos)')
        ax3.axvline(x=df_filtrado['PONTUACAO'].mean(), color='red', linestyle='--', alpha=0.7, label='Média Geral')
        
        for i, row in bairro_analysis.iterrows():
            ax3.text(row['PONTUACAO'] + 0.05, list(bairro_analysis.index).index(i), 
                    f"{row['PONTUACAO']:.2f}", va='center', fontsize=9)
        
        ax3.legend()
        plt.tight_layout()
        st.pyplot(fig3)
        
        if len(bairro_analysis) >= 3:
            top_3 = bairro_analysis.tail(3)['BAIRRO'].tolist()
            bottom_3 = bairro_analysis.head(3)['BAIRRO'].tolist()
            st.markdown(f"""
            **Ranking de Qualidade:**
            -  **Top 3 bairros**: {', '.join(reversed(top_3))}
            -  **Menores pontuações**: {', '.join(bottom_3)}
            """)
        
        st.markdown("---")
        
        # Análise por tipo
        st.subheader("Análise Específica por Tipo de Estabelecimento")
        
        tipos_para_analisar = df_filtrado['TIPO'].unique()
        cores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
        
        # Criar subplots dinamicamente
        n_tipos = len(tipos_para_analisar)
        cols = 3
        rows = (n_tipos + cols - 1) // cols
        
        fig4, axes = plt.subplots(rows, cols, figsize=(20, 6*rows))
        if rows == 1:
            axes = [axes] if n_tipos == 1 else axes
        else:
            axes = axes.flatten()
        
        resultados_por_tipo = {}
        
        for idx, tipo in enumerate(tipos_para_analisar):
            if idx < len(axes):
                ax = axes[idx]
                df_tipo = df_filtrado[df_filtrado['TIPO'] == tipo]
                
                if len(df_tipo) > 0:
                    bairro_tipo = df_tipo.groupby('BAIRRO').agg({
                        'PONTUACAO': 'mean',
                        'NOME': 'count'
                    }).reset_index()
                    
                    bairro_tipo = bairro_tipo[bairro_tipo['NOME'] >= 3].sort_values('PONTUACAO', ascending=True)
                    
                    if len(bairro_tipo) > 0:
                        cor = cores[idx % len(cores)]
                        bars = ax.barh(range(len(bairro_tipo)), bairro_tipo['PONTUACAO'], 
                                      color=cor, alpha=0.7)
                        
                        ax.set_yticks(range(len(bairro_tipo)))
                        ax.set_yticklabels(bairro_tipo['BAIRRO'], fontsize=9)
                        ax.set_xlabel('Pontuação Média')
                        ax.set_title(f'{tipo}\n({len(df_tipo)} estabelecimentos)', fontweight='bold')
                        ax.axvline(x=df_tipo['PONTUACAO'].mean(), color='red', linestyle='--', alpha=0.7)
                        ax.grid(axis='x', alpha=0.3)
                        
                        if len(bairro_tipo) > 0:
                            resultados_por_tipo[tipo] = {
                                'melhor': bairro_tipo.iloc[-1]['BAIRRO'],
                                'pior': bairro_tipo.iloc[0]['BAIRRO'],
                                'total': len(df_tipo),
                                'bairros_analisados': len(bairro_tipo)
                            }
        
        # Remover subplots vazios
        for idx in range(len(tipos_para_analisar), len(axes)):
            fig4.delaxes(axes[idx])
        
        plt.tight_layout()
        st.pyplot(fig4)
        
        if resultados_por_tipo:
            st.markdown("**Líderes por Categoria:**")
            for tipo, dados in resultados_por_tipo.items():
                st.markdown(f"""
                - **{tipo}**:  {dados['melhor']} (melhor) |  {dados['pior']} (menor pontuação)  
                  _{dados['total']} estabelecimentos em {dados['bairros_analisados']} bairros_
                """)
    
    with tab3:
        st.header("Análise de Correlações e Padrões")
        
        # Matriz de correlação
        st.subheader("Matriz de Correlação - Variáveis Numéricas")
        
        colunas_numericas = ['PONTUACAO', 'NUM_COMENTARIO', 'TEMPO_MIN_M', 'TEMPO_MAX_M', 'LATITUDE', 'LONGITUDE']
        df_corr = df_filtrado[colunas_numericas].dropna()
        
        if len(df_corr) > 0:
            fig5, ax5 = plt.subplots(figsize=(10, 8))
            correlation_matrix = df_corr.corr()
            mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
            
            sns.heatmap(correlation_matrix, 
                       mask=mask,
                       annot=True, 
                       cmap='RdBu_r', 
                       center=0,
                       fmt='.3f',
                       square=True,
                       cbar_kws={'label': 'Correlação'},
                       ax=ax5)
            
            ax5.set_title('Matriz de Correlação - Todas as Variáveis Numéricas')
            plt.tight_layout()
            st.pyplot(fig5)
        
        st.markdown("---")
        
        # Análise de tempos
        st.subheader("Correlação: Tempo Mínimo vs Máximo de Entrega")
        
        df_tempo = df_filtrado[(df_filtrado['TEMPO_MIN_M'] > 0) & (df_filtrado['TEMPO_MAX_M'] > 0)]
        
        if len(df_tempo) > 0:
            fig6, ax6 = plt.subplots(figsize=(12, 8))
            
            scatter = ax6.scatter(df_tempo['TEMPO_MIN_M'], df_tempo['TEMPO_MAX_M'], 
                                alpha=0.6, s=60, c=df_tempo['PONTUACAO'], 
                                cmap='RdYlGn', edgecolors='black', linewidth=0.3)
            
            # Linha de tendência
            z = np.polyfit(df_tempo['TEMPO_MIN_M'], df_tempo['TEMPO_MAX_M'], 1)
            p = np.poly1d(z)
            ax6.plot(df_tempo['TEMPO_MIN_M'], p(df_tempo['TEMPO_MIN_M']), "r--", alpha=0.8, linewidth=2)
            
            ax6.set_xlabel('Tempo Mínimo (minutos)')
            ax6.set_ylabel('Tempo Máximo (minutos)')
            ax6.set_title('Correlação: Tempo Mínimo vs Máximo de Entrega\n(cor representa a qualidade)')
            ax6.grid(True, alpha=0.3)
            
            plt.colorbar(scatter, ax=ax6, label='Pontuação')
            plt.tight_layout()
            st.pyplot(fig6)
            
            # Estatísticas dos tempos
            correlacao_tempo = df_tempo['TEMPO_MIN_M'].corr(df_tempo['TEMPO_MAX_M'])
            diferenca_media = (df_tempo['TEMPO_MAX_M'] - df_tempo['TEMPO_MIN_M']).mean()
            
            st.markdown(f"""
            **Análise dos Tempos de Entrega:**
            - **Correlação MIN vs MAX**: {correlacao_tempo:.3f}
            - **Diferença média**: {diferenca_media:.1f} minutos
            - **Tempo mínimo mais comum**: {df_tempo['TEMPO_MIN_M'].mode().iloc[0]:.0f} min
            - **Tempo máximo mais comum**: {df_tempo['TEMPO_MAX_M'].mode().iloc[0]:.0f} min
            """)
        
        st.markdown("---")
        
        # Popularidade vs Qualidade
        st.subheader("Popularidade vs Qualidade por Tipo")
        
        df_validos = df_filtrado[(df_filtrado['NUM_COMENTARIO'] > 0) & (df_filtrado['PONTUACAO'] > 0)]
        
        if len(df_validos) > 0:
            fig7, ax7 = plt.subplots(figsize=(14, 8))
            
            tipos = df_validos['TIPO'].unique()
            cores_scatter = plt.cm.Set3(np.linspace(0, 1, len(tipos)))
            
            for i, tipo in enumerate(tipos):
                df_tipo = df_validos[df_validos['TIPO'] == tipo]
                ax7.scatter(df_tipo['NUM_COMENTARIO'], df_tipo['PONTUACAO'], 
                           alpha=0.7, s=60, label=tipo, color=cores_scatter[i])
            
            ax7.set_xlabel('Número de Comentários (escala logarítmica)')
            ax7.set_ylabel('Pontuação de Qualidade')
            ax7.set_title('Popularidade vs Qualidade por Tipo de Estabelecimento')
            ax7.set_xscale('log')
            ax7.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            ax7.grid(True, alpha=0.2)
            
            plt.tight_layout()
            st.pyplot(fig7)
            
            st.markdown("**Análise Popularidade vs Qualidade:**")
            for tipo in tipos:
                df_tipo = df_validos[df_validos['TIPO'] == tipo]
                if len(df_tipo) > 0:
                    corr = df_tipo['NUM_COMENTARIO'].corr(df_tipo['PONTUACAO'])
                    st.markdown(f"- **{tipo}**: Correlação = {corr:.3f} ({len(df_tipo)} estabelecimentos)")
    
    with tab4:
        st.header("Mapeamento Geográfico Interativo")
        
        # Filtro de pontuação para o mapa
        min_pontuacao = st.slider("Pontuação mínima para exibir no mapa:", 0.0, 5.0, 3.5, 0.1)
        df_mapa = df_filtrado[df_filtrado['PONTUACAO'] >= min_pontuacao].copy()
        
        if len(df_mapa) > 0:
            # Mapa interativo
            st.subheader(f"Estabelecimentos com Pontuação ≥ {min_pontuacao}")
            
            centro_fortaleza = [-3.7319, -38.5267]
            mapa = folium.Map(location=centro_fortaleza, zoom_start=11, tiles='OpenStreetMap')
            
            cores_folium = {
                'Restaurante': 'red',
                'Padaria': 'blue', 
                'Cafeteria': 'green',
                'Drive Thru': 'purple',
                'Delivery De Comida': 'orange'
            }
            
            grupos = {}
            for tipo in df_mapa['TIPO'].unique():
                df_tipo = df_mapa[df_mapa['TIPO'] == tipo]
                simbolo_cor = {'red': '🔴', 'blue': '🔵', 'green': '🟢', 'purple': '🟣', 'orange': '🟠'}
                cor = cores_folium.get(tipo, 'gray')
                
                nome_grupo = f"{simbolo_cor.get(cor, '⚪')} {tipo} ({len(df_tipo)})"
                grupos[tipo] = folium.FeatureGroup(name=nome_grupo)
                
                for idx, row in df_tipo.iterrows():
                    popup_text = f"""
                    <b>{row['NOME']}</b><br>
                    Tipo: {row['TIPO']}<br>
                    Bairro: {row['BAIRRO']}<br>
                    Pontuação: {row['PONTUACAO']:.1f}<br>
                    Comentários: {row['NUM_COMENTARIO']}<br>
                    Tempo: {row['TEMPO_MIN_M']}-{row['TEMPO_MAX_M']} min
                    """
                    
                    folium.Marker(
                        location=[row['LATITUDE'], row['LONGITUDE']],
                        popup=folium.Popup(popup_text, max_width=250),
                        tooltip=f"{row['NOME']} - {row['PONTUACAO']:.1f}⭐",
                        icon=folium.Icon(color=cor, icon='cutlery', prefix='fa')
                    ).add_to(grupos[tipo])
                
                grupos[tipo].add_to(mapa)
            
            folium.LayerControl(position='topright', collapsed=False).add_to(mapa)
            folium_static(mapa, width=1200, height=600)
            
            st.markdown("---")
            
            # Análise de densidade geográfica
            st.subheader("Análise de Densidade Geográfica")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Top bairros
                bairros_top = df_mapa['BAIRRO'].value_counts().head(10)
                
                fig8, ax8 = plt.subplots(figsize=(10, 8))
                bars8 = ax8.barh(range(len(bairros_top)), bairros_top.values, 
                                color=plt.cm.viridis(np.linspace(0, 1, len(bairros_top))))
                
                ax8.set_yticks(range(len(bairros_top)))
                ax8.set_yticklabels(bairros_top.index)
                ax8.set_xlabel('Quantidade de Estabelecimentos Bem Avaliados')
                ax8.set_title(f'Top 10 Bairros - Pontuação ≥ {min_pontuacao}')
                ax8.grid(axis='x', alpha=0.3)
                
                for i, (bar, value) in enumerate(zip(bars8, bairros_top.values)):
                    ax8.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, 
                            str(value), ha='left', va='center', fontweight='bold')
                
                plt.tight_layout()
                st.pyplot(fig8)
            
            with col2:
                # Distribuição por tipo nos top bairros
                top_5_bairros = bairros_top.head(5).index
                df_top_bairros = df_mapa[df_mapa['BAIRRO'].isin(top_5_bairros)]
                
                if len(df_top_bairros) > 0:
                    cores_tipo = {'Restaurante': '#FF6B6B', 'Padaria': '#4ECDC4', 'Cafeteria': '#45B7D1', 'Drive Thru': '#96CEB4', 'Delivery De Comida': '#FECA57'}
                    
                    fig9, ax9 = plt.subplots(figsize=(10, 8))
                    tipo_bairro_pivot = df_top_bairros.groupby(['BAIRRO', 'TIPO']).size().unstack(fill_value=0)
                    tipo_bairro_pivot.plot(kind='bar', stacked=True, ax=ax9,
                                          color=[cores_tipo.get(col, '#999999') for col in tipo_bairro_pivot.columns])
                    
                    ax9.set_title('Distribuição de Tipos nos Top 5 Bairros')
                    ax9.set_xlabel('Bairro')
                    ax9.set_ylabel('Quantidade')
                    ax9.legend(title='Tipo', bbox_to_anchor=(1.05, 1), loc='upper left')
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    st.pyplot(fig9)
            
            # Estatísticas finais
            st.markdown(f"""
            **Análise Geográfica:**
            - **Total de estabelecimentos bem avaliados**: {len(df_mapa)}
            - **Bairros representados**: {df_mapa['BAIRRO'].nunique()}
            - **Concentração no top 5 bairros**: {len(df_top_bairros)/len(df_mapa)*100:.1f}%
            - **Pontuação média geral**: {df_mapa['PONTUACAO'].mean():.2f}
            """)
        else:
            st.warning(f"Nenhum estabelecimento encontrado com pontuação ≥ {min_pontuacao}")
    
    with tab5:
        st.header("Insights e Recomendações de Negócio")
        
        # Limitações dos dados
        st.subheader("Limitações dos Dados Atuais")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Quantidade de Informações Ausentes:**
            - PONTUACAO: 226 valores (25.28%)
            - COMENTARIO: 226 valores (25.28%)
            - ENDERECO: 1 valor (0.11%)
            - LOCAL: 115 valores (12.86%)
            - TEMPO_ESPERA: 587 valores (65.66%)
            """)
        
        with col2:
            st.markdown("""
            **Interpretação:**
            - Pontuações 0.0 = dados ausentes
            - Análises focam em dados válidos
            - Filtros aplicados para maior confiabilidade
            - Tratamento cuidadoso necessário
            """)
        
        st.markdown("---")
        
        # Recomendações por perfil
        st.subheader("Recomendações por Perfil")
        
        tab_consumidor, tab_empresario, tab_investidor = st.tabs(["👥 Consumidor", "🏢 Empresário", "💰 Investidor"])

        with tab_consumidor:
            if len(bairro_analysis) > 0:
                melhores_bairros = bairro_analysis.tail(5)['BAIRRO'].tolist()
                
                st.markdown("""
                **Para Consumidores:**
                
                🏆 **Melhores bairros para comer bem:**
                """)
                
                for bairro in reversed(melhores_bairros):
                    st.markdown(f"- {bairro}")
                
                st.markdown("""
                **Dicas:**
                - Prefira estabelecimentos com mais de 50 comentários
                - Verifique tempos de entrega antes de pedir
                - Explore diferentes tipos nos bairros bem avaliados
                """)

        with tab_empresario:
            if len(df_filtrado) > 0:
                segmento_dominante = df_filtrado['TIPO'].value_counts().index[0]
                menor_competicao = df_filtrado['TIPO'].value_counts().index[-1]
                
                st.markdown(f"""
                **Para Empresários:**
                
                **Oportunidades de Mercado:**
                - Segmento saturado: {segmento_dominante}
                - Menor competição: {menor_competicao}
                - Foco em qualidade vs quantidade

                **Estratégias:**
                - Invista em bairros com alta demanda e baixa oferta
                - Mantenha consistência nos tempos de entrega
                - Busque avaliações positivas constantes
                """)
        
        with tab_investidor:
            if len(df_filtrado) > 0:
                concentracao_top10 = df_filtrado['BAIRRO'].value_counts().head(10).sum() / len(df_filtrado) * 100
                
                st.markdown(f"""
                **Para Investidores:**
                
                **Análise de Mercado:**
                - Concentração geográfica: {concentracao_top10:.1f}% em 10 bairros
                - Mercado fragmentado com oportunidades
                - ROI potencial em bairros emergentes

                **Recomendações:**
                - Diversifique entre tipos de estabelecimento
                - Monitore correlação popularidade x qualidade
                - Invista em tecnologia para gestão de tempos
                """)
        
        st.markdown("---")
        
        # Metodologia
        st.subheader("🔬 Metodologia Aplicada")
        st.markdown("""
        **Critérios de Análise:**
        - Filtro de confiabilidade: Apenas bairros com 10+ estabelecimentos
        - Tratamento de dados: Exclusão de valores ausentes em análises críticas
        - Múltiplas perspectivas: Rankings, correlações, distribuições geográficas
        - Visualizações interativas: Mapeamento com Folium para exploração detalhada
        
        **Ferramentas Utilizadas:**
        - Pandas: Manipulação e análise de dados
        - Matplotlib/Seaborn: Visualizações estáticas
        - Folium: Mapeamento interativo
        - Streamlit: Interface web interativa
        """)

except FileNotFoundError:
    st.error("❌ Arquivo de dados não encontrado. Verifique se o arquivo 'database/dadosTratados/df_final_comGeo.csv' existe.")
except Exception as e:
    st.error(f"❌ Erro ao carregar os dados: {str(e)}")