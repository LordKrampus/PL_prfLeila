from orcamento import Orcamento
from imposto import *

class Calculador_de_imposto:
    
    def realizar_calculo(self, orcamento : Orcamento, imposto : object):
        return imposto.calcular(orcamento)
