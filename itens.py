class Objeto:
    def __init__(self, x: int, y: int, largura: int, altura: int, figura: str, msg, audio, desc):
        self._x = x
        self._y = y
        self._altura = altura
        self._largura = largura
        self._figura = figura
        self._mensagem = msg
        self._audio = audio
        self._descricao = desc
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x
      
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        self._y = y
    
    @property
    def largura(self):
        return self._largura
    
    @property
    def altura(self):
        return self._altura
    
    @property
    def mensagem(self):
        return self._mensagem
    
    @property
    def figura(self):
        return self._figura
    
    @property
    def audio(self):
        return self._audio
    
    @property
    def descricao(self):
        return self._descricao
    