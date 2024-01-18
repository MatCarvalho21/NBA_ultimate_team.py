import streamlit as st
import pandas as pd  
from functions import rakingCreator, DICT_ATRIBUTOS

def main():
    """
    """
    dataframe = pd.read_csv("main/assets/database/players.csv")
    
    st.markdown("<h1 style='text-align: center;'>NBA Ultimate Team</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("<h2 style='text-align: center;'>Busque um Jogador</h2>", unsafe_allow_html=True)
    option = st.selectbox(label="",
                          options=list(dataframe["FULL_NAME"]),
                          index=None,
                          placeholder="busque um jogador")
    st.markdown("---")

    if option == None:
        st.markdown("<h2 style='text-align: center;'>Melhores Jogadores</h2>", unsafe_allow_html=True)
        dataframe = dataframe.sort_values("OVERALLATTRIBUTE", ascending=False).reset_index(drop=True)
        rakingCreator(dataframe)
        st.markdown("---")

        st.markdown("<h2 style='text-align: center;'>Gerador de Rankings</h2>", unsafe_allow_html=True)
        option = st.selectbox(label="",
                          options=list(DICT_ATRIBUTOS.keys()),
                          index=None,
                          placeholder="busque um atributo")
        st.markdown("---")
        
        if option != None:
            st.markdown(f"<h2 style='text-align: center;'>{option}</h2>", unsafe_allow_html=True)
            dataframe = dataframe.sort_values(DICT_ATRIBUTOS[option], ascending=False).reset_index(drop=True)
            rakingCreator(dataframe)
            st.markdown("---")


    else:
        dataframe = dataframe[dataframe['FULL_NAME'] == str(option)].reset_index(drop=True)
        row_list = dataframe.loc[0, :].values.flatten().tolist()

        st.markdown(f"<h2 style='text-align: center;'>{option}</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.image(f"main/assets/images/full_cards/full_{row_list[1]}.png", width=300)
        with col2:
            st.markdown("", unsafe_allow_html=True)
            st.markdown("", unsafe_allow_html=True)
            st.markdown("", unsafe_allow_html=True)
            st.markdown(f"<h5>NBA ID: {row_list[1]}</h5>", unsafe_allow_html=True)
            st.markdown(f"<h5>EQUIPE: {row_list[-11]}</h5>", unsafe_allow_html=True)
            st.markdown(f"<h5>DATA DE NASC.: {row_list[-4]}/{row_list[-5]}/{row_list[-6]}</h5>", unsafe_allow_html=True)
            st.markdown(f"<h5>IDADE: {row_list[-7]}</h5>", unsafe_allow_html=True)
            st.markdown(f"<h5>POSITION: {row_list[-9]}</h5>", unsafe_allow_html=True)
            st.markdown(f"<h5>NACIONALIDADE: {row_list[-8]}</h5>", unsafe_allow_html=True)
            st.markdown(f"<h5>Nº DE CAMISA: {row_list[-10]}</h5>", unsafe_allow_html=True)
            st.markdown(f"<h5>EXPERIÊNCIA: {row_list[-3]} anos</h5>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()