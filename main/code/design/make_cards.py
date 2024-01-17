
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import numpy as np

dataframe = pd.read_csv("main/assets/database/players.csv")
row_list = dataframe.loc[0, :].values.flatten().tolist()
print(row_list)

im_card = Image.open("main/assets/images/cards/base_cards/full_gold.png").convert("RGBA")
im_player = Image.open(f"main/assets/images/players/{row_list[1]}.png").convert("RGBA")
im_league = Image.open("main/assets/images/league_image.png").convert("RGBA")
im_flag = Image.open(f"main/assets/images/flags/{row_list[-1].lower()}.png")

card_draw = ImageDraw.Draw(im_card)

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
league_mk = (league_ar[:, :, 3] > 0)
im_card.paste(im_league, (575, 1450), Image.fromarray(league_mk))

# TEAM
team_name = (row_list[-11].lower()).replace(" ", "_")
im_team = Image.open(f"main/assets/images/teams/logo_{team_name}.png")
im_team = im_team.resize((120, 120))
team_ar = np.array(im_team)
team_mk = (team_ar[:, :, 3] > 0)
im_card.paste(im_team, (750, 1460), Image.fromarray(team_mk))

# PLAYER
im_player = im_player.resize((1050, 800))
player_ar = np.array(im_player)
player_mk = (player_ar[:, :, 3] > 200)
im_card.paste(im_player, (125, 390), Image.fromarray(player_mk))

im_card.save("teste.png")