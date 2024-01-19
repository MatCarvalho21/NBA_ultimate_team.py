import streamlit as st
import pandas as pd  
from functions import columnOfData

st.set_page_config(initial_sidebar_state="collapsed")

dataframe = pd.read_csv("main/assets/database/players.csv")

st.markdown("<h1 style='text-align: center;'>🏀 NBA Ultimate Team</h1>", unsafe_allow_html=True)
st.markdown("---")
col4, col1, col2, col3 = st.columns([3, 2, 2, 2])
with col1:
    st.markdown("<h3 style='text-align: center;'>Player 1</h3>", unsafe_allow_html=True)
    option_1 = st.selectbox(label="",
                          options=list(dataframe["FULL_NAME"]),
                          index=None,
                          placeholder=" src. player")
    if option_1 != None:
        dataframe_1 = dataframe[dataframe['FULL_NAME'] == str(option_1)].reset_index(drop=True)
        row_list_1 = dataframe_1.loc[0, :].values.flatten().tolist()

        st.image(f"main/assets/images/full_cards/full_{row_list_1[1]}.png")
    else:
        row_list_1 = [0]*50

with col2:
    st.markdown("<h3 style='text-align: center;'>Player 2</h3>", unsafe_allow_html=True)
    option_2 = st.selectbox(label=" ",
                        options=list(dataframe["FULL_NAME"]),
                        index=None,
                        placeholder=" src. player")
    
    if option_2 != None:
        dataframe_2 = dataframe[dataframe['FULL_NAME'] == str(option_2)].reset_index(drop=True)
        row_list_2 = dataframe_2.loc[0, :].values.flatten().tolist()

        st.image(f"main/assets/images/full_cards/full_{row_list_2[1]}.png")
    else:
        row_list_2 = [0]*50

with col3:
    st.markdown("<h3 style='text-align: center;'>Player 3</h3>", unsafe_allow_html=True)
    option_3 = st.selectbox(label="  ",
                        options=list(dataframe["FULL_NAME"]),
                        index=None,
                        placeholder=" src. player")
    
    if option_3 != None:
        dataframe_3 = dataframe[dataframe['FULL_NAME'] == str(option_3)].reset_index(drop=True)
        row_list_3 = dataframe_3.loc[0, :].values.flatten().tolist()

        st.image(f"main/assets/images/full_cards/full_{row_list_3[1]}.png")
    else:
        row_list_3 = [0]*50

col4, col1, col2, col3 = st.columns([3, 2, 2, 2])
columnOfData(row_list_1, col1, 
             row_list_2, col2, 
             row_list_3, col3, 
             col4, 8, 44)

st.markdown("---")