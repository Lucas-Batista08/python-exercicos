class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Email: {self.email}")


pessoa = Pessoa("João", 24, "joao@gmail.com")
pessoa.exibir_informacoes()


class Funcionario(Pessoa):
    def __init__(self, nome, idade, email, matricula):
       
        super().__init__(nome, idade, email)
       
        self.matricula = matricula

    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Email: {self.email}")
        print(f"Matrícula: {self.matricula}")

funcionario = Funcionario("Lucas", 30, "lucasfuncionario@gmail.com", "F12345")
funcionario.exibir_informacoes()