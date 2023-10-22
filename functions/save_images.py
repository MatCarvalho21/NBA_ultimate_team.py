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

if __name__ == "__main__":
    #OK 2023_10_21
    save_images(".\dados\\final_dataframe.csv", ".\design\players_images", "png", False)