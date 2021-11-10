class Orcamento(object):
    
    def __init__(self, valor : float):
        self.__valor = valor
        
    @property
    def valor(self):
        return self.__valor
