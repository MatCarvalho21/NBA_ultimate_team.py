from var_country_names import dict_rigth_countries
import pandas as pd  
dict_correct = {29: ["1628389", "Miami Heat", "13", "Center-Forward", "EUA", "26", "1997", "JULY", "18", "6"], #BAM ADEBAYO
                51: ["1641705", "San Antonio Spurs", "1", "Forward-Center", "France", "19", "2004", "JANUARY", "4", "Rookie"], #VICTOR WEMBANYAMA
                132: ["203482", "Utah Jazz", "41", "Forward-Center", "Canada", "32", "1991", "APRIL", "19", "10"], #KELLY OLYNYK
                142: ["1641706", "Charlotte Hornets", "24", "Forward", "USA", "20", "2002", "NOVEMBER", "22", "Rookie"], #BRANDON MILLER
                147: ["1630198", "Oklahoma City Thunder", "11", "Guard", "USA", "24", "1999", "JULY", "2", "3"], #ISAIAH JOE
                161: ["1630703", "Portland Trail Blazers", "00", "Guard", "USA", "19", "2004", "FEBRUARY", "3", "Rookie"], #SCOOT HENDERSON
                235: ["1641708", "Houston Rockets", "1", "Guard-Forward", "USA", "20", "2003", "JANUARY", "30", "Rookie"], #AMEN THOMPSON
                250: ["1641709", "Detroit Pistons", "9", "Guard-Forward", "USA", "20", "2003", "JANUARY", "30", "Rookie"], #AUSAR THOMPSON
                296: [None, None, None, None, None, None, None, None, None, None], #NERLENS NOEL
                327: ["203095", "New York Knicks", "13", "Guard-Forward", "France", "30", "1992", "OCTOBER", "29", "11"], #EVAN FOURNIER
                333: ["1641715", "Houston Rockets", "7", "Forward", "USA", "19", "2004", "JULY", "8", "Rookie"], #CAM WHITMORE
                343: ["203926", "San Antonio Spurs", "17", "Forward", "USA", "31", "1992", "JANUARY", "3", "9"], #DOUG MCDERMOTT
                401: [None, None, None, None, None, None, None, None, None, None], #NONE_PLAYER
                439: ["1631367", "Memphis Grizzlies", "0", "Guard", "USA", "25", "1998", "JULY", "14", "1"], #JACOB GILYARD
                444: ["1631303", "Portland Trail Blazers", "24", "Forward", "USA", "24", "1999", "MARCH", "26", "1"], #JUSTIN MINAYA
                457: [None, None, None, None, None, None, None, None, None, None], #CHANCE COMANCHE
                461: ["1630637", "Chicago Bulls", "22", "Guard", "USA", "25", "1997", "DECEMBER", "23", "2"], #CARLIK JONES
                462: [None, None, None, None, None, None, None, None, None, None]} #NONE_PLAYER 

def fixing_data(csv_path:str, path_for_save:str, to_save:bool) -> pd.DataFrame:
    """
    Essa função tem como objetivo corrigir os erros gerados pelo webscraping. Alguns jogaores ficaram
    sem dados, esse é o preço por automatizar processos. Como são poucos, resolvi fazer na mão os dados 
    e gerar a função que resove.
    """

    dataframe = pd.read_csv(f"{csv_path}")

    for each_index in dict_correct.keys():
        dict_correct[each_index].insert(0, each_index)
        dataframe.loc[each_index] = dict_correct[each_index]
    
    dataframe.reset_index(drop=True, inplace=True)

    if to_save == True:
        dataframe.to_csv("./dados\web_scraping.csv", index=False)
    
    return dataframe

def fixing_countries(path_for_csv:str, to_save:bool=False, csv_name:str="", path_to_save:str="") -> pd.DataFrame:
    """
    Essa função pega um dataframe com a coluna "COUNTRY" e gera uma nova coluna nesse dataframe
    com um código referente ao país no formato iso 3166.
    """
    dataframe = pd.read_csv(f"{path_for_csv}")

    list_of_countries = list()

    for each_country in list(dataframe["COUNTRY"]):
            if each_country == "EUA" or each_country == "USA":
                list_of_countries.append("US")
            elif each_country.upper() == "TURKEY":
                list_of_countries.append("TR")
            elif each_country == "DRC":
                list_of_countries.append("CD")
            elif each_country.upper() == "UNITED KINGDOM":
                list_of_countries.append("GB")
            else:
                list_of_countries.append(dict_rigth_countries[each_country.upper()])

    dataframe["CORRECT_COUNTRY"] = list_of_countries

    if to_save == True:
          dataframe.to_csv(f"{path_to_save}\{csv_name}", index=False)

    return dataframe

if __name__ == "__main__":
    #OK 2023_10_21
    fixing_data(".\dados\web_scraping.csv", "", False)

    #OK 2023_10_21
    fixing_countries(".\dados\\final_dataframe.csv", False, "final_dataframe.csv", ".\dados")