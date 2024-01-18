import streamlit as st
import pandas as pd  

def main():
    """
    """

    #abrindo o dataframe com todos os dados
    dataframe = pd.read_csv("main/assets/database/players.csv")
    dataframe = dataframe.sort_values("OVERALLATTRIBUTE", ascending=False).reset_index(drop=True)
    
    #título da página
    st.title("NBA Ultimate Team")

    #barra de pesquisa
    option = st.selectbox(label="",
                          options=list(dataframe["FULL_NAME"]),
                          index=None,
                          placeholder="busque um jogador")
    

    #subtítulo da página
    st.header("TOP PLAYERS")

    #top 100 jogadores
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


if __name__ == "__main__":
    main()