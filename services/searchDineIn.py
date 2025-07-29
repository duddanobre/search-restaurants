import pandas as pd
from geopy.geocoders import ArcGIS
from geopy.distance import distance
from services.loadData import load_data

def searchDineIn(address: str, rating_range: tuple, wait_time_range: tuple = (0, 60), max_distance_km: float = 3):
    # Carrega os dados
    df = load_data()
    
    # Filtra estabelecimentos que não são delivery (restaurantes para comer no local)
    df = df[(df['TIPO'] != "Delivery De Comida")]
    
    # Filtra por avaliação
    min_rating, max_rating = rating_range
    df = df[(df['PONTUACAO'] >= min_rating) & (df['PONTUACAO'] <= max_rating)]
    
    # Filtra por tempo de espera
    min_time, max_time = wait_time_range
    df = df[(df['TEMPO_MIN_M'] >= min_time) & (df['TEMPO_MAX_M'] <= max_time)]
    
    # Se não houver endereço, retorna os dados filtrados sem cálculo de distância
    if not address:
        return df
    
    # Geocodificação do endereço do usuário
    geolocator = ArcGIS(timeout=10)
    try:
        location = geolocator.geocode(address)
        if not location:
            print("Endereço não encontrado. Retornando resultados sem filtro de distância.")
            return df
            
        user_lat, user_lon = location.latitude, location.longitude
        
        # Calcula distância para cada estabelecimento
        def calculate_distance(row):
            if pd.isna(row['LATITUDE']) or pd.isna(row['LONGITUDE']):
                return float('inf')  # Retorna infinito se não tiver coordenadas
            return distance((user_lat, user_lon), (row['LATITUDE'], row['LONGITUDE'])).km
        
        df['DISTANCIA_KM'] = df.apply(calculate_distance, axis=1)
        
        # Filtra por distância máxima
        df = df[df['DISTANCIA_KM'] <= max_distance_km]
        
        # Ordena por distância (opcional) - mais próximos primeiro
        df = df.sort_values('DISTANCIA_KM')
        
    except Exception as e:
        print(f"Erro ao geocodificar endereço: {e}. Retornando resultados sem filtro de distância.")
    
    return df