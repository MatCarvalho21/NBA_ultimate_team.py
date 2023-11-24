

import pandas as pd 

dataframe = pd.read_csv("dados\\final_dataframe.csv")

columns_tuple = ('PLAYER_ID', 'LAST_NAME', 'FIRST_NAME', 'ACTIVE', 'IMAGE_URL', 'OVERALL', 
                 'CLOSE_SHOT', 'MID_RANGE_SHOT', 'THREE_PT_SHOT', 'FREE_THROW', 'SHOT_IQ', 
                 'OF_CONSISTENCY', 'LAYUP', 'STANDING_DUNK', 'DRIVING_DUNK', 'POST_HOOK', 
                 'POST_FADE', 'POST_CONTROL', 'DRAW_FOUL', 'HANDS', 'INTERIOR_DEF', 'PERIMETER_DEF', 
                 'STEAL', 'BLK', 'LATERAL_QUICKNESS', 'HELP_DEF_IQ', 'PASS_PERCEPTION', 
                 'DEF_CONSISTENCY', 'SPEED', 'ACCELERATION', 'STRENGTH', 'VERTICAL', 'STAMINA', 
                 'HUSTLE', 'OVER_DURABILITY', 'PASS_ACCURACY', 'BALL_HANDLE', 'SPEED_WITH_BALL', 'PASS_IQ', 
                 'PASS_VISION', 'OFE_REB', 'DEF_REB', 'OSC', 'ISC', 'DEF', 'ATH', 'PLM', 
                 'REB', 'TEAM_NAME', 'JERSEY_NUM', 'POSITION', 'COUNTRY_NAME', 'PLAYER_AGE', 'BD_DATE',
                 'YEARS_EXP', 'COUNTRY_CODE')

months_dict = {
    'JANUARY': 1,
    'FEBRUARY': 2,
    'MARCH': 3,
    'APRIL': 4,
    'MAY': 5,
    'JUNE': 6,
    'JULY': 7,
    'AUGUST': 8,
    'SEPTEMBER': 9,
    'OCTOBER': 10,
    'NOVEMBER': 11,
    'DECEMBER': 12
}

ignored_columns = [48, 54, 54]

list_of_text = list()

for row_index in range(0, dataframe.shape[0]):
    row_list = dataframe.loc[row_index, :].values.flatten().tolist()
    row_list[54] = f"{int(row_list[54])}-{months_dict[row_list[55]]}-{int(row_list[56])}"

    for index in ignored_columns:
        row_list.pop(index)

    list_of_text.append(f"INSERT INTO NBA_UT {columns_tuple} VALUES {tuple(row_list[1:])}")

with open('C:\\Users\\mathe\\NBA_ultimate_team\\sql\\test_file.txt', "w") as file:
    for index in range(0, len(list_of_text)):
        file.write(f"{list_of_text[index]}\n\n")
