from orcamento import Orcamento
from descontos import Desconto_cinco_itens, Desconto_mais_quinhentos_reais, Desconto_nulo

class Calculador_desconto(object):
    
    def calcular(self, orcamento : Orcamento):
        desconto = Desconto_cinco_itens(
            Desconto_mais_quinhentos_reais(Desconto_nulo())
            ).calcular(orcamento)
        
        return desconto
        
if __name__ == '__main__':
    from item import Item
    
    def print_desconto(orcamento: Orcamento):
         print('desconto: $%.02f' %(Calculador_desconto().calcular(orcamento)))
         
         
    itens = [Item('Item A', 100),
             Item('Item B', 200),
             Item('Item C', 300)]
    
    orcamento = Orcamento()
    
    for item in itens:
        orcamento.adicionar_item(item)

    print_desconto(orcamento)
        
    