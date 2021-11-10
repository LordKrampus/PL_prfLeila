from item import Item
from orcamento import Orcamento
from calculador_desconto import Calculador_desconto

     
itens = [Item('Item A', 100),
         Item('Item B', 200),
         Item('Item C', 300)]

orcamento = Orcamento()

for item in itens:
    orcamento.adicionar_item(item)
    
calculador = Calculador_desconto()

print('desconto: $%.02f'%(calculador.calcular(orcamento)))

orcamento.adicionar_item(Item('Item D', 100))
orcamento.adicionar_item(Item('Item E', 100))
orcamento.adicionar_item(Item('Item F', 100))

print('desconto: $%.02f'%(calculador.calcular(orcamento)))
