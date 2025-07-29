import pandas as pd
from geopy.geocoders import ArcGIS
from geopy.distance import distance
from services.loadData import load_data
from typing import Tuple, Union

def searchDelivery(address: str, rating_range: tuple, wait_time_range: tuple = (0, 60), distance_km: tuple = (0, 10)) -> Tuple[pd.DataFrame, Union[Tuple[float, float], None]]:
    # Carrega os dados
    df = load_data()
    
    # Filtra apenas entregas de comida
    df = df[(df['TIPO'] == "Delivery De Comida")]
    
    # Filtra por avaliação
    min_rating, max_rating = rating_range
    df = df[(df['PONTUACAO'] >= min_rating) & (df['PONTUACAO'] <= max_rating)]
    
    # Filtra por tempo de espera
    min_time, max_time = wait_time_range
    df = df[(df['TEMPO_MIN_M'] >= min_time) & (df['TEMPO_MAX_M'] <= max_time)]
    
    
    min_distance, max_distance = distance_km

    # Se não houver endereço, retorna os dados filtrados sem cálculo de distância
    if not address:
        return df
    

    # Geocodificação
    geolocator = ArcGIS(timeout=10)
    try:
        address += " , Fortaleza"  # garante foco geográfico
        location = geolocator.geocode(address)

        if not location:
            print("Endereço não encontrado. Retornando resultados sem filtro de distância.")
            return df, None
            
        user_coords = (location.latitude, location.longitude)
        
        # Cálculo de distância
        def calculate_distance(row):
            if pd.isna(row['LATITUDE']) or pd.isna(row['LONGITUDE']):
                return float('inf')
            return distance(user_coords, (row['LATITUDE'], row['LONGITUDE'])).km
        
        df['DISTANCIA_KM'] = df.apply(calculate_distance, axis=1)
        df = df[(df['DISTANCIA_KM'] >= min_distance) & (df['DISTANCIA_KM'] <= max_distance)].sort_values('DISTANCIA_KM')
        
        return df, user_coords
        
    except Exception as e:
        print(f"Erro ao geocodificar: {e}")
        return df, None