from orcamento import Orcamento

class ISS(object):
    
    def calcular(self, orcamento : Orcamento):
        return orcamento.valor * 0.1
    
class ICMS(object):
    
    def calcular(self, orcamento : Orcamento):
        return orcamento.valor * 0.06
