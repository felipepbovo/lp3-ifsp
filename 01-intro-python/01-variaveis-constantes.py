# identificadores
# latra, números e _
# não pode ser palavra reservada: if, none, true, False
# case sensitive

nome = "pedro"
nome = "Pedro"

# variáveis
# tudo em minusculo
# separador _
# snake_case
idade = 20
pessoa_fisica = "Marcio"
pessoa_juridica = 'paula LTDA'
imposto_renda = 2200.45

# E o tipo?
# java
# String nome = "Pedro"
# int idade = 20
# No python temos inferência de tipo
# O tipo será definido com base no valor

idade = 20 #int
nome = "Pedro" #str

#constantes
# não existe constante no python
# convenção: nome em maiúsculo

PI = 3.14

# Comentários de única linha 

'''
comentário de
múltiplas linhas
'''

# docstring (comentários de documentação)
# documentar classe, módulos, funções, ...

def somar(numero1, numero2):
    '''
    Função que soma dois números
    :param numero1: primeiro número
    :param numero2: segundo número
    :return a soma dos dois números
    '''
    return numero1 + numero2

