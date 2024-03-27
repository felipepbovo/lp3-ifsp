nota = int(input("Insira a nota do aluno: "))

if nota <= 100 and nota >= 76:
    print('nota: A')
elif nota <=  75 and nota >= 51:
    print('nota: B')
elif nota <= 50 and nota >= 26:
    print('nota: C')
elif nota <= 25 and nota >= 12:
    print('nota: D')
else:
    print('nota : F')
