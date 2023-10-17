import requests
import pandas as pd 

def save_images(folder_path:str) -> str:
    """
    This function will receive the name of a folder and save the images of all
    active NBA players in it in PNG format.

    Parameters
    ----------
        folder_path
            type: str
            description: The name of the folder for save the images.

    Returns
    ----------
        message
            type: str
            description: A simple message for success.

    Examples
    ----------
        save_images("my_file_name")

        save_images("..\my_folde_name\my_file_name")
    """
    nba_dataframe = pd.read_csv("dados\\nba_dataset.csv")
    urls = list(nba_dataframe["IMAGE_LINK"])
    ids = list(nba_dataframe["ID"])

    response = requests.get(each_url)

    for each_id, each_url in zip(ids, urls):
        if response.status_code == 200:
            with open(f"{folder_path}\{each_id}.png", "wb") as file:
                file.write(response.content)
            print(f'{each_id} pronto.')
        else:
            print('Falha ao baixar a imagem. Código de status:')
    
    message = "OK"

    return message
