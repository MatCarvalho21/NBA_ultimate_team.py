

import pandas as pd  
import streamlit as st

DICT_ATRIBUTOS = {
    "Arremesso Curto": "CLOSESHOT",
    "Areemesso de Média Distância": "MIDRANGESHOT",
    "Arremesso de 3 Pontos": "THREEPOINTSHOT",
    "Lance Livre": "FREETHROW",
    "Seleção de Arremesso": "SHOTIQ",
    "Consistência Ofensiva": "OFFENSIVECONSISTENCY",
    "Bandeja": "LAYUP",
    "Enterrada Parada": "STANDINGDUNK",
    "Enterrada Em Movimento": "DRIVINGDUNK",
    "Gancho": "POSTHOOK",
    "Controle de Garrafão": "POSTCONTROL",
    "Provocar Faltas": "DRAWFOUL",
    "Hands": "HANDS",
    "Defesa de Garrafão": "INTERIORDEFENSE",
    "Defesa de Perímetro": "PERIMETERDEFENSE",
    "Roubo de Bola": "STEAL",
    "Bloqueio": "BLOCK",
    "Agilidade Lateral": "LATERALQUICKNESS",
    "Inteligência Defensiva": "HELPDEFENSEIQ",
    "Percepção de Passe": "PASSPERCEPTION",
    "Consistência Defensiva": "DEFENSIVECONSISTENCY",
    "Velocidade": "SPEED",
    "Aceleração": "ACCELERATION",
    "Força": "STRENGTH",
    "Salto Vertical": "VERTICAL",
    "Fôlego": "STAMINA",
    "Esforço": "HUSTLE",
    "Durabilidade do Overall": "OVERALLDURABILITY",
    "Precisão de Passe": "PASSACCURACY",
    "Controle de Bola": "BALLHANDLE",
    "Velocidade Com a Bola": "SPEEDWITHBALL",
    "Seleção de Passe": "PASSIQ",
    "Visão de Passe": "PASSVISION",
    "Rebote Ofensivo": "OFFENSIVEREBOUND",
    "Rebote Defensivo": "DEFENSIVEREBOUND"
}

def rakingCreator(dataframe:pd.DataFrame) -> None:
    """
    """

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns(12)
    imagens_urls = list(dataframe["NBA_ID"])
    with col1:
        for i in range(0, 36, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col2:
        for i in range(1, 37, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col3:
        for i in range(2, 38, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col4:
        for i in range(3, 39, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col5:
        for i in range(4, 40, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col6:
        for i in range(5, 41, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col7:
        for i in range(6, 42, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col8:
        for i in range(7, 43, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col9:
        for i in range(8, 44, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col10:
        for i in range(9, 45, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col11:
        for i in range(10, 46, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col12:
        for i in range(11, 47, 12):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")