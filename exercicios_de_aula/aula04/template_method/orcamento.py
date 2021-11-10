from item import Item

class Orcamento(object):
    
    def __init__ (self):
        self.__itens = []
        
    @property        
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total = total + item.valor
        return total
    
    def obter_itens(self):
        return tuple(self.__itens)
    
    @property
    def total_itens(self):
        return len(self.__itens)
    
    def adicionar_item(self, item: Item):
        self.__itens.append(item)


if __name__ == '__main__':
    
    def print_item(item : Item):
         print('nome: %s\tvalor: $%.2f' %(item.nome, item.valor))
         
         
    itens = [Item('Item A', 100),
             Item('Item B', 200),
             Item('Item C', 300)]
    
    orcamento = Orcamento()
    
    for item in itens:
        orcamento.adicionar_item(item)
        
    for item in orcamento.obter_itens():
        print_item(item)
        
    print(orcamento.valor)
    print(orcamento.total_itens)
        
    
    