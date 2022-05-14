import os
import pygame
from constantes import *

fundo_placar = pygame.image.load(r'mapas\pn4.png')
cobre_sobra_mapa = pygame.image.load(r'mapas\terra2.png')


# carregando sprites do cenário
mapas = []
caminho = PATH_MAPA + '\\'
files = os.listdir(caminho)
mapas = [pygame.image.load(caminho + file) for file in sorted(files)]

# Carregando imagens do menu de personagens
menu_personagens = []
caminho = r'menu\menuPersonagens' + '\\'
files = os.listdir(caminho)
menu_personagens = [pygame.image.load(caminho + file) for file in sorted(files)]

abertura = pygame.image.load(r'menu\abertura.png')


path_msg = 'mensagens'
# Carregando mensagens
msg_rei = pygame.image.load(path_msg + r'\msgRei.png')
msg_atacado = pygame.image.load(path_msg + r'\msgAtacado.png')
msg_form_final = pygame.image.load(path_msg + r'\msgFormFinal.png')
msg_nao_encontrou = pygame.image.load(path_msg + r'\msgNaoEncontrou.png')
msg_dragao = pygame.image.load(path_msg + r'\popDragao.png')
msg_ogro = pygame.image.load(path_msg + r'\popOgro.png')
msg_orc = pygame.image.load(path_msg + r'\popOrc.png')




# menu = pygame.image.load(r'menu\menu_principal.png')
# jogar_hover = pygame.image.load(r'menu\jogar_hover.png')
# personagem_hover = pygame.image.load(r'menu\personagem_hover.png')
# sair_hover = pygame.image.load(r'menu\sair_hover.png')