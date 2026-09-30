#Inicio
def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado
    #Fim-para
def divisao(numero1, numero2):
    resultado = numero1 / numero2
    return resultado
def main():
    n = int(input("Digite o valor de N: "))
    soma = 1
    for i in range(1, n + 1):
        fat = fatorial(i)
        resultado = divisao(1, fat)
        soma = soma + resultado
    #Fim-para
    print("Resultado:", soma)
main()
#Fim