import streamlit as st
import pandas as pd  

def pg_lineups():
    """
    """

    #abrindo o dataframe com todos os dados
    dataframe_players = pd.read_csv("main/assets/database/players.csv")
    dataframe_players = dataframe_players.sort_values("OVERALLATTRIBUTE", ascending=False).reset_index(drop=True)

    dataframe_teams = pd.read_csv("main/assets/database/teams.csv")
    dataframe_teams = dataframe_teams.sort_values("FULL_NAME").reset_index(drop=True).reset_index(drop=True)


    st.markdown("<h1 style='text-align: center;'>Montador de Escalações</h1>", unsafe_allow_html=True)
    st.markdown("---")
    quadra_selecionada = st.selectbox(label="Time Mandante:",
                          options=list(dataframe_teams["FULL_NAME"]),
                          index=None,
                          placeholder="selecione a quadra")
    if quadra_selecionada != None:
        quadra_selecionada = (quadra_selecionada.lower()).replace(" ", "_")
    else:
        quadra_selecionada = "padrao"
    col1, col2 = st.columns(2)
    players = list(dataframe_players["FULL_NAME"])
    with col1:
        PG1 = st.selectbox(label="PG Time 1:", options=players, index=None, placeholder="selecione o jogador")
        SG1 = st.selectbox(label="SG Time 1:", options=players, index=None, placeholder="selecione o jogador")
        SF1 = st.selectbox(label="SF Time 1:", options=players, index=None, placeholder="selecione o jogador")
        PF1 = st.selectbox(label="PF Time 1:", options=players, index=None, placeholder="selecione o jogador")
        CE1 = st.selectbox(label="CE Time 1:", options=players, index=None, placeholder="selecione o jogador")
    with col2:
        PG2 = st.selectbox(label="PG Time 2:", options=players, index=None, placeholder="selecione o jogador")
        SG2 = st.selectbox(label="SG Time 2:", options=players, index=None, placeholder="selecione o jogador")
        SF2 = st.selectbox(label="SF Time 2:", options=players, index=None, placeholder="selecione o jogador")
        PF2 = st.selectbox(label="PF Time 2:", options=players, index=None, placeholder="selecione o jogador")
        CE2 = st.selectbox(label="CE Time 2:", options=players, index=None, placeholder="selecione o jogador")
    
    st.markdown("---")

pg_lineups()