tabuada = int(input("Digite um numero de 0 a 10: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))