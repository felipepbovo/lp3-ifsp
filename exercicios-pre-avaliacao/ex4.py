contador = [0,0,0]

for i in range(3):
    comando = int(input('insira o seu voto: '))

    if comando == 1:
        print('votou no Jonas')
        contador[0] += 1

    if comando == 2:
        print('votou no Clovis')
        contador[1] += 1
    if comando == 3:
        print('votou no Cara')
        contador[2] += 1

if contador[0] > contador[1] and contador[0] > contador[2]:
    print ('parabens Jonas')
elif contador[1] > contador[0] and contador[1] > contador[0]:
    print('parabens Clovis')
else:
    contador[2] > contador[1] and contador[2]> contador[1]
    print('parabens Cara')
