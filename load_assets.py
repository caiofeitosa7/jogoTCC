import os
import pygame
from pygame import mixer
from constantes import *
from itens import Objeto

mixer.init()

fundo_placar = pygame.image.load(r'assets\mapas\pn4.png')
cobre_sobra_mapa = pygame.image.load(r'assets\mapas\terra2.png')

# carregando sprites do cenário
caminho = PATH_MAPA + '\\'
files = os.listdir(caminho)
mapas = [pygame.image.load(caminho + file) for file in sorted(files)]

sala_rei = mapas[-1]

# Carregando imagens do menu de personagens
caminho = r'assets\menu\menuPersonagens\\'
files = os.listdir(caminho)
menu_personagens = [pygame.image.load(caminho + file) for file in sorted(files)]

abertura = pygame.image.load(r'assets\menu\abertura.png')

# -------------------- Carregando mensagens ---------------------
path = r'assets\mensagens'
msg_rei = pygame.image.load(path + r'\msgRei.png')
msg_atacado = pygame.image.load(path + r'\msgAtacado.png')
msg_form_final = pygame.image.load(path + r'\msgFormFinal.png')
msg_nao_encontrou = pygame.image.load(path + r'\msgNaoEncontrou.png')
msg_dragao = pygame.image.load(path + r'\popDragao.png')
msg_ogro = pygame.image.load(path + r'\popOgro.png')
msg_orc = pygame.image.load(path + r'\popOrc.png')


# --------------------- Carregando sons -------------------------
path = r'assets\sounds\\'
audio_click = pygame.mixer.Sound(path + r"Click.mp3")
audio_inicioJogo = pygame.mixer.Sound(path + r"inicioJogo.wav")
audio_decrease = pygame.mixer.Sound(path + r"Decrease.mp3")
audio_armadilha = pygame.mixer.Sound(path + r"Armadilha.wav")
audio_passarinho = pygame.mixer.Sound(path + r"passarinho.wav")
audio_addItem = pygame.mixer.Sound(path + r"inicioJogo.wav")
audio_pontua = pygame.mixer.Sound(path + r"pontua.wav")


# -------------------- Carregando itens -------------------------
path = r'assets\itens\\'
files = os.listdir(path)
figura_itens = [pygame.image.load(path + item) for item in sorted(files)]

lado_figura = 30
posicao_item = (200, 250)

itens = {
    'labirinto_orc': [
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[2], msg_atacado, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[3], msg_atacado, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[4], msg_atacado, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[1], msg_atacado, audio_click, 'item'),
    ],
    'labirinto_ogro': [
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[2], msg_atacado, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[3], msg_atacado, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[4], msg_atacado, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[1], msg_atacado, audio_click, 'item'),
    ],
    'labirinto_dragao': [
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[2], msg_atacado, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[3], msg_atacado, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[4], msg_atacado, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[1], msg_atacado, audio_click, 'item'),
    ]
}

# loc_armadilha = ()
# 
# armadilhas = [
#     Objeto(loc_armadilha, , , figura_itens[0], msg_atacado, audio_armadilha, 'armadilha'),
#     Objeto(loc_armadilha, , , figura_itens[1], msg_atacado, audio_armadilha, 'armadilha'),
# ]


# menu = pygame.image.load(r'menu\menu_principal.png')
# jogar_hover = pygame.image.load(r'menu\jogar_hover.png')
# personagem_hover = pygame.image.load(r'menu\personagem_hover.png')
# sair_hover = pygame.image.load(r'menu\sair_hover.png')