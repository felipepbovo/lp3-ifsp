
valor = float(input('insira o valor da compra:'))
if (valor >=10 and valor <=99.99):
    print(valor * 0.95) 
elif (valor >=100 and valor <=499.99):
    print(valor * 0.90)
elif (valor >= 500):
    print(valor * 0.85)
else:
    print(valor)