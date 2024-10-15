class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_informacoes(self):
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano de Publicação: {self.ano_publicacao}')
        print('-----------------------------')

# Criando três instâncias da classe Livro
livro1 = Livro('Dom Casmurro', 'Machado de Assis', 1899)
livro2 = Livro('1984', 'George Orwell', 1949)
livro3 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)

# Exibindo as informações de cada livro
livro1.exibir_informacoes()
livro2.exibir_informacoes()
livro3.exibir_informacoes()