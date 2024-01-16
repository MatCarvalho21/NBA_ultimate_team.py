

from nba_api.stats.library.data import teams, players
from const import RATING_LIST
import pandas as pd
from bs4 import BeautifulSoup
import requests
from set_data import mergeData

def getTeamsData() -> pd.DataFrame:
    """
    Fetches NBA teams data and returns it as a Pandas DataFrame.

    Returns:
    pd.DataFrame: DataFrame containing information about NBA teams, including NBA_ID, SIGN, NICKNAME, FOUNDATION, CITY, FULL_NAME, STATE, TITLES, and IMAGE_URL.
    """

    list_columns_teams = ["NBA_ID", "SIGN", "NICKNAME", "FOUNDATION", 
                      "CITY", "FULL_NAME", "STATE", "TITLES", "IMAGE_URL"]

    for list_of_each_team in teams:
        list_of_each_team.append(f"https://cdn.nba.com/logos/nba/{list_of_each_team[0]}/global/D/logo.svg")

    dataframe = pd.DataFrame(data=teams, columns=list_columns_teams)

    return dataframe

def getPlayersData(is_active:bool=False) -> pd.DataFrame:
    """
    Fetches NBA players data and returns it as a Pandas DataFrame.

    Args:
    is_active (bool, optional): If True, returns only active players. Defaults to False.

    Returns:
    pd.DataFrame: DataFrame containing information about NBA players, including NBA_ID, LAST_NAME, FIRST_NAME, FULL_NAME, IS_ACTIVE, and IMAGE_URL.
    """

    list_columns_players = ["NBA_ID", "LAST_NAME", "FIRST_NAME", "FULL_NAME", 
                        "IS_ACTIVE", "IMAGE_URL"]

    for list_of_each_player in players:
        list_of_each_player.append(f"https://cdn.nba.com/headshots/nba/latest/1040x760/{list_of_each_player[0]}.png")

    dataframe = pd.DataFrame(data=players, columns=list_columns_players)

    if is_active == False:
        return dataframe
    else:
        return dataframe[dataframe["IS_ACTIVE"] == True].reset_index(drop=True)
    
def saveData(dataframe:pd.DataFrame, folder_path:str, file_name:str) -> None:
    """
    Saves a Pandas DataFrame to a CSV file.

    Args:
    dataframe (pd.DataFrame): DataFrame to be saved.
    folder_path (str): Path to the folder where the file will be saved.
    file_name (str): Name of the CSV file (including the ".csv" extension).
    
    Returns:
    None
    """
    dataframe.to_csv(f"{folder_path}/{file_name}", index=False)

def get2KData():
    """
    Fetches NBA 2K player ratings data and returns it as a Pandas DataFrame.

    Returns:
    pd.DataFrame: DataFrame containing NBA 2K player ratings data with columns such as points, assists, rebounds, etc., based on the RATING_LIST structure.
    """

    list_of_2K_columns = list()
    for each_key in RATING_LIST[0].keys():
        list_of_2K_columns.append(each_key.upper())

    number_of_players = len(RATING_LIST) 
    list_of_2K_data = list()
    for index in range(0, number_of_players):
        list_of_2K_data.append(list((RATING_LIST[index].values())))

    dataframe = pd.DataFrame(data=list_of_2K_data, columns=list_of_2K_columns)
    
    return dataframe

def getWebData(path_for_dataframe:str="main/assets/database/merged_data.csv") -> pd.DataFrame:
    """
    """
    dataframe = pd.read_csv(path_for_dataframe)

    test_index = 0
    list_of_columns = ["ID", "TEAM", "JERSEY_NUM", "POSITION", "COUNTRY", "AGE", "BD_YEAR", "BD_MONTH", "BD_DAY", "EXPERIENCE"]
    list_of_data = list()
    list_of_invisibels_players = list()
    for each_id in dataframe["NBA_ID"]:
        each_list_of_data = list()

        response = requests.get(f"https://www.nba.com/player/{each_id}")
        soup = BeautifulSoup(response.text, "html.parser")
        p_tags = soup.find_all('p')
        for index in range(len(p_tags)):
            p_tags[index] = p_tags[index].text

        # TEAM - NUMBER - POSITION
        each_list_of_data.append(each_id)
        try:
            sub_list_01 = p_tags[0].split(" | ")
            each_list_of_data.append(sub_list_01[0])
            each_list_of_data.append(sub_list_01[1])
            each_list_of_data.append(sub_list_01[2])
        except:
            try: 
                each_list_of_data[1] = "Unknow"
            except:
                each_list_of_data.append("Unknow")
            each_list_of_data.append("Unknow")
            each_list_of_data.append("Unknow")
            list_of_invisibels_players.append(each_id)

        # COUNTRY
        try:
            index_country = p_tags.index("COUNTRY") + 1
            each_list_of_data.append(p_tags[index_country])
        except:
            each_list_of_data.append("Unknow")

        # AGE
        try:
            index_age = p_tags.index("AGE") + 1
            each_list_of_data.append(p_tags[index_age][:2] + "y")
        except:
            each_list_of_data.append("Unknow")

        # BIRTHDATE
        try:
            index_bd = p_tags.index("BIRTHDATE") + 1
            sub_list_01 = p_tags[index_bd].split(", ")
            each_list_of_data.append(sub_list_01[1])
            sub_list_02 = sub_list_01[0].split(" ")
            each_list_of_data.append(sub_list_02[0].upper())
            each_list_of_data.append(sub_list_02[1])
        except:
            each_list_of_data.append("Unknow")
            each_list_of_data.append("Unknow")
            each_list_of_data.append("Unknow")

        # EXPERIENCE
        try:
            index_ex = p_tags.index("EXPERIENCE") + 1
            sub_list_01 = p_tags[index_ex].split(" ")
            each_list_of_data.append(sub_list_01[0])
        except:
            each_list_of_data.append("Unknow")

        list_of_data.append(each_list_of_data)
        print(test_index)
        test_index += 1
    
    dataframe = pd.DataFrame(data=list_of_data, columns=list_of_columns)
    return dataframe