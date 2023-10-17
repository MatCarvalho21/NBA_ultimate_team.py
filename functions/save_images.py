import requests
import pandas as pd 

def save_images(dataframe_path:str, folder_path:str, extension:str) -> None:
    """
    """
    dataframe = pd.read_csv(f".\{dataframe_path}")

    urls = list(dataframe["IMAGE_URL"])
    ids = list(dataframe["ID"])
    print(urls)

    for each_id, each_url in zip(ids, urls):

        response = requests.get(each_url)

        if response.status_code == 200:
            with open(f"{folder_path}\{each_id}.{extension}", "wb") as file:
                file.write(response.content)
            print(f'{each_id} pronto.')
        
        else:
            print('Falha ao baixar a imagem. Código de status:')
    
    return None

if __name__ == "__main__":
    save_images("dados\\teams_data.csv", ".\design\\teams_images", "svg")
    save_images("dados\\players_data.csv", ".\design\\players_images", "png")