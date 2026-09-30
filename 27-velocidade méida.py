#Declare
numero_voltas: int = 0
extensao_pista: float = 0.0
tempo_total: float = 0.0

#Inicio
def calcular(numero_voltas,extensao_pista,tempo_total):
    distancia = numero_voltas * extensao_pista
    distancia_km = distancia / 1000
    tempo_horas = tempo_total / 60
    velocidade = distancia_km / tempo_horas
    return velocidade
def main():
    numero_voltas = int(input("Digite o número de voltas: "))
    extensao_pista = float(input("Digite a extensão da pista (em metros): "))
    tempo_total = float(input("Digite o tempo total (em minutos): "))
    velocidade = calcular(numero_voltas,extensao_pista,tempo_total)
    print("Velocidade média:", velocidade, "km/h")
main()
#Fim