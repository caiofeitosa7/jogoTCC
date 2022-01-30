import os
import pygame

pygame.init()

px = 385           # posição x do personagem
py = 380           # posição y do personagem
width = 697           # largura da janela
heigth = 490           # altura da janela
sala_atual = 0         # em que sala o personagem está
lim_superior = -20
lim_lateral = 403 + 87   # limite a direita
inicio_fundo = -553
dir_correta = [('e', 'e', 'e'), ('d', 'd', 'd'), ('e', 'd', 'e'), ('d', 'e', 'd')]    # direcoes corretas de cada calabouço

path_personagem = r'C:\Users\Eliane\Desktop\Jogo TCC\Sprites Personagem'
path_mapa = r'C:\Users\Eliane\Desktop\Jogo TCC\mapas'
fundo_placar = pygame.image.load(r'C:\Users\Eliane\Desktop\Jogo TCC\mapas\terra.png')





calabouco2 = pygame.image.load(r'C:\Users\Eliane\Desktop\Jogo TCC\mapas\mapinha3.png')





# variaveis de pontuação
pontos = 0
fonte = pygame.font.SysFont('blockbit', 20, True, True)     # 3parametro = negrito; 4parametro = italico


# variaveis de movimentação
velocidade = 9                                # velocidade de movimentação do personagem
sprite_cima = 0
sprite_baixo = 0
sprite_direita = 0
sprite_esquerda = 0
px_anterior = px
py_anterior = py


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


# carregando sprites do personagem andando pra cima
p_cima = []
caminho = path_personagem + '\\Cima\\'
files = os.listdir(caminho)
p_cima = [pygame.image.load(caminho + file) for file in files]

# carregando sprites do personagem andando pra baixo
p_baixo = []
caminho = path_personagem + '\\Baixo\\'
files = os.listdir(caminho)
p_baixo = [pygame.image.load(caminho + file) for file in files]

# carregando sprites do personagem andando pra direita
p_direita = []
caminho = path_personagem + '\\Direita\\'
files = os.listdir(caminho)
p_direita = [pygame.image.load(caminho + file) for file in files]

# carregando sprites do personagem andando pra esquerda
p_esquerda = []
caminho = path_personagem + '\\Esquerda\\'
files = os.listdir(caminho)
p_esquerda = [pygame.image.load(caminho + file) for file in files]


personagem = p_cima[0]

# ________________________________________________________________________________ #


# colisão
def colide():
    if px + 85 >= lim_lateral or px <= 5:
        return True
    if py + 90 >= heigth or py <= lim_superior - 10:
        return True
    
    return False



# movimentação do personagem
def movimenta(comandos):
    global px, py, velocidade, sprite_cima, sprite_baixo, sprite_direita, sprite_esquerda
    
    if comandos[pygame.K_UP]:
        #if not colide():
        py -= velocidade
            
        sprite_cima += 1
        atualiza_personagem('c')
        
    elif comandos[pygame.K_DOWN]:
        #if not colide():
        py += velocidade
            
        sprite_baixo += 1
        atualiza_personagem('b')
        
    elif comandos[pygame.K_RIGHT]:
        #if not colide():
        px += velocidade
            
        sprite_direita += 1
        atualiza_personagem('d')
        
    elif comandos[pygame.K_LEFT]:
        #if not colide():
        px -= velocidade
            
        sprite_esquerda += 1
        atualiza_personagem('e')
    


# função que verifica se o personagem foi pela direita
def escolheu_direita():
    if px > lim_lateral / 2 :
        return True

    return False



# função de pontuação
def pontua():
    global sala_atual, pontos
    
    if sala_atual <= 2:                           # primeiro calabouço
        if not escolheu_direita():
            pontos += 1
            
    if sala_atual > 2 and sala_atual <= 5:        # segundo calabouço
        if escolheu_direita():
            pontos += 1
            
#      ('e', 'd', 'e'), ('d', 'e', 'd')]
    if sala_atual == 6 or sala_atual == 8 or sala_atual == 10:
        if not escolheu_direita():
            pontos += 1
    
    if sala_atual == 7 or sala_atual == 9 or sala_atual == 11:
        if escolheu_direita():
            pontos += 1
    


# muda para a próxima sala
def atualiza_cenario():
    global inicio_fundo, sala_atual
    
    pontua()
    inicio_fundo += 490
    sala_atual += 1



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
        
        

# atualiza os frames do personagem
def atualiza_personagem(direcao):
    global py, py_anterior, personagem
    global p_baixo, p_direita, p_esquerda, p_cima
    global sprite_cima, sprite_baixo, sprite_direita, sprite_esquerda
    
    if py != py_anterior:         # vertical
        if sprite_cima == 9:
            sprite_cima = 0
        
        if sprite_baixo == 9:
            sprite_baixo = 0
        
        if direcao == 'c':
            personagem = p_cima[sprite_cima]
        else:
            personagem = p_baixo[sprite_baixo]
        
    if px != px_anterior:         # horizontal
        if sprite_direita == 9:
            sprite_direita = 0
        
        if sprite_esquerda == 9:
            sprite_esquerda = 0
        
        if direcao == 'd':
            personagem = p_direita[sprite_direita]
        else:
            personagem = p_esquerda[sprite_esquerda]
        
        
        
        
        


janela = pygame.display.set_mode((width, heigth))
janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)
    
    label = f'Pontos: {pontos}'
    label_pontos = fonte.render(label, True, (255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    
    px_anterior = px
    py_anterior = py
    movimenta(pygame.key.get_pressed())
    
    
    if py <= lim_superior:
        py = 420
        atualiza_cenario()
        
#     if py <= lim_superior + 80:
#         abre_porta()
#     else:
#         fecha_porta()
        
    
    # cenário
    janela.blit(fundo, (0, inicio_fundo))
    janela.blit(calabouco2, (0, inicio_fundo - 1260))
    janela.blit(fundo_placar, (lim_lateral + 8, 0))
    
    # personagem
    janela.blit(personagem, (px, py))
    print(px, py)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    janela.blit(label_pontos, (lim_lateral + 30, lim_superior + 30))
    pygame.display.update()        
pygame.quit()
