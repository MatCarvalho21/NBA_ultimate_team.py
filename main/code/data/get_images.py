

import pandas as pd
import requests

def saveFlags(dataframe:pd.DataFrame, path_for_save:str="main/assets/images/flags") -> None:
    """
    Downloads and saves country flags based on 'COUNTRY_CODE' column in the dataframe.

    Args:
    dataframe (pd.DataFrame): The dataframe containing a 'COUNTRY_CODE' column.
    path_for_save (str, optional): The path where the flags will be saved. Defaults to "main/assets/images/flags".

    Returns:
    None
    """
    set_of_countries = set(dataframe["COUNTRY_CODE"])
    for each_country in set_of_countries:
            url = f"https://raw.githubusercontent.com/hampusborgos/country-flags/main/png1000px/{each_country.lower()}.png"
            response = requests.get(url)

            if response.status_code == 200:
                with open(f"{path_for_save}/{each_country}.png", "wb") as file:
                    file.write(response.content)
                print(f'{each_country} pronto.')

def savePlayers(dataframe:pd.DataFrame, path_for_save:str="main/assets/images/players") -> None:
    """
    Downloads and saves player images based on 'NBA_ID' column in the dataframe.

    Args:
    dataframe (pd.DataFrame): The dataframe containing an 'NBA_ID' column and an 'IMAGE_URL' column.
    path_for_save (str, optional): The path where the player images will be saved. Defaults to "main/assets/images/players".

    Returns:
    None
    """
    for each_id, each_player_link in zip(dataframe["NBA_ID"], dataframe["IMAGE_URL"]):
        response = requests.get(each_player_link)
        if response.status_code == 200:
            with open(f"{path_for_save}/{each_id}.png", "wb") as file:
                file.write(response.content)
            print(f'{each_id} pronto.')