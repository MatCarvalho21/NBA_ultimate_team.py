
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import numpy as np

def makeCards(index:int=0, path_for_save:str="main/assets/images/full_cards") -> None:
    """
    Creates and saves a full card image for a player based on their information in the players.csv file.

    Args:
    index (int, optional): Index of the player in the players.csv file. Defaults to 0.
    path_for_save (str, optional): The path where the full card image will be saved. Defaults to "main/assets/images/full_cards".

    Returns:
    None
    """
    dataframe = pd.read_csv("main/assets/database/players.csv")
    row_list = dataframe.loc[index, :].values.flatten().tolist()

    if row_list[7] >= 95:
        im_card = Image.open("main/assets/images/cards/base_cards/full_inform.png").convert("RGBA")
        text_color = (242, 205, 136)
    elif row_list[7] >= 85:
        im_card = Image.open("main/assets/images/cards/base_cards/full_gold.png").convert("RGBA")
        text_color = (64, 52, 30)
    elif row_list[7] >= 80:
        im_card = Image.open("main/assets/images/cards/base_cards/full_c_gold.png").convert("RGBA")
        text_color = (64, 52, 30)
    elif row_list[7] >= 75:
        im_card = Image.open("main/assets/images/cards/base_cards/full_silver.png").convert("RGBA")
        text_color = (44, 44, 44)
    elif row_list[7] >= 70:
        im_card = Image.open("main/assets/images/cards/base_cards/full_c_silver.png").convert("RGBA")
        text_color = (44, 44, 44)
    elif row_list[7] >= 68:
        im_card = Image.open("main/assets/images/cards/base_cards/full_bronze.png").convert("RGBA")
        text_color = (64, 39, 30)
    else:
        im_card = Image.open("main/assets/images/cards/base_cards/full_c_bronze.png").convert("RGBA")
        text_color = (64, 39, 30)

    im_player = Image.open(f"main/assets/images/players/{row_list[1]}.png").convert("RGBA")
    im_league = Image.open("main/assets/images/league_image.png").convert("RGBA")
    im_flag = Image.open(f"main/assets/images/flags/{row_list[-1].lower()}.png")

    im_card = im_card.resize((1300, 1800))

    # FLAGS
    if row_list[-1] == "CH":
        im_flag = im_flag.resize((80, 80))
        im_card.paste(im_flag, (465, 1485))
    else:
        im_flag = im_flag.resize((120, 80))
        im_card.paste(im_flag, (425, 1485))

    # LEAGUE
    im_league = im_league.resize((150, 150))
    league_ar = np.array(im_league)
    league_mk = (league_ar[:, :, 3] > 200)
    im_card.paste(im_league, (575, 1450), Image.fromarray(league_mk))

    # TEAM
    team_name = (row_list[-11].lower()).replace(" ", "_")
    im_team = Image.open(f"main/assets/images/teams/logo_{team_name}.png").convert("RGBA")
    im_team = im_team.resize((120, 120))
    team_ar = np.array(im_team)
    team_mk = (team_ar[:, :, 3] > 200)
    im_card.paste(im_team, (750, 1460), Image.fromarray(team_mk))

    # PLAYER
    im_player = im_player.resize((1050, 800))
    player_ar = np.array(im_player)
    player_mk = (player_ar[:, :, 3] > 200)
    im_card.paste(im_player, (125, 380), Image.fromarray(player_mk))

    # OVERALL
    card_draw = ImageDraw.Draw(im_card)
    font = ImageFont.truetype("main/assets/fonts/arial.ttf", 180)
    text_width = card_draw.textlength(str(row_list[7]), font)
    card_draw.text(((550 - text_width)/2, 300), str(row_list[7]), text_color, font=font, stroke_width=3)

    # POSITION
    font = ImageFont.truetype("main/assets/fonts/arial.ttf", 50)
    text_width = card_draw.textlength(str(row_list[-2]), font)
    card_draw.text(((550 - text_width)/2, 475), str(row_list[-2]), text_color, font=font, stroke_width=1)

    # NAME
    player_full_name = f"{row_list[3].upper()} {row_list[2].upper()}"
    if len(player_full_name) >= 18:
        player_full_name = row_list[2].upper()
    font = ImageFont.truetype("main/assets/fonts/arial.ttf", 90)
    text_width = card_draw.textlength(player_full_name, font)
    card_draw.text(((1300 - text_width)/2, 1190), player_full_name, text_color, font=font, stroke_width=2)

    # ATRIBUTE NAME
    font = ImageFont.truetype("main/assets/fonts/arial.ttf", 70)
    osco = "OSC"
    text_width = card_draw.textlength(osco, font)
    card_draw.text(((475 - text_width)/2, 1300), osco, text_color, font=font, stroke_width=1)

    isco = "ISC"
    text_width = card_draw.textlength(isco, font)
    card_draw.text(((800 - text_width)/2, 1300), isco, text_color, font=font, stroke_width=1)

    defe = "DEF"
    text_width = card_draw.textlength(defe, font)
    card_draw.text(((1125 - text_width)/2, 1300), defe, text_color, font=font, stroke_width=1)

    athl = "ATH"
    text_width = card_draw.textlength(athl, font)
    card_draw.text(((1450 - text_width)/2, 1300), athl, text_color, font=font, stroke_width=1)
    plmk = "PLM"
    text_width = card_draw.textlength(plmk, font)
    card_draw.text(((1775 - text_width)/2, 1300), plmk, text_color, font=font, stroke_width=1)
    rebo = "REB"
    text_width = card_draw.textlength(rebo, font)
    card_draw.text(((2100 - text_width)/2, 1300), rebo, text_color, font=font, stroke_width=1)

    # ATRIBUTE
    font = ImageFont.truetype("main/assets/fonts/arial.ttf", 70)
    osco = str(int(round(sum(row_list[8:14])/len(row_list[8:14]), 0)))
    text_width = card_draw.textlength(osco, font)
    card_draw.text(((475 - text_width)/2, 1375), osco, text_color, font=font, stroke_width=0)
    isco = str(int(round(sum(row_list[14:22])/len(row_list[14:22]), 0)))
    text_width = card_draw.textlength(isco, font)
    card_draw.text(((800 - text_width)/2, 1375), isco, text_color, font=font, stroke_width=0)
    defe = str(int(round(sum(row_list[22:30])/len(row_list[22:30]), 0)))
    text_width = card_draw.textlength(defe, font)
    card_draw.text(((1125 - text_width)/2, 1375), defe, text_color, font=font, stroke_width=0)
    athl = str(int(round(sum(row_list[30:37])/len(row_list[30:37]), 0)))
    text_width = card_draw.textlength(athl, font)
    card_draw.text(((1450 - text_width)/2, 1375), athl, text_color, font=font, stroke_width=0)
    plmk = str(int(round(sum(row_list[37:42])/len(row_list[37:42]), 0)))
    text_width = card_draw.textlength(plmk, font)
    card_draw.text(((1775 - text_width)/2, 1375), plmk, text_color, font=font, stroke_width=0)
    rebo = str(int(round(sum(row_list[42:44])/len(row_list[42:44]), 0)))
    text_width = card_draw.textlength(rebo, font)
    card_draw.text(((2100 - text_width)/2, 1375), rebo, text_color, font=font, stroke_width=0)

    im_card.save(f"{path_for_save}/full_{row_list[1]}.png")