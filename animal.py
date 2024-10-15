class Animal:
    def __init__(self, nome):
        self.nome = nome  
    
    def som(self):
        print("Som genérico")  


class Cachorro(Animal):
    def som(self):
        print("Au Au")  


class Gato(Animal):
    def som(self):
        print("Miau")  


cachorro = Cachorro("Preto")
gato = Gato("Apolo")


cachorro.som()  
gato.som()      