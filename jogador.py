import os
import pygame

class Personagem:
    path = r'Jogo TCC\Sprites Personagem'
    
    # variaveis de sprites
    sprites_cima = []
    sprites_baixo = []
    sprites_direita = []
    sprites_esquerda = []
    
    # variaveis de movimentação
    __velocidade = 9
    indices = {'cima': 0, 'baixo': 0, 'direita': 0, 'esquerda': 0}
    
    def __init__(self, x: int, y: int, file: str):
        self.__x = x
        self.__y = y
        self.x_anterior = x
        self.y_anterior = y
        self.__file_sprites = file
        
        #carregando sprites do personagem andando pra cima
        caminho = self.path + self.__file_sprites + '\\Cima\\'
        files = os.listdir(caminho)
        self.sprites_cima = [pygame.image.load(caminho + file) for file in files]

        # carregando sprites do personagem andando pra baixo
        caminho = self.path + self.__file_sprites + '\\Baixo\\'
        files = os.listdir(caminho)
        self.sprites_baixo = [pygame.image.load(caminho + file) for file in files]

        # carregando sprites do personagem andando pra direita
        caminho = self.path + self.__file_sprites + '\\Direita\\'
        files = os.listdir(caminho)
        self.sprites_direita = [pygame.image.load(caminho + file) for file in files]

        # carregando sprites do personagem andando pra esquerda
        caminho = self.path + self.__file_sprites + '\\Esquerda\\'
        files = os.listdir(caminho)
        self.sprites_esquerda = [pygame.image.load(caminho + file) for file in files]
        
        self.__sprite_atual = self.sprites_cima[0]



    def atualiza_frame(self, direcao: str):
        if self.__y != self.y_anterior:              # vertical
            if self.indices.get('cima') == 9:
                self.indices['cima'] = 0
            
            if self.indices.get('baixo') == 9:
                self.indices['baixo'] = 0
            
            if direcao == 'c':
                self.__sprite_atual = self.sprites_cima[self.indices.get('cima')]
            else:
                self.__sprite_atual = self.sprites_baixo[self.indices.get('baixo')]
            
        if self.__x != self.x_anterior:              # horizontal
            if self.indices.get('direita') == 9:
                self.indices['direita'] = 0
            
            if self.indices.get('esquerda') == 9:
                self.indices['esquerda'] = 0
            
            if direcao == 'd':
                self.__sprite_atual = self.sprites_direita[self.indices.get('direita')]
            else:
                self.__sprite_atual = self.sprites_esquerda[self.indices.get('esquerda')]
    
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x
        
    @property
    def y(self):
        return self.__y
        
    @y.setter
    def y(self, y):
        self.__y = y
    
    @property
    def sprite_atual(self):
        return self.__sprite_atual
        
    @sprite_atual.setter
    def sprite_atual(self, sprite_atual):
        self.__sprite_atual = sprite_atual
       
    @property
    def velocidade(self):
        return self.__velocidade
    