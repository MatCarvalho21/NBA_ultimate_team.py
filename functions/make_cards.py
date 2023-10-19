from PIL import Image, ImageDraw, ImageFont
import pandas as pd 
import numpy as np   

"""
text_color = (64, 52, 30)
#pega as imagens das cartas e dos jogadores
carta = Image.open(".\design\cards_images\_80.png")
imagem_jogador = Image.open(".\design\players_images\\1628369.png").convert("RGBA")
imagem_nba = Image.open(".\design\cards_images\logo-nba-4096.png").convert("RGBA")
flag_imagem = Image.open(".\\design\\cards_images\\us.png").convert("RGBA")
imagem_time = Image.open(".\\design\\cards_images\\1610612738.png").convert("RGBA")

#pega a imagem do jogador e arruma as suas dimensões
imagem_jogador = imagem_jogador.resize((1000, 735))
imagem_nba = imagem_nba.resize((120, 120))
flag_imagem = flag_imagem.resize((110, 72))
imagem_time = imagem_time.resize((110, 110))

#verifica e "ativa" a transparência da imagem do jogador
jogador_array = np.array(imagem_jogador)
mascara_jogador = (jogador_array[:, :, 3] > 0)

flag_array = np.array(flag_imagem)
mascara_flag = (flag_array[:, :, 3] > 0)

nba_array = np.array(imagem_nba)
mascara_nba = (nba_array[:, :, 3] > 0)

time_array = np.array(imagem_time)
mascara_time = (time_array[:, :, 3] > 0)



#cola a imagem do jogador sobre a imagem da carta, ativando a transparência e posicionando ela
carta.paste(imagem_jogador, (144, 400), Image.fromarray(mascara_jogador))
carta.paste(imagem_nba, (584, 1450), Image.fromarray(mascara_nba))
carta.paste(imagem_time, (695, 1450), Image.fromarray(mascara_time))
carta.paste(flag_imagem, (465, 1474), Image.fromarray(mascara_flag))

desenho = ImageDraw.Draw(carta)
fonte = ImageFont.truetype("arial.ttf", 105)

# Texto a ser exibido
nome = "Jayson Tatum"

largura_carta, altura_carta = carta.size

# Calcule a posição centralizada para o texto
largura_texto, altura_texto = desenho.textsize(nome, font=fonte)
x = (largura_carta - largura_texto) / 2

meio_da_carta = 644

y = 1150  # Altura desejada para o texto

# Adicione o texto centralizado à carta
desenho.text((x, y), nome, fill=text_color, font=fonte, stroke_width=2)

over = "90"
fonte = ImageFont.truetype("arial.ttf", 165)
desenho.text((220, 300), over, fill=text_color, font=fonte, stroke_width=3)

position = "SF"
fonte = ImageFont.truetype("arial.ttf", 80)
desenho.text((260, 490), position, fill=text_color, font=fonte, stroke_width=0)

text_01 = "OSC"
text_02 = "ISC"
text_03 = "DEF"
text_04 = "ATH"
text_05 = "PLM"
text_06 = "REB"
fonte = ImageFont.truetype("arial.ttf", 65)
desenho.text((190, 1280), text_01, fill=text_color, font=fonte, stroke_width=0)
desenho.text((360, 1280), text_02, fill=text_color, font=fonte, stroke_width=0)
desenho.text((495, 1280), text_03, fill=text_color, font=fonte, stroke_width=0)
desenho.text((655, 1280), text_04, fill=text_color, font=fonte, stroke_width=0)
desenho.text((810, 1280), text_05, fill=text_color, font=fonte, stroke_width=0)
desenho.text((970, 1280), text_06, fill=text_color, font=fonte, stroke_width=0)

number_01 = "90"
number_02 = "84"
number_03 = "83"
number_04 = "84"
number_05 = "79"
number_06 = "78"
fonte = ImageFont.truetype("arial.ttf", 75)
desenho.text((220, 1350), number_01, fill=text_color, font=fonte, stroke_width=2)
desenho.text((375, 1350), number_02, fill=text_color, font=fonte, stroke_width=2)
desenho.text((515, 1350), number_03, fill=text_color, font=fonte, stroke_width=2)
desenho.text((680, 1350), number_04, fill=text_color, font=fonte, stroke_width=2)
desenho.text((840, 1350), number_05, fill=text_color, font=fonte, stroke_width=2)
desenho.text((995, 1350), number_06, fill=text_color, font=fonte, stroke_width=2)

#salva a imagem
carta.save("carta.png")

##########################################################################################################

#pega as imagens das cartas e dos jogadores
carta = Image.open(".\design\cards_images\_80.png")
imagem_jogador = Image.open(".\design\players_images\\203999.png").convert("RGBA")
imagem_nba = Image.open(".\design\cards_images\logo-nba-4096.png").convert("RGBA")
flag_imagem = Image.open(".\\design\\cards_images\\rs.png").convert("RGBA")
imagem_time = Image.open(".\\design\\cards_images\\1610612743.png").convert("RGBA")

#pega a imagem do jogador e arruma as suas dimensões
imagem_jogador = imagem_jogador.resize((1000, 735))
imagem_nba = imagem_nba.resize((120, 120))
flag_imagem = flag_imagem.resize((110, 72))
imagem_time = imagem_time.resize((110, 110))

#verifica e "ativa" a transparência da imagem do jogador
jogador_array = np.array(imagem_jogador)
mascara_jogador = (jogador_array[:, :, 3] > 0)

flag_array = np.array(flag_imagem)
mascara_flag = (flag_array[:, :, 3] > 0)

nba_array = np.array(imagem_nba)
mascara_nba = (nba_array[:, :, 3] > 0)

time_array = np.array(imagem_time)
mascara_time = (time_array[:, :, 3] > 0)



#cola a imagem do jogador sobre a imagem da carta, ativando a transparência e posicionando ela
carta.paste(imagem_jogador, (144, 400), Image.fromarray(mascara_jogador))
carta.paste(imagem_nba, (584, 1450), Image.fromarray(mascara_nba))
carta.paste(imagem_time, (695, 1450), Image.fromarray(mascara_time))
carta.paste(flag_imagem, (465, 1474), Image.fromarray(mascara_flag))

desenho = ImageDraw.Draw(carta)
fonte = ImageFont.truetype("arial.ttf", 105)

# Texto a ser exibido
nome = "Nikola Jokic"

largura_carta, altura_carta = carta.size

# Calcule a posição centralizada para o texto
largura_texto, altura_texto = desenho.textsize(nome, font=fonte)
x = (largura_carta - largura_texto) / 2

meio_da_carta = 644

y = 1150  # Altura desejada para o texto

# Adicione o texto centralizado à carta
desenho.text((x, y), nome, fill=text_color, font=fonte, stroke_width=2)

over = "93"
fonte = ImageFont.truetype("arial.ttf", 165)
desenho.text((220, 300), over, fill=text_color, font=fonte, stroke_width=3)

position = "CE"
fonte = ImageFont.truetype("arial.ttf", 80)
desenho.text((260, 490), position, fill=text_color, font=fonte, stroke_width=0)

text_01 = "OSC"
text_02 = "ISC"
text_03 = "DEF"
text_04 = "ATH"
text_05 = "PLM"
text_06 = "REB"
fonte = ImageFont.truetype("arial.ttf", 65)
desenho.text((190, 1280), text_01, fill=text_color, font=fonte, stroke_width=0)
desenho.text((360, 1280), text_02, fill=text_color, font=fonte, stroke_width=0)
desenho.text((495, 1280), text_03, fill=text_color, font=fonte, stroke_width=0)
desenho.text((655, 1280), text_04, fill=text_color, font=fonte, stroke_width=0)
desenho.text((810, 1280), text_05, fill=text_color, font=fonte, stroke_width=0)
desenho.text((970, 1280), text_06, fill=text_color, font=fonte, stroke_width=0)

number_01 = "93"
number_02 = "90"
number_03 = "65"
number_04 = "77"
number_05 = "85"
number_06 = "80"
fonte = ImageFont.truetype("arial.ttf", 75)
desenho.text((220, 1350), number_01, fill=text_color, font=fonte, stroke_width=2)
desenho.text((375, 1350), number_02, fill=text_color, font=fonte, stroke_width=2)
desenho.text((515, 1350), number_03, fill=text_color, font=fonte, stroke_width=2)
desenho.text((680, 1350), number_04, fill=text_color, font=fonte, stroke_width=2)
desenho.text((840, 1350), number_05, fill=text_color, font=fonte, stroke_width=2)
desenho.text((995, 1350), number_06, fill=text_color, font=fonte, stroke_width=2)

#salva a imagem
carta.save("carta2.png")

##########################################################################################################

#pega as imagens das cartas e dos jogadores
carta = Image.open(".\design\cards_images\_80.png")
imagem_jogador = Image.open(".\design\players_images\\203507.png").convert("RGBA")
imagem_nba = Image.open(".\design\cards_images\logo-nba-4096.png").convert("RGBA")
flag_imagem = Image.open(".\\design\\cards_images\\gr.png").convert("RGBA")
imagem_time = Image.open(".\\design\\cards_images\\1610612749.png").convert("RGBA")

#pega a imagem do jogador e arruma as suas dimensões
imagem_jogador = imagem_jogador.resize((1000, 735))
imagem_nba = imagem_nba.resize((120, 120))
flag_imagem = flag_imagem.resize((110, 72))
imagem_time = imagem_time.resize((110, 110))

#verifica e "ativa" a transparência da imagem do jogador
jogador_array = np.array(imagem_jogador)
mascara_jogador = (jogador_array[:, :, 3] > 0)

flag_array = np.array(flag_imagem)
mascara_flag = (flag_array[:, :, 3] > 0)

nba_array = np.array(imagem_nba)
mascara_nba = (nba_array[:, :, 3] > 0)

time_array = np.array(imagem_time)
mascara_time = (time_array[:, :, 3] > 0)



#cola a imagem do jogador sobre a imagem da carta, ativando a transparência e posicionando ela
carta.paste(imagem_jogador, (144, 400), Image.fromarray(mascara_jogador))
carta.paste(imagem_nba, (584, 1450), Image.fromarray(mascara_nba))
carta.paste(imagem_time, (695, 1450), Image.fromarray(mascara_time))
carta.paste(flag_imagem, (465, 1474), Image.fromarray(mascara_flag))

desenho = ImageDraw.Draw(carta)
fonte = ImageFont.truetype("arial.ttf", 105)

# Texto a ser exibido
nome = "G. Antetokounmpo"

largura_carta, altura_carta = carta.size

# Calcule a posição centralizada para o texto
largura_texto, altura_texto = desenho.textsize(nome, font=fonte)
x = (largura_carta - largura_texto) / 2

meio_da_carta = 644

y = 1150  # Altura desejada para o texto

# Adicione o texto centralizado à carta
desenho.text((x, y), nome, fill=text_color, font=fonte, stroke_width=2)

over = "92"
fonte = ImageFont.truetype("arial.ttf", 165)
desenho.text((220, 300), over, fill=text_color, font=fonte, stroke_width=3)

position = "PF"
fonte = ImageFont.truetype("arial.ttf", 80)
desenho.text((260, 490), position, fill=text_color, font=fonte, stroke_width=0)

text_01 = "OSC"
text_02 = "ISC"
text_03 = "DEF"
text_04 = "ATH"
text_05 = "PLM"
text_06 = "REB"
fonte = ImageFont.truetype("arial.ttf", 65)
desenho.text((190, 1280), text_01, fill=text_color, font=fonte, stroke_width=0)
desenho.text((360, 1280), text_02, fill=text_color, font=fonte, stroke_width=0)
desenho.text((495, 1280), text_03, fill=text_color, font=fonte, stroke_width=0)
desenho.text((655, 1280), text_04, fill=text_color, font=fonte, stroke_width=0)
desenho.text((810, 1280), text_05, fill=text_color, font=fonte, stroke_width=0)
desenho.text((970, 1280), text_06, fill=text_color, font=fonte, stroke_width=0)

number_01 = "78"
number_02 = "88"
number_03 = "83"
number_04 = "91"
number_05 = "85"
number_06 = "76"
fonte = ImageFont.truetype("arial.ttf", 75)
desenho.text((220, 1350), number_01, fill=text_color, font=fonte, stroke_width=2)
desenho.text((375, 1350), number_02, fill=text_color, font=fonte, stroke_width=2)
desenho.text((515, 1350), number_03, fill=text_color, font=fonte, stroke_width=2)
desenho.text((680, 1350), number_04, fill=text_color, font=fonte, stroke_width=2)
desenho.text((840, 1350), number_05, fill=text_color, font=fonte, stroke_width=2)
desenho.text((995, 1350), number_06, fill=text_color, font=fonte, stroke_width=2)

#salva a imagem
carta.save("carta3.png")
"""
text_color = (64, 52, 30)

def make_cards(index:int, text_color_rgb:tuple, card_version:str) -> None:
    """
    """
    text_color = text_color_rgb
    dataframe = pd.read_csv(".\dados\complete_players_database.csv")

    row_list = dataframe.loc[index, :].values.flatten().tolist()

    player_full_name = f"{row_list[2]} {row_list[1]}"
    if len(player_full_name) >= 15:
        player_full_name = row_list[1]

    player_id = row_list[0]

    image_card = Image.open(f".\design\cards_images\{card_version}.png")
    image_player = Image.open(f".\design\players_images\\{player_id}.png").convert("RGBA")
    image_league = Image.open(".\design\cards_images\logo-nba-4096.png").convert("RGBA")

    #SET_CARD
    largura_carta, altura_carta = image_card.size

    #SET_PLAYER
    image_player = image_player.resize((1000, 735))
    player_array = np.array(image_player)
    player_mask = (player_array[:, :, 3] > 0)
    image_card.paste(image_player, (144, 400), Image.fromarray(player_mask))


    image_card.save(f".\design\\test_images\card_{index}.png")
    return None

for i in range(1, 11):
    make_cards(i, (64, 52, 30), "86_90")