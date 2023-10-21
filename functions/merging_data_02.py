import pandas as pd   

dataframe_01 = pd.read_csv("./dados\complete_players_database.csv")
dataframe_01 = dataframe_01.drop('TEAM', axis=1)
dataframe_01["ID"] = dataframe_01["ID"].astype(str)

dataframe_02 = pd.read_csv("./dados\web_scraping.csv")
dataframe_02["ID"] = dataframe_02["ID"].astype(int)
dataframe_02["ID"] = dataframe_02["ID"].astype(str)
dataframe_02 = dataframe_02.dropna(thresh=2)


final_dataframe = pd.merge(dataframe_01, dataframe_02, on="ID", how='inner')
final_dataframe.to_csv("./dados/final_dataframe.csv", index=False)