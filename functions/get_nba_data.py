from nba_api.stats.library.data import teams, players
import pandas as pd
from var_nba_2k_ratings import RATING_LIST
from bs4 import BeautifulSoup
import requests

def get_teams_data(to_save:bool=False, path_for_save:str="", csv_name:str="") -> pd.DataFrame:
    """
    Essa função vai pegar os dados da biblioteca NBA API refente aos times da NBA e gerar um datafame
    com eles. Além disso, vai criar uma coluna com o link do logo de cada equipe que será baixado 
    por outra função. 
    """
    columns_name_teams = ["ID", "ACRONYM", "NICKNAME", "FOUNDATION_YEAR", "CITY", "NAME", "STATE", "TITLES", "IMAGE_URL"]

    for list_of_each_team in teams:
        list_of_each_team.append(f"https://cdn.nba.com/logos/nba/{list_of_each_team[0]}/global/D/logo.svg")

    dataframe = pd.DataFrame(data=teams, columns=columns_name_teams)
    if to_save == True:
        dataframe.to_csv(f"{path_for_save}\{csv_name}", index=False)

    return dataframe

def get_players_data(to_save:bool=False, path_for_save:str="", csv_name:str="", active_player:bool=False) -> pd.DataFrame:
    """
    Essa função vai gerar um dataframe com os dados que foram extraidos da biblioteca 
    NBA API, além de criar o link para a imagem de cada jogador que vai ser usado por
    outra função para salvar.
    """
    columns_name_players = ["ID", "FIRST_NAME", "LAST_NAME", "FULL_NAME", "ACTIVE", "IMAGE_URL"]

    for list_of_each_player in players:
        list_of_each_player.append(f"https://cdn.nba.com/headshots/nba/latest/1040x760/{list_of_each_player[0]}.png")

    dataframe = pd.DataFrame(data=players, columns=columns_name_players)
    
    if active_player == True:
        dataframe = dataframe[dataframe["ACTIVE"] == True].reset_index(drop=True)

    if to_save == True:
        dataframe.to_csv(f"{path_for_save}\{csv_name}", index=False)

    return dataframe

def get_nba_players_ratings(to_save:bool=False, path_for_save:str="", csv_name:str="") -> pd.DataFrame:
    """
    Essa função vai gerar um dataframe com os dados dos jogadores referentes ao NBA2K. Os dados 
    estão em uma lista de dicionários presentes em outro arquivo, ela apenas gera um dataframe com esses dados.
    """
    list_of_data = list()

    list_of_columns = list(dict(RATING_LIST[0]).keys())
    list_of_columns = [each_column.upper() for each_column in list_of_columns]

    for each_dict in RATING_LIST:
        list_of_data.append(list(dict(each_dict).values()))

    dataframe = pd.DataFrame(data=list_of_data, columns=list_of_columns).reset_index(drop=True)
    
    if to_save == True:
        dataframe.to_csv(f"{path_for_save}\{csv_name}", index=False)
    
    return dataframe

def web_scraping_nba(path_for_id_dataframe:str, to_save:bool=False, path_for_save:str="", final_csv_name:str="") -> pd.DataFrame:
    """
    Essa função recebe um dataframe que deve conter os ID dos jogadores e faz um websacraping da página de cada um
    no site da NBA. Além disso, ela retorna um dataframe com os dados que foram coletados. Também é possível passar
    parâmetros opicionais para salvar um csv com os dados obtidos. 
    """
    complete_dataframe = pd.read_csv(f"{path_for_id_dataframe}")

    list_of_colums = ["ID", "TEAM", "JERSEY_NUM", "POSITION", "COUNTRY", "AGE", "BD_YEAR", "BD_MONTH", "BD_DAY", "EXPERIENCE"]
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

        #GET_JERSEY_NUMBER_POSITION
        try:     
            sub_list_01 = p_tags[0].split(" | ")
            player_team = sub_list_01[0]
            player_jersey_number = sub_list_01[1][1:]
            player_position = sub_list_01[2]
            list_of_each_player.append(player_team)
            list_of_each_player.append(player_jersey_number)
            list_of_each_player.append(player_position)
        except:
            list_of_each_player.append(None)
            list_of_each_player.append(None)
            list_of_each_player.append(None)

        #GET_COUNTRY
        try:
            index_country = p_tags.index("COUNTRY") + 1
            list_of_each_player.append(p_tags[index_country])
        except:
            list_of_each_player.append(None)

        
        #GET_AGE
        try:
            index_age = p_tags.index("AGE") + 1
            list_of_each_player.append(p_tags[index_age][:2])
        except:
            list_of_each_player.append(None)

        #GET_BIRTHDATE
        try:
            index_bd = p_tags.index("BIRTHDATE") + 1
            sub_list_01 = p_tags[index_bd].split(", ")
            list_of_each_player.append(sub_list_01[1])
            sub_list_02 = sub_list_01[0].split(" ")
            list_of_each_player.append(sub_list_02[0].upper())
            list_of_each_player.append(sub_list_02[1])
        except:
            list_of_each_player.append(None)
            list_of_each_player.append(None)
            list_of_each_player.append(None)

        #GET_EXPERIENCE
        try:
            index_ex = p_tags.index("EXPERIENCE") + 1
            sub_list_01 = p_tags[index_ex].split(" ")
            list_of_each_player.append(sub_list_01[0])
        except:
            list_of_each_player.append(None)

        print(f"{each_player_id} ready!")

        list_of_data.append(list_of_each_player)

    dataframe = pd.DataFrame(columns=list_of_colums, data=list_of_data).reset_index(drop=True)

    if to_save == True:
        dataframe.to_csv(f"{path_for_save}\{final_csv_name}", index=False)

    return dataframe

def get_teams_dict() -> dict:
    """
    Essa função tem como objetivo gerar um dicionário com o nome dos times e os 
    seus respectivos ID's. Basicamente vai ajudar na conversão e na manipulação dos 
    dados.
    """
    dataframe = pd.read_csv(".\dados\\teams_data.csv")

    dict_teams = dict()
    list_of_ids = list(dataframe["ID"])
    list_of_names = list(dataframe["NAME"])

    for each_id, each_name in zip(list_of_ids, list_of_names):
        dict_teams[each_name] = each_id

    return dict(dict_teams)



if __name__ == "__main__":
    #OK 2023_10_21
    get_teams_data()

    #OK 2023_10_21
    get_players_data()

    #OK 2023_10_21
    get_nba_players_ratings()

    #OK 2023_10_21
    get_teams_dict()

    #OK 2023_10_21
    web_scraping_nba(".\dados\complete_players_database.csv", False, "", "").head()