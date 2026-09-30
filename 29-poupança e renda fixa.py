#Declarar
valor: float = 0.0
investimento: float = 0.0

#Inicio
def calcular(valor,tipo):
    if tipo == 1:
        return valor * 1.03
    elif tipo == 2:
        return valor * 1.05
    else:
        return 0.0
        #Fim-se
def main():
    global valor,investimento
    tipo = int(input("Digite o tipo de investimento (1 - Poupança / 2 - Renda Fixa): "))
    valor = float(input("Digite o valor do investimento: R$ "))
    investimento = calcular(valor,tipo)
    if investimento > 0:
        print(f"Valor corrigido em 30 dias: R$ {investimento:.2f}")
    else:
        print("Tipo de investimento inválido.")
        #Fim-se
main()
#Fim