from bs4 import BeautifulSoup
import requests
import pandas as pd 

def ws_players_name() -> list:
    """
    """
    #link do site que contém os dados dos jogadores
    url = "https://www.2kratings.com/nikola-jokic"

    #processo para acessar a página
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")


ws_players_name()