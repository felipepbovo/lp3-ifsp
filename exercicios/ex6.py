comprimento =  float(input('insira o comprimento do seu aquário: '))
largura =  float(input('insira a largura do seu aquário: '))
altura = float(input('insira a altura do seu aquário: '))
temperatura_ambiente =  float(input('insira a temperatura ambiente atual: '))
temperatura_desejada = float(input('insira a temperatura desejada: '))

def calcular_volume(comprimento, largura, altura):
    volume=(comprimento * altura * largura) / 1000
    return volume

def calcular_potencia_termostato(temperatura_desejada, temperatura_ambiente):
    potencia=calcular_volume(comprimento,largura,altura)* 0.05 * (temperatura_desejada - temperatura_ambiente)
    return potencia

def calcular_filtragem():
    filtragem = calcular_volume(comprimento,altura,largura) * 2.5
    return filtragem

print("\nVolume: " ,calcular_volume(comprimento, largura, altura))
print("Potencia do termostato: ", calcular_potencia_termostato(temperatura_desejada, temperatura_ambiente))
print("Filtragem por hora: ", calcular_filtragem())