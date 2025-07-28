import streamlit as st

from components.sidebar import sidebar
from components.showMapEstablishments import show_map_establishments

from services.searchDelivery import searchDelivery
from services.searchDineIn import searchDineIn


def handle_delivery_search():
    address = st.session_state.delivery_address
    rating = st.session_state.delivery_rating
    wait_time_range = st.session_state.delivery_wait_range

    results = searchDelivery(address, rating, wait_time_range)

    if results.empty:
        st.success("Buscando restaurantes com os filtros selecionados...")
        st.warning("Nenhum restaurante encontrado com os filtros selecionados.")
    else:
        st.success(f"{len(results)} restaurantes encontrados.")
        show_map_establishments(results)

def handle_dine_in_search():
    address = st.session_state.dine_in_address
    rating = st.session_state.dine_in_rating
    wait_time_range = st.session_state.dine_in_wait_range

    results = searchDineIn(address, rating, wait_time_range)

    if results.empty:
        st.success("Buscando restaurantes com os filtros selecionados...")
        st.warning("Nenhum restaurante encontrado com os filtros selecionados.")
    else:
        st.success(f"{len(results)} restaurantes encontrados.")
        show_map_establishments(results)


sidebar()

st.markdown("""
    <style>
    .custom-title {
        color: #6e6e6e; /* cinza */
        font-size: 32px;
        font-weight: 300; /* mais fino */
        margin-bottom: 0.5em;
    }
    .custom-sub {
        font-size: 18px;
        color: #8a8a8a;
        font-weight: 300;
    }
            
    [data-testid="stForm"] {
        background-color: transparent;
        border: none;
        box-shadow: none;
        padding: 0;
    }
            
    .search-button-container {
    display: flex;
    justify-content: flex-end;
    margin-top: 1em;
    }
            
    .search-button-container button {
        background-color: #0d6efd;
        color: white;
        border: none;
        padding: 0.5em 1.2em;
        font-size: 16px;
        border-radius: 6px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-title">🔍 Buscar Restaurante</div>', unsafe_allow_html=True)

st.markdown('<div class="custom-sub">Você pode buscar restaurantes delivery ou consumo no local, filtrando por localização, avaliação e tempo de espera.</div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Restaurantes Delivery", "Restaurantes Consumo no Local"])

with tab1:
    with st.form("delivery_form"):
        st.markdown("""
            <div class="custom-sub">
            Aqui você pode buscar por restaurantes que oferecem serviço de entrega. Utilize os filtros abaixo para encontrar o que melhor atende às suas necessidades.
            <ul>
                <li><strong>Localização:</strong> Insira seu endereço ou utilize sua localização atual.</li>
                <li><strong>Avaliação:</strong> Filtre por avaliações de clientes.</li>
                <li><strong>Tempo de Espera:</strong> Escolha o tempo de espera ideal para você.</li>
            </ul>
            </div>
        """, unsafe_allow_html=True)

        st.text_input("Endereço", placeholder="Digite seu endereço ou use sua localização atual", key="delivery_address")

        col1, col2 = st.columns(2)
        with col1:
            st.slider("Avaliação", 0.0, 5.0, (0.0, 5.0), step=0.1, key="delivery_rating", help="Selecione a faixa de avaliação desejada")

        with col2:
            st.slider("Tempo de Espera (minutos)", min_value=0, max_value=120, value=(0, 60), step=5, help="Selecione a faixa de tempo de espera desejada", key="delivery_wait_range")
        
        submitted_delivery = st.form_submit_button("🔍 Buscar")

    if submitted_delivery:
        handle_delivery_search()

with tab2:
    with st.form("dine_in_form"):
        st.markdown("""
        <div class="custom-sub">
            Aqui você pode buscar por restaurantes onde é possível consumir no local. Utilize os filtros abaixo para encontrar o que melhor atende às suas necessidades.
            <ul>
                <li><strong>Localização:</strong> Insira seu endereço ou utilize sua localização atual.</li>
                <li><strong>Avaliação:</strong> Filtre por avaliações de clientes.</li>
                <li><strong>Tempo de Espera:</strong> Escolha o tempo de espera ideal para você.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.text_input("Endereço", placeholder="Digite seu endereço ou use sua localização atual", key="dine_in_address")

        col1, col2 = st.columns(2)
        with col1:
            st.slider("Avaliação", 0.0, 5.0, (0.0, 5.0), step=0.1, key="dine_in_rating", help="Selecione a faixa de avaliação desejada")

        with col2:
            st.slider("Tempo de Espera (minutos)", min_value=0, max_value=120, value=(0, 60), step=5, help="Selecione a faixa de tempo de espera desejada", key="dine_in_wait_range")

        submitted_dine_in = st.form_submit_button("🔍 Buscar")

        if submitted_dine_in:
            handle_dine_in_search()

