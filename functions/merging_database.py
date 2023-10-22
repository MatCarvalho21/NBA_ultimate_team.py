import pandas as pd 

def merging_dataframes(to_save:bool=True, path_for_save:str="", csv_name:str="", error_players:bool=False) -> pd.DataFrame:
    """
    Essa função é extremamente específica e vai fazer o merge de apenas dois dataframes. Um com os dados dos 
    jogadores oriundos da biblioteca NBA API e o outro com os ratings dos jogadores. Ela vai gerar um dataframe,
    mas se for o caso ela vai salvar, se não for passado o parâmetro, ela vai salvar no formato csv.
    """
    dataframe_ratings = pd.read_csv(".\dados\players_ratings.csv")
    dataframe_players = pd.read_csv(".\dados\players_data.csv")

    columns_01 = list(dataframe_ratings.columns)
    dataframe_ratings = dataframe_ratings.set_index("NAME", drop=True)
    columns_02 = list(dataframe_players.columns)
    del columns_02[3]
    dataframe_players = dataframe_players.set_index("FULL_NAME", drop=True)

    list_of_players = list(dataframe_ratings.index)

    list_of_data = list()
    dict_of_none_players = dict()

    for each_player in list_of_players:
        try:
            list_01 = list(dataframe_players.loc[each_player])
            list_02 = list(dataframe_ratings.loc[each_player])
            list_of_data.append(list_01 + list_02)
        except KeyError:
            dict_of_none_players[f"{each_player}"] = list_of_data

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

    if to_save == True:
        final_dataframe.to_csv(f"{path_for_save}\{csv_name}", index=False)

    if error_players == True:
        return final_dataframe, dict_of_none_players
    
    else:
        return final_dataframe

def merging_dataframes_two(to_save:bool=True, path_for_save:str="", csv_name:str="") -> pd.DataFrame:
    """
    Essa função vai fazer o merge de dois arquivos csv específicos, por isso não 
    é passado nenhuma base de dados. O critério vai ser o ID. O máximo que é possível fazer
    é configurar onde será salva esse dataframe e se será salvo.
    """
    dataframe_01 = pd.read_csv("./dados\complete_players_database.csv")
    dataframe_01 = dataframe_01.drop('TEAM', axis=1)
    dataframe_01["ID"] = dataframe_01["ID"].astype(str)

    dataframe_02 = pd.read_csv("./dados\web_scraping.csv")
    dataframe_02["ID"] = dataframe_02["ID"].astype(int)
    dataframe_02["ID"] = dataframe_02["ID"].astype(str)
    dataframe_02 = dataframe_02.dropna(thresh=2)

    final_dataframe = pd.merge(dataframe_01, dataframe_02, on="ID", how='inner')

    if to_save == True:
        final_dataframe.to_csv(f"{path_for_save}\{csv_name}", index=False)

    return final_dataframe

if __name__ == "__main__":
    #OK 2023_10_21
    merging_dataframes(to_save=False, error_players=True)[1].keys() #LISTA DE JOGADORES QUE FICARAM DE FORA
    merging_dataframes(to_save=False)

    #OK 2023_10_21
    merging_dataframes(to_save=False).head()