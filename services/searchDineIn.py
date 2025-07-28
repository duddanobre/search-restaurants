import pandas as pd
from services.loadData import load_data

def searchDineIn(address: str, rating_range: tuple, wait_time_range: tuple = (0, 60)):
    df = load_data()

    df = df[(df['TIPO'] != "Delivery De Comida")]

    min_rating, max_rating = rating_range
    df = df[(df['PONTUACAO'] >= min_rating) & (df['PONTUACAO'] <= max_rating)]

    if address:
        address_lower = address.lower()
        df = df[df['ENDERECO'].str.lower().str.contains(address_lower) | df['BAIRRO'].str.lower().str.contains(address_lower)]

    min_time, max_time = wait_time_range
    df = df[(df['TEMPO_MIN_M'] >= min_time) & (df['TEMPO_MAX_M'] <= max_time)]

    return df

