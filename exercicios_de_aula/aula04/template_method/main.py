from item import Item
from orcamento import Orcamento
from calculador_de_imposto import Calculador_de_imposto
from imposto import ISS, ICMS, ICPP, IKCV


itens = [Item('Item A', 100),
         Item('Item B', 200),
         Item('Item C', 300)]

orcamento = Orcamento()

for item in itens:
    orcamento.adicionar_item(item)
        
calculador_de_imposto = Calculador_de_imposto()

# calculo e debug
valor_imposto = calculador_de_imposto.realizar_calculo(orcamento, ISS())
print(valor_imposto)
valor_imposto = calculador_de_imposto.realizar_calculo(orcamento, ICMS())
print(valor_imposto)
valor_imposto = calculador_de_imposto.realizar_calculo(orcamento, ICPP())
print(valor_imposto)
valor_imposto = calculador_de_imposto.realizar_calculo(orcamento, IKCV())
print(valor_imposto)