import streamlit as st
import folium
from streamlit_folium import folium_static
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.geometry import mapping
import geojson

def show_map_establishments(df_mapa, titulo="Estabelecimentos", user_location=None, user_address=None, distance_range=[0,10]):
    if len(df_mapa) == 0 and not user_location:
        st.warning("Nenhum estabelecimento encontrado com os filtros selecionados.")
        return

    st.subheader(titulo)

    # Define o centro do mapa: usa a localização do usuário se disponível, senão usa Fortaleza
    if user_location:
        mapa_center = [user_location[0], user_location[1]]
        zoom_start = 14  # Zoom mais próximo para focar no local do usuário
    else:
        mapa_center = [-3.7319, -38.5267]  # Centro de Fortaleza
        zoom_start = 11

    mapa = folium.Map(location=mapa_center, zoom_start=zoom_start, tiles='OpenStreetMap')

    # Adiciona o marcador do usuário (se fornecido)
    if user_location:
        popup_text = f"<b>📍 Seu Local</b><br>{user_address}" if user_address else "📍 Seu Local"
        
        folium.Marker(
            location=user_location,
            popup=folium.Popup(popup_text, max_width=250),
            tooltip="Você está aqui",
            icon=folium.Icon(color='black', icon='user', prefix='fa')
        ).add_to(mapa)

        min_dist = distance_range[0] * 1000  # em metros
        max_dist = distance_range[1] * 1000

        # Criação do anel usando shapely
        lat, lon = user_location  # folium usa (lat, lon), shapely (lon, lat)
        center = Point(lon, lat)

        # Conversão aproximada de metros para graus: 1 grau ~ 111320 metros
        outer_circle = center.buffer(max_dist / 111320)
        inner_circle = center.buffer(min_dist / 111320)

        ring = Polygon(outer_circle.exterior.coords, [inner_circle.exterior.coords])
        geojson_data = geojson.Feature(geometry=mapping(ring), properties={})

        # Cria grupo com nome para aparecer na legenda
        anel_group = folium.FeatureGroup(name=f"⚫ Área de busca: {distance_range[0]}km a {distance_range[1]}km")

        folium.GeoJson(
            geojson_data,
            style_function=lambda x: {
                'fillColor': '#3186cc',
                'color': '#3186cc',
                'weight': 1,
                'fillOpacity': 0.2
            },
            tooltip=f"Área de busca: {distance_range[0]}km a {distance_range[1]}km"
        ).add_to(anel_group)
        anel_group.add_to(mapa)

    # Configurações de cores e símbolos (mantido da versão original)
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

    # Adiciona os estabelecimentos ao mapa (mantido da versão original)
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
    folium_static(mapa, width=1200, height=500)
    st.markdown("---")