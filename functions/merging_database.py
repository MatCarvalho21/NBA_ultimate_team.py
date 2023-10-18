import pandas as pd 

dataframe_ratings = pd.read_csv(".\dados\players_ratings.csv")
dataframe_players = pd.read_csv(".\dados\players_data.csv")

columns_01 = list(dataframe_ratings.columns)
dataframe_ratings = dataframe_ratings.set_index("NAME", drop=True)
columns_02 = list(dataframe_players.columns)
del columns_02[3]
dataframe_players = dataframe_players.set_index("FULL_NAME", drop=True)

list_of_players = list(dataframe_ratings.index)

list_of_data = list()
list_of_none_players = list()

for each_player in list_of_players:
    try:
        list_01 = list(dataframe_players.loc[each_player])
        list_02 = list(dataframe_ratings.loc[each_player])
        list_of_data.append(list_01 + list_02)
    except KeyError:
        list_of_none_players.append(list_02)

#TODO existem alguns jogadores que estão ficando de fora
list_of_columns = columns_02 + columns_01[1:]

final_dataframe = pd.DataFrame(columns=list_of_columns, data=list_of_data)
final_dataframe.rename(columns={"FIRST_NAME":"LAST_NAME", "LAST_NAME":"FIRST_NAME"}, inplace=True)

final_dataframe.to_csv(f".\dados\complete_players_database.csv", index=False)