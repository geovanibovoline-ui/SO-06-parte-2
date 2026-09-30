#Inicio
def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado
    #Fim-para
def main():
    numero = int(input("Digite um número: "))
    resultado = fatorial(numero)
    print("Fatorial:", resultado)
main()
#Fim