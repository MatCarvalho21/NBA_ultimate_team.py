import pandas as pd 
import math

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
final_dataframe.sort_values(inplace=True, by=["OVERALLATTRIBUTE"], ascending=False)

final_dataframe['OSC'] = round((final_dataframe["CLOSESHOT"] + final_dataframe["THREEPOINTSHOT"] + final_dataframe["MIDRANGESHOT"] + final_dataframe["FREETHROW"] + final_dataframe["SHOTIQ"] + final_dataframe["OFFENSIVECONSISTENCY"])/6, 0)
final_dataframe['ISC'] = round((final_dataframe["LAYUP"] + final_dataframe["STANDINGDUNK"] + final_dataframe["DRIVINGDUNK"] + final_dataframe["POSTHOOK"] + final_dataframe["POSTFADE"] + final_dataframe["POSTCONTROL"] + final_dataframe["DRAWFOUL"] + final_dataframe["HANDS"])/8, 0)
final_dataframe['DEF'] = round((final_dataframe["INTERIORDEFENSE"] + final_dataframe["PERIMETERDEFENSE"] + final_dataframe["STEAL"] + final_dataframe["BLOCK"] + final_dataframe["LATERALQUICKNESS"] + final_dataframe["HELPDEFENSEIQ"] + final_dataframe["PASSPERCEPTION"] + final_dataframe["DEFENSIVECONSISTENCY"])/8, 0)
final_dataframe['ATH'] = round((final_dataframe["SPEED"] + final_dataframe["ACCELERATION"] + final_dataframe["STRENGTH"] + final_dataframe["VERTICAL"] + final_dataframe["STAMINA"] + final_dataframe["HUSTLE"] + final_dataframe["OVERALLDURABILITY"])/7, 0)
final_dataframe['PLM'] = round((final_dataframe["PASSACCURACY"] + final_dataframe["BALLHANDLE"] + final_dataframe["SPEEDWITHBALL"] + final_dataframe["PASSIQ"] + final_dataframe["PASSVISION"])/5, 0)
final_dataframe['REB'] = round((final_dataframe["OFFENSIVEREBOUND"] + final_dataframe["DEFENSIVEREBOUND"])/2, 0)

final_dataframe = final_dataframe.reset_index(drop=True)

final_dataframe.to_csv(f".\dados\complete_players_database.csv", index=False)