import requests
import pandas as pd 

def save_images(csv_path:str, destine_path:str, extension:str) -> None:
    """
    This function will receive the path to a CSV file (containing data about NBA teams or players), 
    a path to a folder (where the images will be saved), and the extension in which the images will 
    be saved. Its goal is to collect the images corresponding to the links and download them.

    Parameters
    ----------
        csv_path
            type:str
            description: relative path to the CSV file
        
        destine_path
            type:str
            description: relative path to the destine folder

        extension
            type:str
            description: file extension for save

    Return
    ----------
        None

    Examples
    ----------
        save_images("path\\for_my.csv", "path\\for_my_folder", "csv")
    """

    dataframe = pd.read_csv(f".\{csv_path}")
    list_of_urls = list(dataframe["IMAGE_URL"])
    list_of_ids = list(dataframe["ID"])

    for each_id, each_url in zip(list_of_ids, list_of_urls):
        response = requests.get(each_url)

        if response.status_code == 200:
            with open(f"{destine_path}\{each_id}.{extension}", "wb") as file:
                file.write(response.content)
            print(f'{each_id} pronto.')

    return None

if __name__ == "__main__":
    save_images("dados\\teams_data.csv", ".\design\teams_images", "svg")
    save_images("dados\\active_players_data.csv", ".\design\players_images", "png")