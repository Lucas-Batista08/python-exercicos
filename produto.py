class Produto:
    def __init__(self, *args, **kwargs):
        if len(args) == 1:  
            self.nome = args[0]
            self.preco = 0  
        elif len(args) == 2:  
            self.nome = args[0]
            self.preco = args[1]
        else:  
            self.nome = kwargs.get('nome', 'Kitkat')
            self.preco = kwargs.get('preco', 0)

    def exibir_informacoes(self):
        print(f"Nome do Produto: {self.nome}")
        print(f"Preço: R$ {self.preco}")
        print('-------------------------')




produto1 = Produto('KitKat', 2,50)


produto2 = Produto('Chocolate')


produto1.exibir_informacoes()
produto2.exibir_informacoes()
