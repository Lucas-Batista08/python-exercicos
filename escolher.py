def exibir_menu():
    print("Escolha uma das opções abaixo:")
    print("1 - Dom Casmurro")
    print("2 - O Senhor dos Anéis")
    print("3 - 1984")
    print("4 - sair do programa")

def escolher_livros():
    while True:
        exibir_menu()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            print("Você escolheu: Dom Casmurro")
            
            print('Dom Casmurro', 'Machado de Assis', 1899)
        elif escolha == "2":
            print("Você escolheu: Exibir uma mensagem")

            print('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
            
        elif escolha == "3":
           print("1984", 'George Orwell',1949)
              
        elif escolha == "4":
              break
        else:
            print("Opção inválida, tente novamente.")
            
    

escolher_livros()