
class Objeto:
    def __init__(self, x: int, y: int, largura: int, altura: int, path: str):
        self.__x = x
        self.__y = y
        self.__altura = altura
        self.__largura = largura
        self.__path = path
        
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
    def largura(self):
        return self.__largura
    
    @property
    def altura(self):
        return self.__altura
    