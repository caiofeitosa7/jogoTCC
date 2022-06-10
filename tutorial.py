import sys
import time
import itens
import pygame
import random
from jogador import Personagem
from load_assets import *
from constantes import *

troca_mapa = 0
tempo_fim_jogo = 0
tempo_inicio_jogo = 0
anima_label_pontos = 0

MENU = not MENU
x_fundo = 0
y_fundo = - DESLOCA_MAPA_VERTICAL
# dir_correta = [('ESQUERDA', 'ESQUERDA', 'ESQUERDA'), ('DIREITA', 'DIREITA', 'DIREITA'),
#                ('ESQUERDA', 'DIREITA', 'ESQUERDA'), ('DIREITA', 'ESQUERDA', 'DIREITA')]    # direcoes corretas de cada calabouço

dir_correta = ['ESQUERDA', 'ESQUERDA', 'ESQUERDA',
               'DIREITA', 'DIREITA', 'DIREITA',
               'ESQUERDA', 'DIREITA', 'ESQUERDA',
               'DIREITA', 'ESQUERDA', 'DIREITA',
               'ESQUERDA', 'ESQUERDA', 'ESQUERDA',
               'DIREITA', 'DIREITA', 'DIREITA',
               'ESQUERDA', 'DIREITA', 'ESQUERDA',
               'DIREITA', 'ESQUERDA', 'DIREITA']
dir_jogador = []                      # direcao que o jogador seguiu em cada sala
sala_atual = len(dir_jogador)         # em que sala o personagem está
bg_atual = 0                          # background atual
bg_anterior = -1
fluxo_jogo = 0
fundo = mapas[bg_atual]
volta_inicio = True
entrou_sala_item = False
entrou_sala_inimigo = False
entrou_sala_armadilha = False
item_da_vez = itens['labirinto_orc'][0]
ultimo_objeto_colidido = itens['labirinto_orc'][0]


# ------ variaveis do inventario ------

itemy = 188
itemx = LIM_LATERAL + 31

itens_encontrados = []
pos_item_inventario = [itemx, itemy]


# ------------ personagem -------------

pos_inicial = (LIM_LATERAL/2 - 10, 400)
p1 = Personagem(x = pos_inicial[0], y = pos_inicial[1], altura = 48, largura = 35, path = r'assets\Personagens\p1')


# ------------- inimigos --------------

inimigo = Personagem(x = -100, y = LIM_SUPERIOR, largura = 28, altura = 57, path = r'assets\Personagens\orc')


def encontrou_objeto(objeto):
    global pos_item_inventario, itemx, itemy, ultimo_objeto_colidido
    
    if objeto.descricao == 'item':
        objeto.x = pos_item_inventario[0]
        objeto.y = pos_item_inventario[1]
        
        itens_encontrados.append(objeto)
        
        if len(itens_encontrados) % 4 == 0:
            pos_item_inventario[0] = itemx
            pos_item_inventario[1] += 42
        else:
            pos_item_inventario[0] += 42
    else:
        objeto.x = -100
        
    ultimo_objeto_colidido = objeto
    objeto.audio.play()


def verifica_entrou_sala_item():
    global item_da_vez, entrou_sala_item
    
    labirinto = ''
    entrou_sala_item = False
    
    if (sala_atual == 1 and dir_jogador[-1] == 'ESQUERDA') or \
       (sala_atual == 5 and dir_jogador[-1] == 'DIREITA'):
        labirinto = 'labirinto_orc'
    elif sala_atual == 7 and dir_jogador[-1] == 'ESQUERDA':
        labirinto = 'labirinto_ogro'
    elif sala_atual == 11 and dir_jogador[-1] == 'DIREITA':
        labirinto = 'labirinto_dragao'
    
    if labirinto:
        item_da_vez = itens[labirinto][random.randint(0,len(itens[labirinto])-1)]
        itens[labirinto].remove(item_da_vez)
        entrou_sala_item = True
    

def verifica_entrou_sala_armadilha():
    global item_da_vez, entrou_sala_armadilha
    
    entrou_sala_armadilha = False
    
    if (sala_atual == 5 and dir_jogador[-1] == 'ESQUERDA') or sala_atual == 8:
        item_da_vez = armadilhas[random.randint(0,len(armadilhas)-1)]
        armadilhas.remove(item_da_vez)
        entrou_sala_armadilha = True
            
        if dir_jogador[-1] == 'ESQUERDA':
            item_da_vez.x, item_da_vez.y = (527, 290)
        else:
            item_da_vez.x, item_da_vez.y = (30, 290)
    

def verifica_entrou_sala_inimigo():
    global entrou_sala_inimigo, inimigo
    
    entrou_sala_inimigo = False
    
    if sala_atual == 4 and dir_jogador[-1] == 'ESQUERDA':
        entrou_sala_inimigo = True
        inimigo = Personagem(x = LIM_LATERAL/2 + 30,
                             y = LIM_SUPERIOR,
                             largura = 28,
                             altura = 57,
                             path = r'assets\Personagens\orc')
        
    if sala_atual == 8 and dir_jogador[-1] == 'ESQUERDA':
        entrou_sala_inimigo = True
        inimigo = Personagem(x = LIM_LATERAL/2 - 30,
                             y = LIM_SUPERIOR + 40,
                             largura = 32,
                             altura = 65,
                             path = r'assets\Personagens\ogro')
    
    if sala_atual == 11:
        entrou_sala_inimigo = True
        inimigo = Personagem(x = LIM_LATERAL/2 - 30,
                             y = LIM_SUPERIOR + 40,
                             largura = 32,
                             altura = 65,
                             path = r'assets\Personagens\dragao')
    
    
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
    h = p1.altura
    w = p1.largura

    if comandos[pygame.K_UP]:
        p1.movimenta('c')

        if sala_atual == 1:
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
    global pontos, anima_label_pontos
    ganha_ponto = False
    
    if sala_atual <= 2:                           # primeiro calabouço
        if not escolheu_direita():
            if sala_atual == 0 \
               or sala_atual == 1 and dir_jogador[-1] == 'ESQUERDA' \
               or sala_atual == 2 and dir_jogador[-1] == 'ESQUERDA' and dir_jogador[-2] == 'ESQUERDA':
                ganha_ponto = True
            
    if sala_atual >= 3 and sala_atual <= 5:        # segundo calabouço
        if escolheu_direita():
            if sala_atual == 3 \
               or sala_atual == 4 and dir_jogador[-1] == 'DIREITA' \
               or sala_atual == 5 and dir_jogador[-1] == 'DIREITA' and dir_jogador[-2] == 'DIREITA':
                ganha_ponto = True
            
#      ('ESQUERDA', 'DIREITA', 'ESQUERDA')
    if sala_atual >= 6 and sala_atual <= 8:        # terceiro calabouco        
        if not escolheu_direita():
            if sala_atual == 6 \
               or sala_atual == 8 and dir_jogador[-1] == 'DIREITA' and dir_jogador[-2] == 'ESQUERDA':
                ganha_ponto = True
                
        elif sala_atual == 7:
            ganha_ponto = True
            
#      ('DIREITA', 'ESQUERDA', 'DIREITA')
    if sala_atual >= 9 and sala_atual <= 11:
        if escolheu_direita():
            if sala_atual == 9 \
               or sala_atual == 11 and dir_jogador[-1] == 'ESQUERDA' and dir_jogador[-2] == 'DIREITA':
                ganha_ponto = True
                
        elif sala_atual == 10:
            ganha_ponto = True
    
    if ganha_ponto:
        anima_label_pontos = 1
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
    
    if fundo == sala_rei:
        x_fundo = 0
        y_fundo = - DESLOCA_MAPA_VERTICAL
    
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
        fluxo_jogo = 2
        bg_atual = 0
        sala_atual = -1
    
    
# muda para a próxima sala
def atualiza_cenario():
    global sala_atual, troca_mapa
    
    pontua()
    troca_mapa += 1
    gerencia_mapa()
    sala_atual += 1
    p1.y = pos_inicial[1]
    verifica_entrou_sala_item()
    verifica_entrou_sala_inimigo()
    verifica_entrou_sala_armadilha()
    
    
def jogar():
    global MENU, fluxo_jogo, bg_anterior, anima_label_pontos
    global ultimo_objeto_colidido, entrou_sala_inimigo, pontos
    
    direcoes = 'ESQUERDA' + ' '*20 + 'DIREITA'
    cor_labels = (255, 255, 255)
    posicao_msg = (100, 100)
    chegou_em_cima = False
    rodando = True
    
    while rodando:
        pygame.time.delay(DELAY)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_END:
                    rodando = False
                    
                elif event.key == pygame.K_RETURN:
                    if bg_anterior != bg_atual:
                        fluxo_jogo += 1
                        audio_click.play()
                        
                        if fluxo_jogo == 7:
                            rodando = False
                        
                    elif p1.colidiu_objeto:
                        p1.colidiu_objeto = False
                
            elif MENU:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    botao_clicado_menu()
                
        if fluxo_jogo >= 1:
            if not MENU:               
                p1.x_anterior = p1.x
                p1.y_anterior = p1.y
                movimenta_personagem(pygame.key.get_pressed())
                
                if p1.y <= LIM_SUPERIOR and fundo != sala_rei and sala_atual <= 1:
                    atualiza_cenario()
                
                fundo = mapas[bg_atual]
                
                
                # --------- cenário ---------
                
                janela.blit(fundo, (x_fundo, y_fundo))
                janela.blit(fundo_placar, (LIM_LATERAL + 10, 0))
                janela.blit(cobre_sobra_mapa, (0, HEIGHT))
                
                
                # -------- personagem -------
                
                janela.blit(p1.sprite_atual, (p1.x, p1.y))
                
                
                # ---------- itens ----------
                
                if entrou_sala_item or entrou_sala_armadilha:
                    if not p1.colidir(item_da_vez):
                        janela.blit(item_da_vez.figura, (item_da_vez.x, item_da_vez.y))
                    else:
                        encontrou_objeto(item_da_vez)
                    
                for item in itens_encontrados:
                    janela.blit(item.figura, (item.x, item.y))
                    
                    
                # --------- inimigo ---------
                
                if entrou_sala_inimigo:
                    if not p1.colidir(inimigo):
                        janela.blit(inimigo.sprite_atual, (inimigo.x, inimigo.y))
                        movimenta_inimigo()
                    else:
                        ultimo_objeto_colidido = inimigo
                        entrou_sala_inimigo = False
                        audio_decrease.play()
                        inimigo.x = -100
                        pontos -= 3


                if p1.colidiu_objeto:
                    if type(ultimo_objeto_colidido) == Objeto:
                        janela.blit(ultimo_objeto_colidido.mensagem, posicao_msg)
                    else:
                        janela.blit(msg_atacado, posicao_msg)
                
                
                # ------------------- labels ------------------
                
                label = f'Pontos:{pontos}'
                label_pontos = fonte_pontos.render(label, True, cor_labels)

                janela.blit(label_pontos, (LIM_LATERAL + 30, LIM_SUPERIOR + 30))
                
                if p1.y <= LIM_SUPERIOR + 90 and sala_atual != 24:
                    label_direcoes = fonte_dir.render(direcoes, True, (255, 255, 255))
                    janela.blit(label_direcoes, (LIM_LATERAL - 540, LIM_SUPERIOR + 35))
                
                
                # --------- animacao de ganhar ponto ----------
                
                label_pontua = fonte_pontos.render(f'+ 3', True, cor_labels)
                
                if anima_label_pontos != 0 and anima_label_pontos >= -60:
                    janela.blit(label_pontua, (LIM_LATERAL//2, HEIGHT//2 - 40 + anima_label_pontos))
                    anima_label_pontos -= 7
                
                if anima_label_pontos <= -60:
                    anima_label_pontos = 0
                
                
                # --------------- fluxo de jogo ----------------
                
                if fluxo_jogo == 1:
                    janela.blit(msg_tutorial[fluxo_jogo-1], posicao_msg)
                elif fluxo_jogo == 2:
                    janela.blit(msg_tutorial[fluxo_jogo-1], posicao_msg)
                elif fluxo_jogo == 3:
                    janela.blit(msg_tutorial[fluxo_jogo-1], (100, 260))
                    
                    if p1.y > LIM_SUPERIOR + 60 and not chegou_em_cima:
                        p1.movimenta('c')
                    else:
                        chegou_em_cima = True                        
                    
                elif fluxo_jogo == 4:
                    janela.blit(msg_tutorial[fluxo_jogo-1], (130, 180))
                elif fluxo_jogo == 5:
                    janela.blit(msg_tutorial[fluxo_jogo-1], (130, 50))
                elif fluxo_jogo == 6:
                    janela.blit(msg_tutorial[fluxo_jogo-1], posicao_msg)
            else:
                menu_principal()
        else:
            janela.blit(abertura, (0,0))
        
        pygame.display.update()
          

if __name__ == '__main__':
    # criando a janela
    pygame.init()
    pygame.display.set_caption("Lost Kingdom")
    janela = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    
    # variaveis de pontuação
    pontos = 0
    fonte_pontos = pygame.font.SysFont(FONT, FONT_SIZE, True, True)
    fonte_dir = pygame.font.SysFont(FONT, FONT_SIZE - 4, True, True)
    
    jogar()

pygame.quit()
    