import streamlit as st
import folium
from streamlit_folium import folium_static

def show_map_establishments(df_mapa, titulo="Estabelecimentos"):
    if len(df_mapa) == 0:
        st.warning("Nenhum estabelecimento encontrado com os filtros selecionados.")
        return

    st.subheader(titulo)

    centro_fortaleza = [-3.7319, -38.5267]
    mapa = folium.Map(location=centro_fortaleza, zoom_start=11, tiles='OpenStreetMap')

    cores_folium = {
        'Restaurante': 'red',
        'Padaria': 'blue',
        'Cafeteria': 'green',
        'Drive Thru': 'purple',
        'Delivery De Comida': 'orange'
    }

    simbolo_cor = {
        'red': '🔴', 'blue': '🔵', 'green': '🟢',
        'purple': '🟣', 'orange': '🟠', 'gray': '⚪'
    }

    grupos = {}

    for tipo in df_mapa['TIPO'].unique():
        df_tipo = df_mapa[df_mapa['TIPO'] == tipo]
        cor = cores_folium.get(tipo, 'gray')
        nome_grupo = f"{simbolo_cor.get(cor, '⚪')} {tipo} ({len(df_tipo)})"
        grupos[tipo] = folium.FeatureGroup(name=nome_grupo)

        for _, row in df_tipo.iterrows():
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
