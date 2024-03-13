## operadores aritméticos
# +, -, *, /, %, **

nota1 = 3.5
nota2 = 5.5
media = (nota1 + nota2) /2

# 2 elevado ao quadrado
potencia = 2 ** 2

# 2 elevado ao cubo
potencia = 2 ** 3

numero = 2 * 2 * 2

# operadores de atribuição
# =, +=, -=, ...
idade = 20

# idade = idade + 10
idade += 10

#operadores lógicos
# and, for , not

resultado = True and False
print (type(resultado))
print (resultado)

#  and               or
# 1 1 = 1           1 1 = 1
# 1 0 = 0           1 0 = 1
# 0 1 = 0           0 1 = 1
# 0 0 = 0           0 0 = 0

#operdadores de comparação
# ==, !=, >, <, >=, <=

idade = 17 

if idade >=18: 
    print (' Maior de idade')
else:
    print ('Menor')


# operador is
# os valores do objeto e se ocupam o mesmo 
# espaço de memória

a = [1,2,3]
b = [1,2,3]
print (a is b)

z = [1,2,3]

x = z
print(z is x)

# operador in e not in
#verificar se um objeto está ou não em dentro de uma sequência (str, list, tuple, ...)

print('a' in 'java')
print('maria' in ['Pedro', 'Ana'])

alunos = ['Pedro', 'Ana']
aluno = 'Maria'
print(aluno in alunos)
print(aluno not in alunos)