from PIL import Image, ImageDraw, ImageFont
import pandas as pd 
import numpy as np   
from get_nba_data import get_teams_dict

teams_dict = get_teams_dict()
text_color = (64, 52, 30)

def make_cards(index:int, text_color_rgb:tuple, card_version:str, path_for_save:str) -> None:
    """
    Essa função vai gerar e salvar a carta de um jogador com base no seu ID. Ela recebe, além do ID, 
    a cor do texto da carta no formato RGB, a versão da carta, apenas o nome sem a extensão, e o path
    de onde a carta deve ser salva.
    """
    
    text_color = text_color_rgb
    dataframe = pd.read_csv(".\dados\\final_dataframe.csv")
    dataframe.fillna(0, inplace=True)

    row_list = dataframe.loc[index, :].values.flatten().tolist()

    player_full_name = f"{row_list[2]} {row_list[1]}"
    if len(player_full_name) >= 20:
        player_full_name = row_list[1]

    player_id = row_list[0]

    image_card = Image.open(f".\design\cards_images\{card_version}.png")
    image_player = Image.open(f".\design\players_images\\{player_id}.png").convert("RGBA")
    image_league = Image.open(".\design\cards_images\league_logo.png").convert("RGBA")
    card_draw = ImageDraw.Draw(image_card)

    #SET_CARD
    largura_carta, altura_carta = image_card.size

    #SET_NAME
    text_font = ImageFont.truetype("arial.ttf", 105)
    largura_texto, altura_texto = card_draw.textsize(player_full_name, font=text_font)
    card_draw.text(((largura_carta - largura_texto)/2, 1150), player_full_name, fill=text_color, font=text_font, stroke_width=2)

    #SET_PLAYER
    image_player = image_player.resize((1000, 735))
    player_array = np.array(image_player)
    player_mask = (player_array[:, :, 3] > 0)
    image_card.paste(image_player, (144, 410), Image.fromarray(player_mask))

    #SET_OVERALL
    player_overall = str(int(row_list[5] - 5))
    text_font = ImageFont.truetype("arial.ttf", 165)
    card_draw.text((220, 300), player_overall, fill=text_color, font=text_font, stroke_width=3)

    #SET_NBA_LOGO
    image_league = image_league.resize((120, 120))
    league_array = np.array(image_league)
    league_mask = (league_array[:, :, 3] > 0)
    image_card.paste(image_league, (584, 1450), Image.fromarray(league_mask))

    #SET_TEAMS_LOGO
    team_code = teams_dict[row_list[49]]
    image_team = Image.open(f".\\design\\teams_images\\png\\{team_code}.png").convert("RGBA")
    image_team = image_team.resize((110, 110))
    team_array = np.array(image_team)
    team_mask = (team_array[:, :, 3] > 0)
    image_card.paste(image_team, (695, 1450), Image.fromarray(team_mask))

    #SET_STATS
    text_01 = "OSC"
    text_02 = "ISC"
    text_03 = "DEF"
    text_04 = "ATH"
    text_05 = "PLM"
    text_06 = "REB"
    text_font = ImageFont.truetype("arial.ttf", 65)
    card_draw.text((190, 1280), text_01, fill=text_color, font=text_font, stroke_width=0)
    card_draw.text((360, 1280), text_02, fill=text_color, font=text_font, stroke_width=0)
    card_draw.text((495, 1280), text_03, fill=text_color, font=text_font, stroke_width=0)
    card_draw.text((655, 1280), text_04, fill=text_color, font=text_font, stroke_width=0)
    card_draw.text((810, 1280), text_05, fill=text_color, font=text_font, stroke_width=0)
    card_draw.text((970, 1280), text_06, fill=text_color, font=text_font, stroke_width=0)

    #SET_SUBSTATS
    text_01 = str(int(row_list[42]))
    text_02 = str(int(row_list[43]))
    text_03 = str(int(row_list[44]))
    text_04 = str(int(row_list[45]))
    text_05 = str(int(row_list[46]))
    text_06 = str(int(row_list[47]))
    fonte = ImageFont.truetype("arial.ttf", 75)
    card_draw.text((220, 1350), text_01, fill=text_color, font=fonte, stroke_width=2)
    card_draw.text((375, 1350), text_02, fill=text_color, font=fonte, stroke_width=2)
    card_draw.text((515, 1350), text_03, fill=text_color, font=fonte, stroke_width=2)
    card_draw.text((680, 1350), text_04, fill=text_color, font=fonte, stroke_width=2)
    card_draw.text((840, 1350), text_05, fill=text_color, font=fonte, stroke_width=2)
    card_draw.text((995, 1350), text_06, fill=text_color, font=fonte, stroke_width=2)

    image_card.save(f"{path_for_save}\{player_id}_{card_version}.png")
    return None

if __name__ == "__main__":
    for i in range(463, 477):
        make_cards(i, (255, 255, 255), "card_gold")