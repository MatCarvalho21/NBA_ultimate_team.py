from nba_api.stats.library.data import teams, players
import pandas as pd

def get_teams_data(csv_name:str) -> None:
    """
    """
    columns_name = ["ID", "ACRONYM", "NICKNAME", "FOUNDATION_YEAR", "CITY", "NAME", "STATE", "TITLES", "IMAGE_URL"]

    for list_of_each_team in teams:
        list_of_each_team.append(f"https://cdn.nba.com/logos/nba/{list_of_each_team[0]}/global/D/logo.svg")

    dataframe = pd.DataFrame(data=teams, columns=columns_name)

    dataframe.to_csv(f"{csv_name}.csv")

    return None

def get_players_data(csv_name:str) -> None:
    """
    """
    columns_name = ["ID", "FIRST_NAME", "LAST_NAME", "FULL_NAME", "ACTIVE", "IMAGE_URL"]

    for list_of_each_player in players:
        list_of_each_player.append(f"https://cdn.nba.com/headshots/nba/latest/1040x760/{list_of_each_player[0]}.png")

    dataframe = pd.DataFrame(data=players, columns=columns_name)

    dataframe.to_csv(f"{csv_name}.csv")

    return None

if __name__ == "__main__":
    get_teams_data(".\dados\\teams_data")
    get_players_data(".\dados\\players_data")