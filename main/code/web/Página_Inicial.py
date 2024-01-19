import streamlit as st
import pandas as pd  
from functions import rakingCreator, colorAttribute, DICT_ATRIBUTOS

def main():
    """
    """
    dataframe = pd.read_csv("main/assets/database/players.csv")
    
    st.markdown("<h1 style='text-align: center;'>NBA Ultimate Team</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("<h2 style='text-align: center;'>Player Selector</h2>", unsafe_allow_html=True)
    option = st.selectbox(label="",
                          options=list(dataframe["FULL_NAME"]),
                          index=None,
                          placeholder="search for a player")
    st.markdown("---")

    if option == None:
        st.markdown("<h2 style='text-align: center;'>Best Players</h2>", unsafe_allow_html=True)
        dataframe = dataframe.sort_values("OVERALLATTRIBUTE", ascending=False).reset_index(drop=True)
        rakingCreator(dataframe)
        st.markdown("---")

        st.markdown("<h2 style='text-align: center;'>Ranking Generator</h2>", unsafe_allow_html=True)
        option = st.selectbox(label="",
                          options=list(DICT_ATRIBUTOS.keys()),
                          index=None,
                          placeholder="search for an attribute")
        st.markdown("---")
        
        if option != None:
            st.markdown(f"<h2 style='text-align: center;'>{option}</h2>", unsafe_allow_html=True)
            dataframe = dataframe.sort_values(DICT_ATRIBUTOS[option], ascending=False).reset_index(drop=True)
            rakingCreator(dataframe, DICT_ATRIBUTOS[option])
            st.markdown("---")


    else:
        dataframe = dataframe[dataframe['FULL_NAME'] == str(option)].reset_index(drop=True)
        row_list = dataframe.loc[0, :].values.flatten().tolist()

        st.markdown(f"<h2 style='text-align: center;'>{option}</h2>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            tab__1, tab__2 = st.tabs(["Mini Card", "Full Card"])
            tab__1.markdown("", unsafe_allow_html=True)
            tab__1.image(f"main/assets/images/mini_cards/{row_list[1]}.png", width=300)
            tab__2.image(f"main/assets/images/full_cards/full_{row_list[1]}.png", width=300)

        with col2:
            st.markdown("", unsafe_allow_html=True)
            st.markdown("", unsafe_allow_html=True)
            st.markdown("", unsafe_allow_html=True)
            st.markdown("", unsafe_allow_html=True)
            st.markdown("", unsafe_allow_html=True)
            st.markdown("", unsafe_allow_html=True)

            with st.container(border=True):
                st.markdown(f"<h5>NBA ID: {row_list[1]}</h5>", unsafe_allow_html=True)
                st.markdown(f"<h5>TEAM: {row_list[-11]}</h5>", unsafe_allow_html=True)
                st.markdown(f"<h5>DATE OF BIRTH: {row_list[-5].title()} {row_list[-4]}, {row_list[-6]}</h5>", unsafe_allow_html=True)
                st.markdown(f"<h5>AGE: {row_list[-7]}</h5>", unsafe_allow_html=True)
                st.markdown(f"<h5>POSITION: {row_list[-9]}</h5>", unsafe_allow_html=True)
                st.markdown(f"<h5>NACIONALITY: {row_list[-8]}</h5>", unsafe_allow_html=True)
                st.markdown(f"<h5>JERSEY NUM.: {row_list[-10]}</h5>", unsafe_allow_html=True)
                if row_list != "Rookie":
                    st.markdown(f"<h5>EXPERIENCE: {row_list[-3]}</h5>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<h5>EXPERIENCE: {row_list[-3]} year(s)</h5>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["Attributes", "Chart"])

        coluna_1, coluna_2, coluna_3 = tab1.columns(3)

        with coluna_1:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: center;'>Outside Scoring</h5>", unsafe_allow_html=True)
                coluna_1_1, coluna_1_2 = st.columns([1, 4])
                with coluna_1_1:
                    colorAttribute(row_list[8])
                    colorAttribute(row_list[9])
                    colorAttribute(row_list[10])
                    colorAttribute(row_list[11])
                    colorAttribute(row_list[12])
                    colorAttribute(row_list[13])
                with coluna_1_2:
                    st.markdown(f"<p>Close Shot</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Mid-Range Shot</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Three-Point Shot</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Free Throw</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Shot IQ</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Off. Consistency</p>", unsafe_allow_html=True)

            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: center;'>Inside Scoring</h5>", unsafe_allow_html=True)
                coluna_1_3, coluna_1_4 = st.columns([1, 4])
                with coluna_1_3:
                    colorAttribute(row_list[14])
                    colorAttribute(row_list[15])
                    colorAttribute(row_list[16])
                    colorAttribute(row_list[17])
                    colorAttribute(row_list[18])
                    colorAttribute(row_list[19])
                    colorAttribute(row_list[20])
                    colorAttribute(row_list[21])
                with coluna_1_4:
                    st.markdown(f"<p>Layup</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Standing Dunk</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Driving Dunk</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Post Hook</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Post Fade</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Post Control</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Draw Foul</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Hands</p>", unsafe_allow_html=True)

        with coluna_2:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: center;'>Defending</h5>", unsafe_allow_html=True)
                coluna_2_1, coluna_2_2 = st.columns([1, 4])
                with coluna_2_1:
                    colorAttribute(row_list[22])
                    colorAttribute(row_list[23])
                    colorAttribute(row_list[24])
                    colorAttribute(row_list[25])
                    colorAttribute(row_list[26])
                    colorAttribute(row_list[27])
                    colorAttribute(row_list[28])
                    colorAttribute(row_list[29])
                with coluna_2_2:
                    st.markdown(f"<p>Interior Defense</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Perimeter Defense</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Steal</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Block</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Lateral Quickness</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Help Defense IQ</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Pass Perception</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Def. Consistency</p>", unsafe_allow_html=True)

            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: center;'>Rebounding</h5>", unsafe_allow_html=True)
                coluna_2_3, coluna_2_4 = st.columns([1, 4])
                with coluna_2_3:
                    colorAttribute(row_list[42])
                    colorAttribute(row_list[43])
                with coluna_2_4:
                    st.markdown(f"<p>Off. Rebound</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Def. Rebound</p>", unsafe_allow_html=True)

        with coluna_3:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: center;'>Playmaking</h5>", unsafe_allow_html=True)
                coluna_3_1, coluna_3_2 = st.columns([1, 4])
                with coluna_3_1:
                    colorAttribute(row_list[37])
                    colorAttribute(row_list[38])
                    colorAttribute(row_list[39])
                    colorAttribute(row_list[40])
                    colorAttribute(row_list[41])
                with coluna_3_2:
                    st.markdown(f"<p>Pass Accuracy</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Ball Handle</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Speed with Ball</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Pass IQ</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Pass Vision</p>", unsafe_allow_html=True)

            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: center;'>Athleticism</h5>", unsafe_allow_html=True)
                coluna_3_3, coluna_3_4 = st.columns([1, 4])
                with coluna_3_3:
                    colorAttribute(row_list[30])
                    colorAttribute(row_list[31])
                    colorAttribute(row_list[32])
                    colorAttribute(row_list[33])
                    colorAttribute(row_list[34])
                    colorAttribute(row_list[35])
                    colorAttribute(row_list[36])
                with coluna_3_4:
                    st.markdown(f"<p>Speed</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Acceleration</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Strength</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Vertical</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Stamina</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Hustle</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Overall Durability</p>", unsafe_allow_html=True)


        tab1.markdown("---")


if __name__ == "__main__":
    main()