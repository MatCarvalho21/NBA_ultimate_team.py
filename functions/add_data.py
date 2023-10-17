from bs4 import BeautifulSoup
import requests

list_of_columns = ["PPG", "RPG", "APG", "PIE", "HEIGHT", "WEIGHT", "COUNTRY", "LAST ATTENDED", "AGE", "BIRTHDATE", "DRAFT", "EXPERIENCE"]

def add_players_data(id_jogador:str):
    """
    """
    url = f"https://www.nba.com/stats/player/{id_jogador}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("div", class_="PlayerSummary_summaryBotInner__1r03I")

    #config string
    list_elements_01 = str(elements).split("\">")
    list_elements_02 = list()

    for each_elements in list_elements_01:
        list_of_each_elements = each_elements.split("</p>")

        if len(list_of_each_elements) == 2:
            list_elements_02.append(list_of_each_elements[0])

    final_list = list()
    for each_index in range(1, 25, 2):
        if list_elements_02[each_index] == "DRAFT":
            final_list.insert(3, "--")
        else:
            final_list.append(list_elements_02[each_index])

    return final_list

if __name__ == "__main__":
    print(add_players_data("1641705"))
    print(add_players_data("203648"))
    print(add_players_data("1628386"))
    