dia = int(input("quantos dias alugou o carro?"))
km = float(input("quantos km rodados? "))
aluguel = dia * 60 +  km*0.15
print("o  alugou por {} e a quilometragem foi {} o total a pagar e de {}".format(dia,km,aluguel))