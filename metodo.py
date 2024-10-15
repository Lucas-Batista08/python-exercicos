# Classe base Conta com encapsulamento e atributos privados e protegidos
class Conta:
    def __init__(self, saldo_inicial=0, limite=1000):
        self.__saldo = saldo_inicial  # Atributo privado para o saldo
        self._limite = limite  # Atributo protegido para o limite
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor  # Adiciona ao saldo
        else:
            print("Depósito inválido.")
    
    def sacar(self, valor):
        # Só permite saque se o valor for menor ou igual ao saldo e ao limite
        if 0 < valor <= self.__saldo + self._limite:
            self.__saldo -= valor  # Subtrai do saldo
        else:
            print("Saque inválido. Saldo ou limite insuficiente.")
    
    def ver_saldo(self):
        return self.__saldo  # Retorna o saldo atual

# Subclasse ContaEspecial que herda de Conta
class ContaEspecial(Conta):
    def __init__(self, saldo_inicial=0, limite=2000):
        super().__init__(saldo_inicial, limite)  # Usa o construtor da classe base
    
    def sacar(self, valor):
        # Permite saques até o dobro do limite original
        if 0 < valor <= self.ver_saldo() + (2 * self._limite):
            super().sacar(valor)  # Usa o método da classe base para sacar
        else:
            print("Saque inválido. Limite excedido.")

# Testando a classe ContaEspecial
conta_especial = ContaEspecial(500, 1500)  # Conta com saldo inicial de 500 e limite de 1500

# Realizando um depósito
conta_especial.depositar(1000)  # Deposita 1000
saldo_apos_deposito = conta_especial.ver_saldo()

# Tentando sacar dentro do limite (2000)
conta_especial.sacar(2000)  # Deve permitir o saque
saldo_apos_saque = conta_especial.ver_saldo()

# Tentando sacar acima do limite (até o dobro do limite original, ou seja, 3000)
conta_especial.sacar(3000)  # Deve permitir o saque
saldo_apos_saque_maior = conta_especial.ver_saldo()

# Tentando sacar mais do que o dobro do limite
conta_especial.sacar(4000)  # Saque inválido, deve exibir uma mensagem de erro
saldo_final = conta_especial.ver_saldo()

saldo_apos_deposito, saldo_apos_saque, saldo_apos_saque_maior, saldo_final
