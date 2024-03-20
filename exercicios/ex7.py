def valor_imc(peso, altura):
    return peso / (altura * altura)

def calcular_imc(altura, peso):
    imc = valor_imc(peso, altura)

    if imc < 18.5:
        print('Baixo peso')
    elif imc < 24.9:
        print('Peso normal')
    elif imc < 29.9:
        print('Excesso de peso')
    elif imc < 34.9:
        print('Obesidade de Classe 1')
    elif imc < 39.9:
        print('Obesidade de Classe 2')
    else:
        print('Obesidade de Classe 3')

def calcular_diferenca(altura, peso):
    peso_necessario = (18.5 * altura * altura) - peso

    if valor_imc(altura, peso) < 18.5:
        print(f"Você precisa ganhar {peso_necessario} Kg")
    elif valor_imc(altura, peso) >= 25.0 and valor_imc(altura, peso) < 40.0:
        peso_necessario = (24.9 * altura * altura) - peso
        print(f"Você precisa perder {peso_necessario} Kg")

peso = float(input("Insira o peso em Kg: "))
altura = float(input("Insira a altura em metros: "))

print("Seu IMC é:")
calcular_imc(altura, peso)

print("Diferença de peso recomendada:")
calcular_diferenca(altura, peso)