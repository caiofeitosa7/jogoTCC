import os
import pygame
from jogador import Personagem

pygame.init()

pos_inicial = (385, 380)
p1 = Personagem(x = pos_inicial[0], y = pos_inicial[1], file = '')

# px = 385           # posição x do personagem
# py = 380           # posição y do personagem
width = 697           # largura da janela
heigth = 490           # altura da janela
sala_atual = 0         # em que sala o personagem está
lim_superior = -20
lim_lateral = 403 + 87   # limite a direita
inicio_fundo = -553
dir_correta = [('e', 'e', 'e'), ('d', 'd', 'd'), ('e', 'd', 'e'), ('d', 'e', 'd')]    # direcoes corretas de cada calabouço

path_mapa = r'Jogo TCC\mapas'
fundo_placar = pygame.image.load(r'Jogo TCC\mapas\terra.png')



calabouco2 = pygame.image.load(r'Jogo TCC\mapas\mapinha3.png')



# variaveis de pontuação
pontos = 0
font_size = 17
fonte = pygame.font.SysFont('PressStart2P-Regular', font_size, True, True)

# carregando sprites do cenário principal
m_principal = []
caminho = path_mapa + '\\Principal\\'
files = os.listdir(caminho)
m_principal = [pygame.image.load(caminho + file) for file in files]


# carregando sprites do cenário com a porta direita aberta
m_direita = []
caminho = path_mapa + '\\AbertoDir\\'
files = os.listdir(caminho)
m_direita = [pygame.image.load(caminho + file) for file in files]


# carregando sprites do cenário com a porta esquerda aberta
m_esquerda = []
caminho = path_mapa + '\\AbertoEsq\\'
files = os.listdir(caminho)
m_esquerda = [pygame.image.load(caminho + file) for file in files]


fundo = m_principal[sala_atual]

# ________________________________________________________________________________ #


# colisão
def colide():
    if p1.x + 85 >= lim_lateral or p1.x <= 5:
        return True
    if p1.y + 90 >= heigth or p1.y <= lim_superior - 10:
        return True
    
    return False



# movimentação do personagem
def movimenta_personagem(comandos):
    
    if comandos[pygame.K_UP]:
        #if not colide():
        p1.y -= p1.velocidade
         
        p1.indices['cima'] += 1
        p1.atualiza_frame('c')
        
    elif comandos[pygame.K_DOWN]:
        #if not colide():
        p1.y += p1.velocidade
        
        p1.indices['baixo'] += 1
        p1.atualiza_frame('b')
        
    elif comandos[pygame.K_RIGHT]:
        #if not colide():
        p1.x += p1.velocidade
        
        p1.indices['direita'] += 1
        p1.atualiza_frame('d')
        
        
    elif comandos[pygame.K_LEFT]:
        #if not colide():
        p1.x -= p1.velocidade
        
        p1.indices['esquerda'] += 1
        p1.atualiza_frame('e')       



# função que verifica se o personagem foi pela direita
def escolheu_direita():
    if p1.x > lim_lateral / 2 :
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
        


# muda para a próxima sala
def atualiza_cenario():
    global inicio_fundo, sala_atual
    
    pontua()
    inicio_fundo += 490
    sala_atual += 1


                                                                        # TODO
def label_direcao():
    global font_size
    
    if py <= lim_superior + 110:
        d = 'DIREITA'
        e = 'ESQUERDA'
        label_pontos = fonte.render(label, True, (255, 255, 255))


# # abre a porta
# def abre_porta():
#     global m_direita, m_esquerda, fundo, sala_atual
#     
#     if escolheu_direita():
#         fundo = m_direita[sala_atual]
#     else:
#         fundo = m_esquerda[sala_atual]
#         
# 
# 
# # fecha a porta
# def fecha_porta():
#     global m_principal, sala_atual, fundo
#     fundo = m_principal[sala_atual]
        



janela = pygame.display.set_mode((width, heigth))
janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)
    
    label = f'Pontos: {pontos}'
    label_pontos = fonte.render(label, True, (255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    
    p1.x_anterior = p1.x
    p1.y_anterior = p1.y
    movimenta_personagem(pygame.key.get_pressed())
    
    if p1.y <= lim_superior:
        p1.y = 420
        atualiza_cenario()
    
    
    
    
    
    
    label_direcao()
    
    
    
#     if py <= lim_superior + 80:
#         abre_porta()
#     else:
#         fecha_porta()
        
    
    # cenário
    janela.blit(fundo, (0, inicio_fundo))
    janela.blit(calabouco2, (0, inicio_fundo - 1260))
    janela.blit(fundo_placar, (lim_lateral + 8, 0))
    
    # personagem
    janela.blit(p1.sprite_atual, (p1.x, p1.y))
    print(p1.x, p1.y)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    janela.blit(label_pontos, (lim_lateral + 30, lim_superior + 30))
    pygame.display.update()        
pygame.quit()
