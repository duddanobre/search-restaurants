def searchDelivery(address, rating, wait_time):
    """
    Função para buscar restaurantes com base nos filtros fornecidos.
    
    Args:
        address (str): Endereço ou localização do usuário.
        rating (tuple): Faixa de avaliação selecionada pelo usuário (min, max).
        wait_time (str): Tempo de espera selecionado pelo usuário.
        
    Returns:
        list: Lista de restaurantes que atendem aos critérios de busca.
    """
    # Aqui você implementaria a lógica de busca, por exemplo, consultando um banco de dados ou uma API
    # Para fins de exemplo, retornaremos uma lista fictícia de restaurantes
    restaurants = [
        {"name": "Restaurante A", "rating": 4.5, "wait_time": 30},
        {"name": "Restaurante B", "rating": 3.8, "wait_time": 45},
        {"name": "Restaurante C", "rating": 5.0, "wait_time": 20},
    ]
    
    # Filtrar os restaurantes com base nos critérios
    filtered_restaurants = [
        restaurant for restaurant in restaurants 
        if rating[0] <= restaurant["rating"] <= rating[1] and 
           (wait_time == 'Menor tempo (min)' and restaurant["wait_time"] <= 30 or 
            wait_time == 'Maior tempo (min)' and restaurant["wait_time"] >= 30)
    ]
    
    return filtered_restaurants