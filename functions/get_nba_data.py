from nba_api.stats.library.data import teams, players
import pandas as pd
from var_nba_2k_ratings import RATING_LIST
from bs4 import BeautifulSoup
import requests

def get_teams_data(csv_path:str) -> None:
    """
    This function aims to save data from the NBA_API library related to NBA teams 
    into a CSV file.

    Parameters
    ----------
        csv_path
            type:str
            description: the path for save the CSV with the name of the file

    Return
    ----------
        None

    Examples
    ----------
        get_teams_data("randon\path\my_file.csv")
    """
    columns_name_teams = ["ID", "ACRONYM", "NICKNAME", "FOUNDATION_YEAR", "CITY", "NAME", "STATE", "TITLES", "IMAGE_URL"]

    for list_of_each_team in teams:
        list_of_each_team.append(f"https://cdn.nba.com/logos/nba/{list_of_each_team[0]}/global/D/logo.svg")

    dataframe = pd.DataFrame(data=teams, columns=columns_name_teams)

    dataframe.to_csv(f"{csv_path}", index=False)

    return None

def get_players_data(csv_path:str, active_player:bool=False) -> None:
    """
    This function aims to save data from the NBA_API library related to NBA players, 
    both retired and current, into a CSV file.

    Parameters
    ----------
        csv_path
            type:str
            description: the path for save the CSV with the name of the file

    Return
    ----------
        None

    Examples
    ----------
        get_players_data("randon\path\my_file.csv", True)
    """
    columns_name_players = ["ID", "FIRST_NAME", "LAST_NAME", "FULL_NAME", "ACTIVE", "IMAGE_URL"]

    for list_of_each_player in players:
        list_of_each_player.append(f"https://cdn.nba.com/headshots/nba/latest/1040x760/{list_of_each_player[0]}.png")

    dataframe = pd.DataFrame(data=players, columns=columns_name_players)
    
    if active_player == True:
        dataframe = dataframe[dataframe["ACTIVE"] == True].reset_index(drop=True)

    dataframe.to_csv(f"{csv_path}", index=False)

    return None

def get_nba_players_ratings(csv_path:str) -> None:
    """
    This function aims to save data from the NBA2K into a CSV file.

    Parameters
    ----------
        csv_path
            type:str
            description: the path for save the CSV with the name of the file

    Return
    ----------
        None

    Examples
    ----------
        get_nba_players_ratings("randon\path\my_file.csv")
    """
    list_of_data = list()

    list_of_columns = list(dict(RATING_LIST[0]).keys())
    list_of_columns = [each_column.upper() for each_column in list_of_columns]

    for each_dict in RATING_LIST:
        list_of_data.append(list(dict(each_dict).values()))

    dataframe = pd.DataFrame(data=list_of_data, columns=list_of_columns)
    dataframe.to_csv(f"{csv_path}", index=False)
    
    return None

def get_additional_data(complete_dataframe:pd.DataFrame) -> None:
    """
    """
    list_of_colums = ["ID", "JERSEY_NUMBER", "POSITIONS", "COUNTRY", "AGE", "YEAR_BD", "MONTH_BD", "DAY_BD", "EXPERIENCE"]
    list_of_data = list()
    for each_player_id in complete_dataframe["ID"]:

        #SET_ID
        list_of_each_player = list()
        list_of_each_player.append(each_player_id)

        player_url = f"https://www.nba.com/player/{each_player_id}"

        response = requests.get(player_url)
        soup = BeautifulSoup(response.text, "html.parser")
        p_tags = soup.find_all('p')

        for index in range(0, len(p_tags)):
            p_tags[index] = p_tags[index].text

        #GET_JERSEYNUMBER_POSITION
        sub_list_01 = p_tags[0].split("|")
        jersey_number = sub_list_01[1][1:]
        position = sub_list_01[2].upper()
        list_of_each_player.append(jersey_number)
        list_of_each_player.append(position)

        #GET_COUNTRY
        index_country = p_tags.index("COUNTRY") + 1
        list_of_each_player.append(p_tags[index_country])

        #GET_AGE
        index_age = p_tags.index("AGE") + 1
        list_of_each_player.append(p_tags[index_age][:2])
        
        #GET_BIRTHDATE
        index_bd = p_tags.index("BIRTHDATE") + 1
        sub_list_01 = p_tags[index_bd].split(", ")
        list_of_each_player.append(sub_list_01[1])
        sub_list_02 = sub_list_01[0].split(" ")
        list_of_each_player.append(sub_list_02[0].upper())
        list_of_each_player.append(sub_list_02[1])

        #GET_EXPERIENCE
        index_ex = p_tags.index("EXPERIENCE") + 1
        sub_list_01 = p_tags[index_ex].split(" ")
        list_of_each_player.append(sub_list_01[0])

        print(list_of_each_player)



        


def get_teams_dict():
    """
    """
    dataframe = pd.read_csv(".\dados\\teams_data.csv")

    dict_teams = dict()
    list_of_ids = list(dataframe["ID"])
    list_of_names = list(dataframe["NAME"])

    for each_id, each_name in zip(list_of_ids, list_of_names):
        dict_teams[each_name] = each_id

    return dict_teams



if __name__ == "__main__":
    """
    get_teams_data(".\dados\\teams_data.csv")
    get_players_data(".\dados\\players_data.csv")
    get_players_data(".\dados\\active_players_data.csv", True)
    get_nba_players_ratings(".\dados\\players_ratings.csv")
    print(get_teams_dict)
    """
    dataframe = pd.read_csv(".\dados\complete_players_database.csv")
    get_additional_data(dataframe)