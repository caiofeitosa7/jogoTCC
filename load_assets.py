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


# --------------------- Carregando sons -------------------------
path = r'assets\sounds\\'
audio_click = pygame.mixer.Sound(path + "Click.mp3")
audio_inicioJogo = pygame.mixer.Sound(path + "inicioJogo.wav")
audio_decrease = pygame.mixer.Sound(path + "Decrease.mp3")
audio_armadilha = pygame.mixer.Sound(path + "Armadilha.wav")
audio_passarinho = pygame.mixer.Sound(path + "passarinho.wav")
audio_addItem = pygame.mixer.Sound(path + "inicioJogo.wav")
audio_pontua = pygame.mixer.Sound(path + "pontua.wav")


# -------------------- Carregando mensagens ---------------------
path = r'assets\mensagens\\'
msg_rei = pygame.image.load(path + 'msgRei.png')
msg_atacado = pygame.image.load(path + 'msgAtacado.png')
msg_form_final = pygame.image.load(path + 'msgFormFinal.png')
msg_nao_encontrou = pygame.image.load(path + 'msg_encontrou_nada.jpg')
msg_armadilha = pygame.image.load(path + 'msg_armadilha.jpg')
msg_dragao = pygame.image.load(path + 'popDragao.png')
msg_ogro = pygame.image.load(path + 'popOgro.png')
msg_orc = pygame.image.load(path + 'popOrc.png')

msg_cotaMitril = pygame.image.load(path + 'msgCotaMitril.jpg')
msg_capacete = pygame.image.load(path + 'msgCapacete.jpg')
msg_broquel = pygame.image.load(path + 'msgBroquel.jpg')
msg_espada_lunar = pygame.image.load(path + 'msgEspadaLunar.jpg')
msg_manopla = pygame.image.load(path + 'msgManopla.jpg')
msg_botas = pygame.image.load(path + 'msgBotas.jpg')
msg_esfera = pygame.image.load(path + 'msgEsfera.jpg')
msg_tacape = pygame.image.load(path + 'msgTacape.jpg')
msg_moedas = pygame.image.load(path + 'msgMoedas.jpg')
msg_flexa = pygame.image.load(path + 'msgFlexa.jpg')
msg_cajado_mago = pygame.image.load(path + 'msgCajadoMago.jpg')
msg_espada_vorpal = pygame.image.load(path + 'msgEspadaVorpal.jpg')

files = [file for file in os.listdir(path) if file.startswith('titulo')]
msg_titulo_rei = [pygame.image.load(path + file) for file in sorted(files)]

caminho = r'assets\msg_tutorial\\'
files = os.listdir(caminho)
msg_tutorial = [pygame.image.load(caminho + file) for file in sorted(files)]


# -------------------- Carregando itens -------------------------
path = r'assets\itens\\'
files = os.listdir(path)
figura_itens = [pygame.image.load(path + item) for item in sorted(files)]

lado_figura = 30
posicao_item = (300, 150)

armadilhas = [
    Objeto((527, 290), 34, 38, figura_itens[0], msg_armadilha, audio_armadilha, 'armadilha'),
    Objeto((527, 290), 37, 40, figura_itens[1], msg_armadilha, audio_armadilha, 'armadilha'),
]

itens_labirinto_orc = [
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[8], msg_cotaMitril, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[9], msg_capacete, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[7], msg_broquel, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[2], msg_espada_lunar, audio_click, 'item'),
    ]

itens_labirinto_ogro = [
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[10], msg_manopla, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[11], msg_botas, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[6], msg_esfera, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[5], msg_tacape, audio_click, 'item'),
    ]


itens_labirinto_dragao = [
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[12], msg_moedas, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[13], msg_flexa, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[4], msg_cajado_mago, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[3], msg_espada_vorpal, audio_click, 'item'),
    ]

itens_labirinto_orc2 = [
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[8], msg_cotaMitril, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[9], msg_capacete, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[7], msg_broquel, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[2], msg_espada_lunar, audio_click, 'item'),
    ]

itens_labirinto_ogro2 = [
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[10], msg_manopla, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[11], msg_botas, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[6], msg_esfera, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[5], msg_tacape, audio_click, 'item'),
    ]


itens_labirinto_dragao2 = [
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[12], msg_moedas, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[13], msg_flexa, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[4], msg_cajado_mago, audio_click, 'item'),
        Objeto(posicao_item, lado_figura, lado_figura, figura_itens[3], msg_espada_vorpal, audio_click, 'item'),
    ]

itens1 = {
    'labirinto_orc': itens_labirinto_orc,
    'labirinto_ogro': itens_labirinto_ogro,
    'labirinto_dragao': itens_labirinto_dragao
}

itens2 = {
    'labirinto_orc': itens_labirinto_orc2,
    'labirinto_ogro': itens_labirinto_ogro2,
    'labirinto_dragao': itens_labirinto_dragao2
}
