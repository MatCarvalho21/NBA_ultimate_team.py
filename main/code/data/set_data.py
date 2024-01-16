"""
LISTA DE JOGADORES QUE ESTÃO EM UMA BASE DE DADOS, MAS NÃO NA OUTRA E, POR ISSO, SERÃO CORTADOS
['Danny Green', 'Duane Washington Jr', 'Filip Petrusev', 'Kaiser Gates', 'Ibou Badji', 'Jaylen Martin', 'Shaquille Harrison', 'Xavier Moon']

OBS.: FORAM NECESSÁRIAS ALGUMAS CORREÇÕES MANUAIS EM AMBOS OS ARQUIVOS PARA QUE NOMES IGUAIS, MAS COM DIGITAÇÃO DIFERENTE, NÃO FOSSEM DEIXADOS DE FORA
"""

import pandas as pd

def mergeData(dataframe1:pd.DataFrame, macth_column_1:str, dataframe2:pd.DataFrame, macth_column_2:str, column_for_delete:str=None) -> pd.DataFrame:
    """
    Merges two dataframes horizontally based on matching columns and optionally deletes a specified column.

    Args:
    dataframe1 (pd.DataFrame): The first dataframe.
    match_column_1 (str): The column in the first dataframe for matching.
    dataframe2 (pd.DataFrame): The second dataframe.
    match_column_2 (str): The column in the second dataframe for matching.
    column_for_delete (str, optional): The column to be deleted from the merged dataframe. Defaults to None.

    Returns:
    pd.DataFrame: Merged dataframe with rows matched based on the specified columns.
    """

    merge_dataframe = pd.merge(dataframe1, dataframe2, left_on=macth_column_1, right_on=macth_column_2, how='inner').reset_index(drop=True)
    if column_for_delete != None:
        merge_dataframe = merge_dataframe.drop(column_for_delete, axis=1)

    return merge_dataframe