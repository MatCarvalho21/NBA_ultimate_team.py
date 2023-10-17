from nba_api.stats.library.data import teams, players
import pandas as pd

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

if __name__ == "__main__":
    get_teams_data(".\dados\\teams_data.csv")
    get_players_data(".\dados\\players_data.csv")
    get_players_data(".\dados\\active_players_data.csv", True)