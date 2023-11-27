

import pandas as pd  

dataframe = pd.read_csv("C:/Users/mathe/NBA_ultimate_team/dados/final_dataframe.csv")
dataframe["COMPLETE_NAME"] = dataframe["FIRST_NAME"] + " " + dataframe["LAST_NAME"]

lista_de_nomes = list(dataframe["COMPLETE_NAME"])

with open('C:\\Users\\mathe\\NBA_ultimate_team\\assets\\python_for_web\\creating_list.txt', "w") as file:
    for indice in range(0, len(lista_de_nomes)):
        if indice == 0:
            file.write(f"const jogadores = ['{lista_de_nomes[indice]}',\n")
        elif indice == len(lista_de_nomes) - 1:
            file.write(f"\t'{lista_de_nomes[indice]}']")
        else:
            file.write(f"\t'{lista_de_nomes[indice]}',\n")