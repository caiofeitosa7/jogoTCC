import os
import pygame
from constantes import *
from pygame import mixer
from jogador import Personagem

troca_mapa = 0
anima_label_pontos = 0

pygame.init()
mixer.init()

y_fundo = - DESLOCA_MAPA + ESPACO_ENTRE_MAPAS
x_fundo = 0
dir_correta = [('ESQUERDA', 'ESQUERDA', 'ESQUERDA'), ('DIREITA', 'DIREITA', 'DIREITA'),
               ('ESQUERDA', 'DIREITA', 'ESQUERDA'), ('DIREITA', 'ESQUERDA', 'DIREITA')]    # direcoes corretas de cada calabouço
dir_jogador = []                      # direcao que o jogador seguiu em cada sala
sala_atual = len(dir_jogador)         # em que sala o personagem está
bg = 0                                # background atual

# criando a janela
pygame.display.set_caption("Lost Kingdom")
janela = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

PATH_MAPA = 'mapas3'
fundo_placar = pygame.image.load(r'mapas\terra.png')
cobre_sobra_mapa = pygame.image.load(r'mapas\terra2.png')


pos_inicial = (LIM_LATERAL/2 - 15, 360)
p1 = Personagem(x = pos_inicial[0], y = pos_inicial[1], altura = 48, largura = 35, path = r'Personagens\p1')


#inimigos
orc = Personagem(x = LIM_LATERAL/2 + 30, y = LIM_SUPERIOR, largura = 28, altura = 57, path = r'C:\Users\Eliane\Desktop\Temporario\jogoPy\Personagens\orc')
# dragao = Personagem(x = LIM_LATERAL/2 - 30, y = LIM_SUPERIOR + 40, file = '', velocidade = 10)
# ogro = Personagem(x = LIM_LATERAL/2 - 30, y = LIM_SUPERIOR + 40, file = '', velocidade = 10)

inimigo = orc

# variaveis de pontuação
pontos = 0
fonte_pontos = pygame.font.SysFont(FONT, FONT_SIZE, True, True)
fonte_dir = pygame.font.SysFont(FONT, FONT_SIZE - 4, True, True)

# carregando sprites do cenário
mapas = []
caminho = PATH_MAPA + '\\'
files = os.listdir(caminho)
mapas = [pygame.image.load(caminho + file) for file in sorted(files)]

fundo = mapas[bg]


# Carregando imagens do menu de personagens
menu_personagens = []
caminho = r'menu\menuPersonagens' + '\\'
files = os.listdir(caminho)
menu_personagens = [pygame.image.load(caminho + file) for file in sorted(files)]

# menu = pygame.image.load(r'menu\menu_principal.png')
# jogar_hover = pygame.image.load(r'menu\jogar_hover.png')
# personagem_hover = pygame.image.load(r'menu\personagem_hover.png')
# sair_hover = pygame.image.load(r'menu\sair_hover.png')

# Carregando sons do jogo
audio_click = pygame.mixer.Sound(r"sounds\Click.mp3")
audio_inicioJogo = pygame.mixer.Sound(r"sounds\inicioJogo.wav")
audio_decrease = pygame.mixer.Sound(r"sounds\Decrease.mp3")
audio_armadilha = pygame.mixer.Sound(r"sounds\Armadilha.wav")
audio_passarinho = pygame.mixer.Sound(r"sounds\passarinho.wav")
audio_addItem = pygame.mixer.Sound(r"sounds\inicioJogo.wav")
audio_pontua = pygame.mixer.Sound(r"sounds\pontua.wav")


# posiciona inimigo no mapa jogavel
def posiciona_inimigo():
    for i in range(8):
        inimigo.movimenta('b')
    
    
# movimentacao do inimigo
def movimenta_inimigo():
    dif_y = abs(inimigo.y - p1.y) > 50
    dif_x = abs(inimigo.x - p1.x) > 20
    
    if inimigo.x <= p1.x and dif_x:    # RIGHT
        inimigo.movimenta('d')
    elif inimigo.x >= p1.x and dif_x:  # LEFT
        inimigo.movimenta('e')
    elif inimigo.y >= p1.y and dif_y:  # UP
        inimigo.movimenta('c')
    elif inimigo.y <= p1.y and dif_y:  # DOWN
        inimigo.movimenta('b')
    
    
# movimentacao do personagem
def movimenta_personagem(comandos):
    global troca_mapa
    h = p1.altura
    w = p1.largura
    
    if comandos[pygame.K_UP]:
        p1.movimenta('c')
        
        if (p1.x + w > 108 and p1.x < 500) and p1.y < LIM_SUPERIOR:
            p1.movimenta('b')
        
    elif comandos[pygame.K_DOWN]:
        p1.movimenta('b')
        
        if p1.y + h >= 472:
            p1.movimenta('c')
            
        elif troca_mapa == 0:
            if (p1.x <= 196 or p1.x + w >= 413) and p1.y + h >= 290:
                p1.movimenta('c')
        else:
            if dir_jogador[-1] == 'ESQUERDA' and p1.y + h >= 290 and p1.x <= 500:
                p1.movimenta('c')
            
            elif dir_jogador[-1] == 'DIREITA' and p1.y + h >= 290 and p1.x >= 108:
                p1.movimenta('c')
            
    elif comandos[pygame.K_RIGHT]:
        p1.movimenta('d')
        
        if p1.x + w >= 596:
            p1.movimenta('e')
            
        elif troca_mapa == 0:
            if p1.x + w >= 412 and p1.y + h >= 291:
                p1.movimenta('e')
        else:
            if dir_jogador[-1] == 'DIREITA' and p1.y + h >= 290 and p1.x + w > 108:
                p1.movimenta('e')
            
    elif comandos[pygame.K_LEFT]:
        p1.movimenta('e')
        
        if p1.x + w <= 45:
            p1.movimenta('d')
            
        elif troca_mapa == 0:
            if p1.x + w <= 225 and p1.y + h >= 291:
                p1.movimenta('d')
        else:
            if dir_jogador[-1] == 'ESQUERDA' and p1.y + h >= 290 and p1.x < 500:
                p1.movimenta('d')
        

# função que verifica se o personagem foi pela direita
def escolheu_direita():
    if p1.x > LIM_LATERAL / 2 :
        return True

    return False


# função de pontuação
def pontua():
    global sala_atual, pontos
    ganha_ponto = False
    
    if sala_atual <= 2:                           # primeiro calabouço
        if not escolheu_direita():
            ganha_ponto = True
            
    if sala_atual > 2 and sala_atual <= 5:        # segundo calabouço
        if escolheu_direita():
            ganha_ponto = True
            
#      ('e', 'd', 'e'), ('d', 'e', 'd')]
    if sala_atual == 6 or sala_atual == 8 or sala_atual == 10:
        if not escolheu_direita():
            ganha_ponto = True
    
    if sala_atual == 7 or sala_atual == 9 or sala_atual == 11:
        if escolheu_direita():
            ganha_ponto = True
    
    if ganha_ponto:
        audio_pontua.play()
        pontos += 3
        
        
def gerencia_mapa():
    global troca_mapa, dir_jogador, y_fundo, x_fundo, DESLOCA_MAPA, bg
    
    deslocamento = DESLOCA_MAPA - ESPACO_ENTRE_MAPAS
    
    if escolheu_direita():
        dir_jogador.append('DIREITA')
        p1.x = 40
        
        if troca_mapa == 1:
            x_fundo = - DESLOCA_MAPA
            y_fundo = - deslocamento
            
        if troca_mapa == 2:
            bg += 1
            if dir_jogador[sala_atual - 1] == 'DIREITA': # verifica qual opcao a pessoa tinha escolhido na sala anterior
                x_fundo = - DESLOCA_MAPA
                y_fundo = - deslocamento
            else:
                x_fundo = - DESLOCA_MAPA
                y_fundo = - ESPACO_ENTRE_MAPAS       
    else:
        dir_jogador.append('ESQUERDA')
        p1.x = LIM_LATERAL - 70
        
        if troca_mapa == 1:
            x_fundo = 0
            y_fundo = - ESPACO_ENTRE_MAPAS
            
        if troca_mapa == 2:
            bg += 1
            if dir_jogador[sala_atual - 1] == 'DIREITA': # verifica qual opcao a pessoa tinha escolhido na sala anterior
                x_fundo = 0
                y_fundo = - deslocamento
            else:
                x_fundo = 0
                y_fundo = - ESPACO_ENTRE_MAPAS
            
    if troca_mapa == 3:
        x_fundo = 0
        y_fundo = - deslocamento
        troca_mapa = 0
        bg += 1
        p1.x = pos_inicial[0]
        
    
# muda para a próxima sala
def atualiza_cenario():
    global sala_atual, dir_jogador, y_fundo, x_fundo, troca_mapa
    
    pontua()
    troca_mapa += 1
    gerencia_mapa()
    sala_atual = len(dir_jogador)
    p1.y = pos_inicial[1]




def animacao_pontos_ganhos():
    pass



path_personagem = 'p1'

# click button
def botao_clicado_menu():
    global MENU, menu_personagens, p1, path_personagem, pos_inicial
    
    x, y = pygame.mouse.get_pos()
    pos_click_horizontal = y >= 200 and y <= 259
    
    if pos_click_horizontal:
        if x >= 203 and x <= 262:
            audio_click.play()
            path_personagem = 'p1'
            
        elif x >= 281 and x <= 341:
            audio_click.play()
            path_personagem = 'p3'
            
        elif x >= 360 and x <= 421:
            audio_click.play()
            path_personagem = 'p2'
            
        elif x >= 439 and x <= 500:
            audio_click.play()
            path_personagem = 'p4'
            
    if (y >= 293 and y <= 324) and (x >= 297 and x <= 407):
        MENU = False
        audio_inicioJogo.play()
        p1 = Personagem(x = pos_inicial[0], y = pos_inicial[1], altura = 48, largura = 35, \
                        path = 'Personagens\\' + path_personagem)


# menu principal
def menu_principal():
    global MENU, menu_personagens, path_personagem
    
    MENU = True
    x, y = pygame.mouse.get_pos()
    
    if path_personagem == 'p1':
        janela.blit(menu_personagens[0], (0, 0))
    elif path_personagem == 'p2':
        janela.blit(menu_personagens[2], (0, 0))
    elif path_personagem == 'p3':
        janela.blit(menu_personagens[1], (0, 0))
    else:
        janela.blit(menu_personagens[3], (0, 0))
    
    
def jogar():
    global MENU, menu
    
    direcoes = 'ESQUERDA                    DIREITA'
    rodando = True
    
    while rodando:
        pygame.time.delay(DELAY)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_END:
                    rodando = False
                    
            if MENU:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    botao_clicado_menu()
        
        if not MENU:
            label = f'Pontos: {pontos}'
            label_pontos = fonte_pontos.render(label, True, (255, 255, 255))
            label_pontua = fonte_pontos.render(f'+{pontos}', True, (255, 255, 255))
            
            p1.x_anterior = p1.x
            p1.y_anterior = p1.y
            comandos = pygame.key.get_pressed()
            movimenta_personagem(comandos)
            
            if p1.y <= LIM_SUPERIOR:
                atualiza_cenario()
            
            fundo = mapas[bg]
            
            # cenário
            janela.blit(fundo, (x_fundo, y_fundo))
            janela.blit(fundo_placar, (LIM_LATERAL + 10, 0))
            janela.blit(cobre_sobra_mapa, (0, HEIGHT))

            
            # personagem
            if not p1.colidir(inimigo):
                janela.blit(p1.sprite_atual, (p1.x, p1.y))
            
            # inimigo
            if sala_atual == 1:
                if p1.y <= 400:
                    movimenta_inimigo()
                janela.blit(inimigo.sprite_atual, (inimigo.x, inimigo.y))
            
            # labels
            if p1.y <= LIM_SUPERIOR + 90:
                label_direcoes = fonte_dir.render(direcoes, True, (255, 255, 255))
                janela.blit(label_direcoes, (LIM_LATERAL - 540, LIM_SUPERIOR + 35))
            
            janela.blit(label_pontos, (LIM_LATERAL + 30, LIM_SUPERIOR + 30))
#             animacao_pontos_ganhos(janela)
#             janela.blit(label_pontua, (LIM_LATERAL + 30, HEIGHT/2 + anima_label_pontos)
        else:
            menu_principal()
        
        
        
        
        
        
        
        
        
        print('personagem:', p1.x, p1.y)
        print('inimigo:', inimigo.x, inimigo.y)
        pygame.display.update()
        
        
       
if __name__ == '__main__':
    jogar()
    
pygame.quit()