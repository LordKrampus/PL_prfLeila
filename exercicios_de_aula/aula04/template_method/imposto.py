from orcamento import Orcamento
from abc import ABCMeta, abstractmethod

class Template_imposto_condicional(object):
    
    __metaclass__ = ABCMeta
    
    def calcular(self, orcamento: Orcamento):
        if self.validar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        return self.minima_taxacao(orcamento)
    
    @abstractmethod
    def validar_maxima_taxacao(self, orcamento: Orcamento):
        pass
    
    @abstractmethod
    def maxima_taxacao(self, orcamento: Orcamento):
        pass
    
    @abstractmethod
    def minima_taxacao(self, orcamento: Orcamento):
        pass


class ISS(object):
    
    def calcular(self, orcamento : Orcamento):
        return orcamento.valor * 0.1
    
    
class ICMS(object):
    
    def calcular(self, orcamento : Orcamento):
        return orcamento.valor * 0.06


class ICPP(Template_imposto_condicional):
    
    def validar_maxima_taxacao(self, orcamento: Orcamento):
        return orcamento.valor > 500
    
    def maxima_taxacao(self, orcamento: Orcamento):
        return orcamento.valor*0.7
        
    def minima_taxacao(self, orcamento: Orcamento):
        return orcamento.valor*0.5
    
    
class IKCV(Template_imposto_condicional):
    
    def validar_maxima_taxacao(self, orcamento: Orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_cem_reais(orcamento)
            
    
    def maxima_taxacao(self, orcamento: Orcamento):
        return orcamento.valor*0.1
        
    def minima_taxacao(self, orcamento: Orcamento):
        return orcamento.valor*0.06
    
    def __tem_item_maior_que_cem_reais(self, orcamento: Orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100: return True
        return False