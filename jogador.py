import os
import pygame

class Personagem:
    sprites_cima = []
    sprites_baixo = []
    sprites_direita = []
    sprites_esquerda = []
    
    indices = {'cima': 0, 'baixo': 0, 'direita': 0, 'esquerda': 0}
    
    def __init__(self, x: int, y: int, largura: int, altura: int, path = 'assets\Personagens\p1'):
        self.__x = x
        self.__y = y
        self.x_anterior = x
        self.y_anterior = y
        self.__altura = altura
        self.__largura = largura
        self.__velocidade = 20
        self.__path = path
        self.frame_frente = True
        
        #carregando sprites do personagem andando pra cima
        caminho = self.__path + '\\Cima\\'
        files = sorted(os.listdir(caminho))
        self.sprites_cima = [pygame.image.load(caminho + file) for file in files]

        # carregando sprites do personagem andando pra baixo
        caminho = self.__path + '\\Baixo\\'
        files = sorted(os.listdir(caminho))
        self.sprites_baixo = [pygame.image.load(caminho + file) for file in files]

        # carregando sprites do personagem andando pra direita
        caminho = self.__path + '\\Direita\\'
        files = sorted(os.listdir(caminho))
        self.sprites_direita = [pygame.image.load(caminho + file) for file in files]

        # carregando sprites do personagem andando pra esquerda
        caminho = self.__path + '\\Esquerda\\'
        files = sorted(os.listdir(caminho))
        self.sprites_esquerda = [pygame.image.load(caminho + file) for file in files]
        
        self.__sprite_atual = self.sprites_cima[0]


    def __verifica_sentido_frame(self, direcao: str):
        if self.indices.get(direcao) >= 2:
            self.frame_frente = False
                
        if self.indices.get(direcao) <= 0:
            self.frame_frente = True
            
        if self.indices.get(direcao) < 0 or self.indices.get(direcao) > 2:
            self.indices[direcao] = 2
        
    
    def atualiza_frame(self, direcao: str):
        if self.__y != self.y_anterior:              # vertical
            if direcao == 'c':
                self.__verifica_sentido_frame('cima')
                self.__sprite_atual = self.sprites_cima[self.indices.get('cima')]
            elif direcao == 'b':
                self.__verifica_sentido_frame('baixo')
                self.__sprite_atual = self.sprites_baixo[self.indices.get('baixo')]
            
        if self.__x != self.x_anterior:              # horizontal
            if direcao == 'd':
                self.__verifica_sentido_frame('direita')
                self.__sprite_atual = self.sprites_direita[self.indices.get('direita')]
            elif direcao == 'e':
                self.__verifica_sentido_frame('esquerda')
                self.__sprite_atual = self.sprites_esquerda[self.indices.get('esquerda')]
        
    
    def __verifica_sentido_movimenta(self, direcao: str):
        if self.frame_frente:
            self.indices[direcao] += 1
        else:
            self.indices[direcao] -= 1
    
    
    def movimenta(self, direcao: str):
        if direcao == 'c':
            self.y -= self.velocidade
            self.__verifica_sentido_movimenta('cima')
        elif direcao == 'b':
            self.y += self.velocidade
            self.__verifica_sentido_movimenta('baixo')
        elif direcao == 'd':
            self.x += self.velocidade
            self.__verifica_sentido_movimenta('direita')
        elif direcao == 'e':
            self.x -= self.velocidade
            self.__verifica_sentido_movimenta('esquerda')
            
        self.atualiza_frame(direcao)
    

    def colidir(self, obj):
        if self.__y + self.__altura <= obj.y:
            return False
        elif self.__y >= obj.y + obj.altura:
            return False
        elif self.__x + self.__largura <= obj.x:
            return False
        elif self.__x >= obj.x + obj.largura:
            return False

        return True


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
    def largura(self):
        return self.__largura
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def velocidade(self):
        return self.__velocidade
    