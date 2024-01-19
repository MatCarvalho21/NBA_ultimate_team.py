

import pandas as pd  
import streamlit as st

DICT_ATRIBUTOS = {
    "Close Shot": "CLOSESHOT",
    "Mid-Range Shot": "MIDRANGESHOT",
    "Three-Point Shot": "THREEPOINTSHOT",
    "Free Throw": "FREETHROW",
    "Shot IQ": "SHOTIQ",
    "Offensive Consistency": "OFFENSIVECONSISTENCY",
    "Layup": "LAYUP",
    "Standing Dunk": "STANDINGDUNK",
    "Driving Dunk": "DRIVINGDUNK",
    "Post Hook": "POSTHOOK",
    "Post Fade": "POSTFADE",
    "Post Control": "POSTCONTROL",
    "Draw Foul": "DRAWFOUL",
    "Hands": "HANDS",
    "Interior Defense": "INTERIORDEFENSE",
    "Perimeter Defense": "PERIMETERDEFENSE",
    "Steal": "STEAL",
    "Block": "BLOCK",
    "Lateral Quickness": "LATERALQUICKNESS",
    "Help Defense IQ": "HELPDEFENSEIQ",
    "Pass Perception": "PASSPERCEPTION",
    "Defensive Consistency": "DEFENSIVECONSISTENCY",
    "Speed": "SPEED",
    "Acceleration": "ACCELERATION",
    "Strength": "STRENGTH",
    "Vertical": "VERTICAL",
    "Stamina": "STAMINA",
    "Hustle": "HUSTLE",
    "Overall Durability": "OVERALLDURABILITY",
    "Pass Accuracy": "PASSACCURACY",
    "Ball Handle": "BALLHANDLE",
    "Speed with Ball": "SPEEDWITHBALL",
    "Pass IQ": "PASSIQ",
    "Pass Vision": "PASSVISION",
    "Offensive Rebound": "OFFENSIVEREBOUND",
    "Defensive Rebound": "DEFENSIVEREBOUND"
}

def rakingCreator(dataframe:pd.DataFrame) -> None:
    """
    """

    col1, col2, col3, col4, col5 = st.columns(5)
    imagens_urls = list(dataframe["NBA_ID"])
    with col1:
        for i in range(0, 15, 5):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col2:
        for i in range(1, 15, 5):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col3:
        for i in range(2, 15, 5):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col4:
        for i in range(3, 15, 5):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")
    with col5:
        for i in range(4, 15, 5):
            st.image(f"main/assets/images/full_cards/full_{imagens_urls[i]}.png")


def colorAttribute(attribute:int) -> None:
    """
    """
    if attribute >= 90:
        st.markdown(f"<p style='color: #122273'>{attribute}</p>", unsafe_allow_html=True)
    elif attribute >= 80:
        st.markdown(f"<p style='color: #008000'>{attribute}</p>", unsafe_allow_html=True)
    elif attribute >= 70:
        st.markdown(f"<p style='color: #00FF00'>{attribute}</p>", unsafe_allow_html=True)
    elif attribute >= 60:
        st.markdown(f"<p style='color: #EDFA00'>{attribute}</p>", unsafe_allow_html=True)
    elif attribute >= 50:
        st.markdown(f"<p style='color: #FFFF00'>{attribute}</p>", unsafe_allow_html=True)
    elif attribute >= 40:
        st.markdown(f"<p style='color: orange'>{attribute}</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p style='color: red'>{attribute}</p>", unsafe_allow_html=True)