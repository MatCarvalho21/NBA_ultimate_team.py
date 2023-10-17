from nba_api.stats.static import players
import pandas as pd

def get_nba_data(csv_name:str) -> str:
    """
    This function takes a name for a CSV file (it can be a path if you want to save it in another folder)
    and saves the CSV file with the data of all NBA players who are currently playing.

    Parameters
    ----------
        csv_name
            type: str
            description: The name of the CSV file that will be saved.

    Returns
    ----------
        message
            type: str
            description: A simple message for success.

    Examples
    ----------
        get_nba_data("my_file_name")

        get_nba_data("..\my_folde_name\my_file_name")
    """

    list_of_dict_nba_players = players.get_active_players()
    list_of_columns = ["ID", "FULL_NAME", "FIRST_NAME", "LAST_NAME", "ACTIVE", "IMAGE_LINK"]
    list_of_data_complete = list()

    for indice in range(0, len(list_of_dict_nba_players)):
        dict_of_each_player = list_of_dict_nba_players[indice]
        list_of_data = list(dict_of_each_player.values())
        list_of_data.append(f"https://cdn.nba.com/headshots/nba/latest/1040x760/{list_of_data[0]}.png")
        list_of_data_complete.append(list_of_data)

    dataframe = pd.DataFrame(data=list_of_data_complete, columns=list_of_columns).sort_values(by="FULL_NAME").reset_index(drop=True)
    dataframe.to_csv(f"{csv_name}.csv")

    message = "OK"

    return message