class Item(object):
    
    def __init__(self, nome: str, valor: float):
        self.__nome = nome;
        self.__valor = valor;
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def valor(self):
        return self.__valor
    
if __name__ == '__main__':
    
    def print_item(item : Item):
         print('nome: %s\tvalor: $%.2f' %(item.nome, item.valor))
    
    
    item_a = Item('Item A', 100.0)
    item_b = Item('Item B', 200.0)
    
    print_item(item_a)
    print_item(item_b)
