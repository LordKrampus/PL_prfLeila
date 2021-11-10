from orcamento import Orcamento
from calculador_de_imposto import Calculador_de_imposto
from imposto import ISS, ICMS

# objetos
orcamento = Orcamento(100)
calculador_de_imposto = Calculador_de_imposto()

# calculo e debug
valor_imposto = calculador_de_imposto.realizar_calculo(orcamento, ISS())
print(valor_imposto)
valor_imposto = calculador_de_imposto.realizar_calculo(orcamento, ICMS())
print(valor_imposto)