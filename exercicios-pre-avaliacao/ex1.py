# Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
# Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.


import random
aleatorio = random.randint(1, 100)

while True:
    comando = int(input('tente acertar o número: '))

    if comando == aleatorio:
        print('fala dele, você acertou o número')
        break
    if comando > aleatorio:
        print('número acima do esperado')
    if comando < aleatorio:
        print('número abaixo do esperado')