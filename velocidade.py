# Classe base Veiculo
class Veiculo:
    def __init__(self, velocidade_maxima):
        self._velocidade_maxima = velocidade_maxima  # Atributo protegido
    
    def get_velocidade_maxima(self):
        return self._velocidade_maxima  # Método público para acessar a velocidade
    
    def acelerar(self, valor):
        # Adiciona à velocidade, mas não pode ultrapassar 200
        self._velocidade_maxima = min(self._velocidade_maxima + valor, 200)

# Subclasse Carro herdando de Veiculo
class Carro(Veiculo):
    def acelerar(self, valor):
        # Sobrescreve para garantir que não ultrapasse 180
        self._velocidade_maxima = min(self._velocidade_maxima + valor, 180)
    
    def frear(self, valor):
        # Reduz a velocidade, mas não pode ser menor que 0
        self._velocidade_maxima = max(self._velocidade_maxima - valor, 0)

# Testando a classe Carro
carro = Carro(60)  # Iniciando com velocidade máxima de 60

# Acelerando o carro
carro.acelerar(100)  # Deve acelerar até 160
velocidade_atual = carro.get_velocidade_maxima()

# Tentando acelerar além de 180
carro.acelerar(50)  # Deve limitar a 180
velocidade_final = carro.get_velocidade_maxima()

# Freando o carro
carro.frear(70)  # Deve reduzir a 110
velocidade_apos_freio = carro.get_velocidade_maxima()

# Tentando frear mais do que a velocidade atual
carro.frear(150)  # Deve reduzir a 0, pois não pode ser menor que 0
velocidade_minima = carro.get_velocidade_maxima()

velocidade_atual, velocidade_final, velocidade_apos_freio, velocidade_minima
