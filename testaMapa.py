import os
import pygame
from jogador import Personagem

pygame.init()

DELAY = 80
MENU = True
FONT = 'PressStart2P-Regular'
FONT_SIZE = 17
DESLOCA_MAPA = 510
WIDTH = 700           # largura da janela
HEIGHT = 500          # altura da janela
LIM_SUPERIOR = 20
LIM_LATERAL = 500     # limite a direita
y_fundo = - DESLOCA_MAPA
x_fundo = 0
dir_correta = [('ESQUERDA', 'ESQUERDA', 'ESQUERDA'), ('DIREITA', 'DIREITA', 'DIREITA'),
               ('ESQUERDA', 'DIREITA', 'ESQUERDA'), ('DIREITA', 'ESQUERDA', 'DIREITA')]    # direcoes corretas de cada calabouço
dir_jogador = []                      # direcao que o jogador seguiu em cada sala
sala_atual = len(dir_jogador)         # em que sala o personagem está
bg = 0                                # background atual

pygame.display.set_caption("King")
janela = pygame.display.set_mode((WIDTH, HEIGHT))

pos_inicial = (LIM_LATERAL/2 - 30, 360)
p1 = Personagem(x = pos_inicial[0], y = pos_inicial[1], path = r'C:\Users\Eliane\Desktop\Temporario\jogoPy\Personagens\p1')


# x = LIM_LATERAL - 130


#inimigos
inimigo = Personagem(x = LIM_LATERAL/2 + 30, y = LIM_SUPERIOR + 40, path = r'C:\Users\Eliane\Desktop\Temporario\jogoPy\Personagens\orc')
# dragao = Personagem(x = LIM_LATERAL/2 - 30, y = LIM_SUPERIOR + 40, file = '', velocidade = 10)
# orc = Personagem(x = LIM_LATERAL/2 - 30, y = LIM_SUPERIOR + 40, file = '', velocidade = 10)

PATH_MAPA = 'mapas2'
fundo_placar = pygame.image.load(r'mapas\terra.png')

# variaveis de pontuação
pontos = 0
fonte_pontos = pygame.font.SysFont(FONT, FONT_SIZE, True, True)
fonte_dir = pygame.font.SysFont(FONT, FONT_SIZE - 4, True, True)

# carregando sprites do cenário com a porta esquerda aberta
mapas = []
caminho = PATH_MAPA + '\\'
files = os.listdir(caminho)
mapas = [pygame.image.load(caminho + file) for file in sorted(files)]

fundo = mapas[bg]


# Carregando menus
menu = pygame.image.load(r'menu\menu_principal.png')
jogar_hover = pygame.image.load(r'menu\jogar_hover.png')
personagem_hover = pygame.image.load(r'menu\personagem_hover.png')
sair_hover = pygame.image.load(r'menu\sair_hover.png')


def colidir(ax: float, ay: float, aComp: float, aAlt: float, bx: float, by: float, bComp: float, bAlt: float):
    if ay + aAlt <= by:
        return False
    elif ay >= by + bAlt:
        return False
    elif ax + aComp <= bx:
        return False
    elif ax >= bx + bComp:
        return False

    return True
    
        
# movimentacao do inimigo
def movimenta_inimigo():
    dif_y = abs(inimigo.y - p1.y) > 70
    dif_x = abs(inimigo.x - p1.x) > 20
    
    if inimigo.x <= p1.x and dif_x:    # RIGHT
        inimigo.movimenta('d')
    elif inimigo.x >= p1.x and dif_x:    # LEFT
        inimigo.movimenta('e')
    elif inimigo.y >= p1.y and dif_y:      # UP
        inimigo.movimenta('c')
    elif inimigo.y <= p1.y and dif_y:    # DOWN
        inimigo.movimenta('b')
    
        
# movimentacao do personagem
def movimenta_personagem(comandos):
    if comandos[pygame.K_UP]:
        p1.movimenta('c')
    elif comandos[pygame.K_DOWN]:
        p1.movimenta('b')
    elif comandos[pygame.K_RIGHT]:
        p1.movimenta('d')
    elif comandos[pygame.K_LEFT]:
        p1.movimenta('e')
        

# # movimentacao do personagem
# def movimenta_personagem(comandos):
#     if comandos[pygame.K_UP]:
#         if (p1.y >= LIM_SUPERIOR + 40) and (p1.x <= 163 and p1.x + 85 >= 325):
#             p1.movimenta('c')
#     elif comandos[pygame.K_DOWN]:
#         if (p1.y <= 299) and (p1.x >= 32 and p1.x + 85 >= 354):
#             p1.movimenta('b')
#     elif comandos[pygame.K_RIGHT]:
#         p1.movimenta('d')
#     elif comandos[pygame.K_LEFT]:
#         p1.movimenta('e')


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
        pontos += 3
        
        
        
troca_mapa = 0
def gerencia_mapa():
    global troca_mapa, dir_jogador, y_fundo, x_fundo, DESLOCA_MAPA, bg
    
    if escolheu_direita():
        dir_jogador.append('DIREITA')
        p1.x = 50
        
        if troca_mapa == 1:
            x_fundo = - DESLOCA_MAPA
            y_fundo = - DESLOCA_MAPA
            
        if troca_mapa == 2:
            bg += 1
            if dir_jogador[sala_atual - 1] == 'DIREITA':
                x_fundo = - DESLOCA_MAPA
                y_fundo = - DESLOCA_MAPA
            else:
                x_fundo = - DESLOCA_MAPA
                y_fundo = 0
                
    else:
        dir_jogador.append('ESQUERDA')
        p1.x = LIM_LATERAL - 130
        
        if troca_mapa == 1:
            y_fundo = 0
            x_fundo = 0
            
        if troca_mapa == 2:
            bg += 1
            if dir_jogador[sala_atual - 1] == 'DIREITA':
                x_fundo = 0
                y_fundo = - DESLOCA_MAPA
            else:
                x_fundo = 0
                y_fundo = 0
            
    if troca_mapa == 3:
        x_fundo = 0
        y_fundo = - DESLOCA_MAPA
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
    


# click button
def botao_clicado():
    global MENU
    x, y = pygame.mouse.get_pos()
    
    if (y >= 163 and y <= 205) and (x >= 261 and x <= 440):
        MENU = False
    elif (y >= 231 and y <= 273) and (x >= 261 and x <= 440):
        pass
#         escolhe_personagem()
        
    elif (y >= 298 and y <= 340) and (x >= 261 and x <= 440):
        pygame.quit()
        exit()



# menu principal
def menu_principal():
    global MENU, menu
    
    MENU = True
    x, y = pygame.mouse.get_pos()
    
    if (y >= 163 and y <= 205) and (x >= 261 and x <= 440):
        janela.blit(jogar_hover, (0, 0))
    elif (y >= 231 and y <= 273) and (x >= 261 and x <= 440):
        janela.blit(personagem_hover, (0, 0))
    elif (y >= 298 and y <= 340) and (x >= 261 and x <= 440):
        janela.blit(sair_hover, (0, 0))
    else:
        janela.blit(menu, (0, 0))
    
    

def jogar():
    global MENU, menu
    
    direcoes = 'ESQUERDA          DIREITA'
    rodando = True
    
    while rodando:
        pygame.time.delay(DELAY)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                botao_clicado()
        
        if not MENU:
            label = f'Pontos: {pontos}'
            label_pontos = fonte_pontos.render(label, True, (255, 255, 255))
            
            p1.x_anterior = p1.x
            p1.y_anterior = p1.y
            comandos = pygame.key.get_pressed()
            movimenta_personagem(comandos)
            
            if p1.y <= LIM_SUPERIOR:
                atualiza_cenario()
            
            fundo = mapas[bg]
            
            # cenário
            janela.blit(fundo, (x_fundo, y_fundo))
            janela.blit(fundo_placar, (LIM_LATERAL + 8, 0))
            
            # personagem
            if not colidir(p1.y, p1.x, 35, 48, inimigo.y, inimigo.x, 32, 57):
                janela.blit(p1.sprite_atual, (p1.x, p1.y))
            
            # inimigo
            if sala_atual == 1:
                if p1.y <= 400:
                    movimenta_inimigo()
                janela.blit(inimigo.sprite_atual, (inimigo.x, inimigo.y))
            
            # labels
            if p1.y <= LIM_SUPERIOR + 90:
                label_direcoes = fonte_dir.render(direcoes, True, (255, 0, 0))
                janela.blit(label_direcoes, (LIM_LATERAL - 430, LIM_SUPERIOR + 35))
            
            janela.blit(label_pontos, (LIM_LATERAL + 30, LIM_SUPERIOR + 30))
        else:
            menu_principal()
        
        
        
        
        
        
        
        
        
        print('personagem:', p1.x, p1.y)
        print('inimigo:', inimigo.x, inimigo.y)
        pygame.display.update()
        
        
       
        
        
if __name__ == '__main__':
    jogar()
    
pygame.quit()
