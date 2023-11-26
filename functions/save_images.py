import requests
import pandas as pd 

def save_images(csv_path:str, path_for_save_images:str, extension:str, to_save:bool=True) -> None:
    """
    Essa função recebe um dataframe, ou de jogadores ou de times, desde que contenha a coluna 
    ID e a coluna IMAGE_URL e baixa as imagens de acordo com esses dados. 
    """

    dataframe = pd.read_csv(f".\{csv_path}")
    list_of_urls = list(dataframe["IMAGE_URL"])
    list_of_ids = list(dataframe["ID"])

    if to_save == True:
        for each_id, each_url in zip(list_of_ids, list_of_urls):
            response = requests.get(each_url)

            if response.status_code == 200:
                with open(f"{path_for_save_images}\{each_id}.{extension}", "wb") as file:
                    file.write(response.content)
                print(f'{each_id} pronto.')

    return None

def save_flags(csv_path:str, path_for_save_images:str, extension:str, to_save:bool=True) -> None:
    """
    Recebe um dataframe que tem uma coluna com as siglas no formato iso 3166 dos países e
    salva em uma pasta desejada as bandeiras dos países contidos no dataframe.
    """

    dataframe = pd.read_csv(f".\{csv_path}")
    set_of_countries = set(dataframe["CORRECT_COUNTRY"])

    if to_save == True:
        for each_country in set_of_countries:
            url = f"https://raw.githubusercontent.com/hampusborgos/country-flags/main/png1000px/{each_country.lower()}.png"
            response = requests.get(url)

            if response.status_code == 200:
                with open(f"{path_for_save_images}\{each_country}.{extension}", "wb") as file:
                    file.write(response.content)
                print(f'{each_country} pronto.')

    return None

if __name__ == "__main__":
    #OK 2023_10_21
    save_images(".\\dados\\final_dataframe.csv", ".\\design\\players_images", "png", False)

    #OK 2023_10_21
    save_flags(".\\dados\\final_dataframe.csv", ".\\design\\flags_images", "png", to_save=False)

"""
response = requests.get('https://cdn.nba.com/headshots/nba/latest/1040x760/203468.png')

if response.status_code == 200:
    with open(f"{'./design/players_images'}/{203468}.{'png'}", "wb") as file:
        file.write(response.content)
    print(f'{203468} pronto.')
"""