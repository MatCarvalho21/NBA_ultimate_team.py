from PIL import Image, ImageDraw, ImageFont
import pandas as pd 
import numpy as np   
from get_nba_data import get_teams_dict

dict_positions = {
    "Guard":"PG/SG",
    "Forward":"SF/PF",
    "Center":"CE/PF",
    "Guard-Forward":"SG/SF",
    "Forward-Center":"PF/CE",
    "Center-Forward":"CE/PF",
    "Forward-Guard":"SF/SG", 
}

teams_dict = get_teams_dict()
text_color = (64, 52, 30)

def make_cards(index:int, text_color_rgb:tuple, card_version:str, to_save:bool=False, path_for_save:str="") -> None:
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
    flag_code = row_list[58]

    image_card = Image.open(f".\design\cards_images\{card_version}.png")
    image_player = Image.open(f".\design\players_images\\{player_id}.png").convert("RGBA")
    image_league = Image.open(".\design\cards_images\league_logo.png").convert("RGBA")
    image_flag = Image.open(f".\design\\flags_images\{flag_code}.png")
    card_draw = ImageDraw.Draw(image_card)

    #SET_CARD
    largura_carta, altura_carta = image_card.size

    #SET_FLAG
    if flag_code == "CH":
        image_flag = image_flag.resize((70, 70))
        image_card.paste(image_flag, (500, 1470))
    else:
        image_flag = image_flag.resize((100, 70))
        image_card.paste(image_flag, (470, 1475))

    #SET_NAME
    text_font = ImageFont.truetype("arial.ttf", 105)
    largura_texto, altura_texto = card_draw.textsize(player_full_name, font=text_font)
    card_draw.text(((largura_carta - largura_texto)/2, 1150), player_full_name, fill=text_color, font=text_font, stroke_width=2)

    #SET_PLAYER
    image_player = image_player.resize((1000, 735))
    player_array = np.array(image_player)
    player_mask = (player_array[:, :, 3] > 0)
    image_card.paste(image_player, (144, 410), Image.fromarray(player_mask))

    #SET_POSITION
    position = dict_positions[row_list[51]]
    text_font = ImageFont.truetype("arial.ttf", 55)
    card_draw.text((228, 480), position, fill=text_color, font=text_font, stroke_width=1)

    #SET_OVERALL
    player_overall = str(int(row_list[5]))
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

    if to_save == True:
        image_card.save(f"{path_for_save}\{index}_{row_list[1].lower()}_{row_list[2].lower()}_{player_id}.png")

    return None

if __name__ == "__main__":
    """
    for indice in range(0, 100):
        make_cards(indice, text_color, "card_gold", False, ".\cartas\cartas_ouro")

    lista_de_exemplos = [0, 2, 3, 4, 5, 7]
    dict_de_cartas = {"card_gold":text_color, 
                        "card_purple":(255,255,255),
                        "card_default":(255,255,255), 
                        "card_centurion":(255,255,255)}

    for indice in range(0, 6):
        chave = indice
        if indice >= 4:
            indice = indice - 4
        make_cards(lista_de_exemplos[chave], list(dict_de_cartas.values())[indice], list(dict_de_cartas.keys())[indice], False, ".\cartas\exemplos")
    
    lista_de_jogadores_celtic = [7, 19, 35, 27, 80]
    for indice in lista_de_jogadores_celtic:
        make_cards(indice, text_color, "card_gold", False, ".\cartas\celtics_lineup")
    """
    lista_de_jogadores_celtic = [0, 23, 159, 67, 49]
    for indice in lista_de_jogadores_celtic:
        make_cards(indice, text_color, "card_gold", True, ".\cartas\\nuguets_lineup")