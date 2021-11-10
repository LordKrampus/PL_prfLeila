from orcamento import Orcamento

class Desconto_cinco_itens(object):
    
    def __init__(self, proximo):
        self.__proximo = proximo
    
    def calcular(self, orcamento: Orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor*0.1
        
        return self.__proximo.calcular(orcamento)
    
class Desconto_mais_quinhentos_reais(object):
    
    def __init__(self, proximo):
         self.__proximo = proximo
    
    def calcular(self, orcamento: Orcamento):
        if orcamento.valor > 500:
            return orcamento.valor*0.07

        return self.__proximo.calcular(orcamento)
    
class Desconto_nulo(object):
    
    def __init__(self):
        pass

    def calcular(self, orcamento: Orcamento):
        return 0.0
