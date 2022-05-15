import os
import pygame
from constantes import *
from pygame import mixer
from load_assets import *
from jogador import Personagem

troca_mapa = 0
anima_label_pontos = 0

pygame.init()
mixer.init()

y_fundo = - DESLOCA_MAPA_VERTICAL
x_fundo = 0
dir_correta = [('ESQUERDA', 'ESQUERDA', 'ESQUERDA'), ('DIREITA', 'DIREITA', 'DIREITA'),
               ('ESQUERDA', 'DIREITA', 'ESQUERDA'), ('DIREITA', 'ESQUERDA', 'DIREITA')]    # direcoes corretas de cada calabouço
dir_jogador = []                      # direcao que o jogador seguiu em cada sala
sala_atual = len(dir_jogador)         # em que sala o personagem está
bg_atual = 0                          # background atual
bg_anterior = -1
fluxo_jogo = 0
fundo = mapas[bg_atual]
volta_inicio = True

# criando a janela
pygame.display.set_caption("Lost Kingdom")
janela = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)


# personagem
pos_inicial = (LIM_LATERAL/2 - 10, 360)
p1 = Personagem(x = pos_inicial[0], y = pos_inicial[1], altura = 48, largura = 35, path = r'assets\Personagens\p1')


#inimigos
orc = Personagem(x = LIM_LATERAL/2 + 30, y = LIM_SUPERIOR, largura = 28, altura = 57, path = r'assets\Personagens\orc')
# dragao = Personagem(x = LIM_LATERAL/2 - 30, y = LIM_SUPERIOR + 40, file = '', velocidade = 10)
# ogro = Personagem(x = LIM_LATERAL/2 - 30, y = LIM_SUPERIOR + 40, file = '', velocidade = 10)

inimigo = orc

path_sounds = 'assets\\'
# Carregando sons do jogo
audio_click = pygame.mixer.Sound(path_sounds + r"sounds\Click.mp3")
audio_inicioJogo = pygame.mixer.Sound(path_sounds + r"sounds\inicioJogo.wav")
audio_decrease = pygame.mixer.Sound(path_sounds + r"sounds\Decrease.mp3")
audio_armadilha = pygame.mixer.Sound(path_sounds + r"sounds\Armadilha.wav")
audio_passarinho = pygame.mixer.Sound(path_sounds + r"sounds\passarinho.wav")
audio_addItem = pygame.mixer.Sound(path_sounds + r"sounds\inicioJogo.wav")
audio_pontua = pygame.mixer.Sound(path_sounds + r"sounds\pontua.wav")


# variaveis de pontuação
pontos = 0
fonte_pontos = pygame.font.SysFont(FONT, FONT_SIZE, True, True)
fonte_dir = pygame.font.SysFont(FONT, FONT_SIZE - 4, True, True)


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
        
        if sala_atual == 24:
            if p1.y < 18:
                p1.movimenta('b')
        else:
            if (p1.x + w > 108 and p1.x < 500) and p1.y < LIM_SUPERIOR:
                p1.movimenta('b')
            
    elif comandos[pygame.K_DOWN]:
        p1.movimenta('b')
        
        if sala_atual == 24:
            if p1.y + h >= 460:
                p1.movimenta('c')
        else:
            if p1.y + h >= 472:
                p1.movimenta('c')
                
            elif troca_mapa == 0:
                if (p1.x <= 194 or p1.x + w >= 413) and p1.y + h >= 290:
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
        
        if not sala_atual == 24:
            if troca_mapa == 0:
                if p1.x + w >= 412 and p1.y + h >= 291:
                    p1.movimenta('e')
            else:
                if dir_jogador[-1] == 'DIREITA' and p1.y + h >= 290 and p1.x + w > 108:
                    p1.movimenta('e')
            
    elif comandos[pygame.K_LEFT]:
        p1.movimenta('e')
        
        if p1.x + w <= 45:
            p1.movimenta('d')
        
        if not sala_atual == 24:
            if troca_mapa == 0:
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
        

# manipula o cenario do jogo
def gerencia_mapa():
    global troca_mapa, dir_jogador, y_fundo, x_fundo, volta_inicio
    global DESLOCA_MAPA, bg_atual, fluxo_jogo, bg_anterior
    global sala_atual, DESLOCA_MAPA_VERTICAL
    
    if escolheu_direita():
        dir_jogador.append('DIREITA')
        p1.x = 40
        
        if troca_mapa == 1:
            x_fundo = - DESLOCA_MAPA
            y_fundo = - DESLOCA_MAPA_VERTICAL
            
        if troca_mapa == 2:
            bg_atual += 1
            
            if dir_jogador[sala_atual - 1] == 'DIREITA': # verifica qual opcao a pessoa tinha escolhido na sala anterior
                x_fundo = - DESLOCA_MAPA
                y_fundo = - DESLOCA_MAPA_VERTICAL
            else:
                x_fundo = - DESLOCA_MAPA
                y_fundo = 0
    else:
        dir_jogador.append('ESQUERDA')
        p1.x = LIM_LATERAL - 70
        
        if troca_mapa == 1:
            x_fundo = 0
            y_fundo = 0
            
        if troca_mapa == 2:
            bg_atual += 1
            
            if dir_jogador[sala_atual - 1] == 'DIREITA': # verifica qual opcao a pessoa tinha escolhido na sala anterior
                x_fundo = 0
                y_fundo = - DESLOCA_MAPA_VERTICAL
            else:
                x_fundo = 0
                y_fundo = 0
                
    if troca_mapa == 3:
        x_fundo = 0
        y_fundo = - DESLOCA_MAPA_VERTICAL
        troca_mapa = 0
        bg_anterior = bg_atual
        bg_atual += 1
        fluxo_jogo += 1
        p1.x = pos_inicial[0]
    
    if fluxo_jogo == 9 and volta_inicio:
        volta_inicio = False
        fluxo_jogo = 2             # coloquei uma unidade a menos do que queria porque no if de baixo ele incrementa
        bg_atual = 0
        sala_atual = 0
        
    if fundo == sala_rei:
        x_fundo = 0
        y_fundo = - DESLOCA_MAPA_VERTICAL
        
        
        
# muda para a próxima sala
def atualiza_cenario():
    global sala_atual, dir_jogador, y_fundo, x_fundo, troca_mapa
    
    pontua()
    troca_mapa += 1
    gerencia_mapa()
    sala_atual = len(dir_jogador)
    p1.y = pos_inicial[1]


# 
# 
# def animacao_pontos_ganhos():
#     pass
# 


path_personagem = 'p1'

# click button
def botao_clicado_menu():
    global MENU, p1, path_personagem, pos_inicial
    
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
                        path = 'assets\Personagens\\' + path_personagem)


# menu principal
def menu_principal():
    global MENU, menu_personagens, path_personagem
    
    MENU = True
    
    if path_personagem == 'p1':
        janela.blit(menu_personagens[0], (0, 0))
    elif path_personagem == 'p2':
        janela.blit(menu_personagens[2], (0, 0))
    elif path_personagem == 'p3':
        janela.blit(menu_personagens[1], (0, 0))
    else:
        janela.blit(menu_personagens[3], (0, 0))
    
    
def jogar():
    global MENU, menu, fluxo_jogo, bg_anterior
    
    direcoes = 'ESQUERDA                    DIREITA'
    rodando = True
    cor_labels = (255, 255, 255)
    posicao_msg = (100, 100)
    
    while rodando:
        pygame.time.delay(DELAY)
        
        if fluxo_jogo % 2 == 0 and fluxo_jogo:
            bg_anterior = bg_atual
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_END:
                    rodando = False
                    
                elif event.key == pygame.K_RETURN and bg_anterior != bg_atual:
                    fluxo_jogo += 1
                    
            elif MENU:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    botao_clicado_menu()
        
        if fluxo_jogo >= 1:
            if not MENU:
                label = f'Pontos:{pontos}'
                label_pontos = fonte_pontos.render(label, True, cor_labels)
                label_pontua = fonte_pontos.render(f'+{pontos}', True, cor_labels)
                
                p1.x_anterior = p1.x
                p1.y_anterior = p1.y
                comandos = pygame.key.get_pressed()
                movimenta_personagem(comandos)
                
                if p1.y <= LIM_SUPERIOR and fundo != sala_rei:
                    atualiza_cenario()
                
                fundo = mapas[bg_atual]
                
                # cenário
                janela.blit(fundo, (x_fundo, y_fundo))
                janela.blit(fundo_placar, (LIM_LATERAL + 10, 0))
                janela.blit(cobre_sobra_mapa, (0, HEIGHT))

                
                # personagem
#                 if not p1.colidir(inimigo):
#                     janela.blit(p1.sprite_atual, (p1.x, p1.y))
                
                janela.blit(p1.sprite_atual, (p1.x, p1.y))
                
                # inimigo
#                 if sala_atual == 1:
#                     if p1.y <= 400:
#                         movimenta_inimigo()
#                     janela.blit(inimigo.sprite_atual, (inimigo.x, inimigo.y))
                
                # labels
                if p1.y <= LIM_SUPERIOR + 90 and sala_atual != 24:
                    label_direcoes = fonte_dir.render(direcoes, True, (255, 255, 255))
                    janela.blit(label_direcoes, (LIM_LATERAL - 540, LIM_SUPERIOR + 35))
                
                janela.blit(label_pontos, (LIM_LATERAL + 30, LIM_SUPERIOR + 30))
    #             animacao_pontos_ganhos(janela)
    #             janela.blit(label_pontua, (LIM_LATERAL + 30, HEIGHT/2 + anima_label_pontos)
    
                if fluxo_jogo % 2 != 0:
                    if fluxo_jogo == 1:
                        janela.blit(msg_rei, posicao_msg)
                    elif fluxo_jogo == 3:
                        janela.blit(msg_orc, posicao_msg)
                    elif fluxo_jogo == 5:
                        janela.blit(msg_ogro, posicao_msg)
                    elif fluxo_jogo == 7:
                        janela.blit(msg_dragao, posicao_msg)
                    elif fluxo_jogo == 9:
                        janela.blit(msg_form_final, posicao_msg)

            else:
                menu_principal()
            
            
            
        else:
            janela.blit(abertura, (0,0))
        
        
        
        
        
        
        
        
        print('personagem:', p1.x, p1.y)
        print('inimigo:', inimigo.x, inimigo.y)
        pygame.display.update()
        
        
if __name__ == '__main__':
#     os.system('python formulario.py')
    jogar()
    
    
pygame.quit()