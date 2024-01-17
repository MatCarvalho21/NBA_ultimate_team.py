from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import numpy as np

def saveMiniCard(index:int=0, path_for_save:str="main/assets/images/mini_cards") -> None:
    """
    Creates and saves a mini card image for a player based on their information in the players.csv file.

    Args:
    index (int, optional): Index of the player in the players.csv file. Defaults to 0.
    path_for_save (str, optional): The path where the mini card image will be saved. Defaults to "main/assets/images/mini_cards".

    Returns:
    None
    """

    dataframe = pd.read_csv("main/assets/database/players.csv")
    row_list = dataframe.loc[index, :].values.flatten().tolist()

    if row_list[7] >= 90:
        im_card = Image.open("main/assets/images/cards/base_cards/mini_inform.png").convert("RGBA")
        text_color = (242, 205, 136)
    elif row_list[7] >= 85:
        im_card = Image.open("main/assets/images/cards/base_cards/mini_gold.png").convert("RGBA")
        text_color = (64, 52, 30)
    elif row_list[7] >= 80:
        im_card = Image.open("main/assets/images/cards/base_cards/mini_c_gold.png").convert("RGBA")
        text_color = (64, 52, 30)
    elif row_list[7] >= 75:
        im_card = Image.open("main/assets/images/cards/base_cards/mini_silver.png").convert("RGBA")
        text_color = (44, 44, 44)
    elif row_list[7] >= 70:
        im_card = Image.open("main/assets/images/cards/base_cards/mini_c_silver.png").convert("RGBA")
        text_color = (44, 44, 44)
    elif row_list[7] >= 68:
        im_card = Image.open("main/assets/images/cards/base_cards/mini_bronze.png").convert("RGBA")
        text_color = (64, 39, 30)
    else:
        im_card = Image.open("main/assets/images/cards/base_cards/mini_c_bronze.png").convert("RGBA")
        text_color = (64, 39, 30)

    im_player = Image.open(f"main/assets/images/players/{row_list[1]}.png").convert("RGBA")
    im_league = Image.open("main/assets/images/league_image.png").convert("RGBA")
    im_flag = Image.open(f"main/assets/images/flags/{row_list[-1].lower()}.png")

    card_draw = ImageDraw.Draw(im_card)

    im_card = im_card.resize((1300, 1550))

    # FLAGS
    if row_list[-1] == "CH":
        im_flag = im_flag.resize((100, 100))
        im_card.paste(im_flag, (350, 1205))
    else:
        im_flag = im_flag.resize((160, 100))
        im_card.paste(im_flag, (320, 1205))
        
    # LEAGUE
    im_league = im_league.resize((200, 200))
    league_ar = np.array(im_league)
    league_mk = (league_ar[:, :, 3] > 0)
    im_card.paste(im_league, (550, 1155), Image.fromarray(league_mk))

    # TEAM
    team_name = (row_list[-11].lower()).replace(" ", "_")
    im_team = Image.open(f"main/assets/images/teams/logo_{team_name}.png").convert("RGBA")
    if team_name == "unemployed":
        im_team = im_team.resize((140, 140))
        team_ar = np.array(im_team)
        team_mk = (team_ar[:, :, 3] > 0)
        im_card.paste(im_team, (800, 1180), Image.fromarray(team_mk))
    else:
        im_team = im_team.resize((180, 180))
        team_ar = np.array(im_team)
        team_mk = (team_ar[:, :, 3] > 0)
        im_card.paste(im_team, (800, 1155), Image.fromarray(team_mk))

    # PLAYER
    im_player = im_player.resize((900, 700))
    player_ar = np.array(im_player)
    player_mk = (player_ar[:, :, 3] > 200)
    im_card.paste(im_player, (200, 420), Image.fromarray(player_mk))

    # OVERALL
    card_draw = ImageDraw.Draw(im_card)
    font = ImageFont.truetype("main/assets/fonts/arial.ttf", 180)
    text_width = card_draw.textlength(str(row_list[7]), font)
    card_draw.text(((550 - text_width)/2, 350), str(row_list[7]), text_color, font=font, stroke_width=3)

    # POSITION
    font = ImageFont.truetype("main/assets/fonts/arial.ttf", 50)
    text_width = card_draw.textlength(str(row_list[-2]), font)
    card_draw.text(((550 - text_width)/2, 525), str(row_list[-2]), text_color, font=font, stroke_width=1)

    im_card.save(path_for_save + f"/{row_list[1]}.png")