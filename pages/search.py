import streamlit as st

from components.sidebar import sidebar

from services.searchDelivery import searchDelivery

def handle_delivery_search():
    address = st.session_state.delivery_address
    rating = st.session_state.delivery_rating
    wait_time = st.session_state.delivery_wait_time
    searchDelivery(address, rating, wait_time)

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
            st.slider("Avaliação", 0, 5, (0, 5), step=1, help="Selecione a faixa de avaliação desejada", key="delivery_rating")

        with col2:
            st.selectbox("Tempo de Espera (minutos)", ['Menor tempo (min)', 'Maior tempo (min)'], index=0, help="Selecione o tempo de espera máximo desejado", key="delivery_wait_time")
        
        submitted = st.form_submit_button("🔍 Buscar", on_click=handle_delivery_search)

        if submitted:
            st.success("Buscando restaurantes com os filtros selecionados...")

with tab2:
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
        st.slider("Avaliação", 0, 5, (0, 5), step=1, help="Selecione a faixa de avaliação desejada", key="dine_in_rating")

    with col2:
        st.selectbox("Tempo de Espera (minutos)", ['Menor tempo (min)', 'Maior tempo (min)'], index=0, help="Selecione o tempo de espera máximo desejado", key="dine_in_wait_time")

