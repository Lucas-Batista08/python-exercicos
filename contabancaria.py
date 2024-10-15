class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso.")
        else:
            print("Saque inválido. Verifique o saldo ou o valor inserido.")

    def exibir_informacoes(self):
        print(f"Número da Conta: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo}")
        print('----------------------------')


def realizar_operacoes(conta):
    while True:
        print("\nEscolha uma operação:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Exibir informações da conta")
        print("4 - Sair")
        opcao = input("Digite a opção desejada (1/2/3/4): ")

        if opcao == "1":
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor_deposito)
        elif opcao == "2":
            valor_saque = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor_saque)
        elif opcao == "3":
            conta.exibir_informacoes()
        elif opcao == "4":
            print("Encerrando operações...")
            break
        else:
            print("Opção inválida. Tente novamente.")


conta1 = ContaBancaria('123456', 'Lucas Silva', 1000)


conta2 = conta1


realizar_operacoes(conta1)

print("\nInformações finais da conta1:")
conta1.exibir_informacoes()

print("Informações finais da conta2:")
conta2.exibir_informacoes()