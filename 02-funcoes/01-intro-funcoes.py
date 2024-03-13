# Função
# modularizar o programa
# reuso
# manutenabilidade

# só pode acesssar hora se estiver entre 8h e 18h
hora_atual = 12

if hora_atual >=8 and hora_atual <= 18:
    print('permitindo acesso')

# entrada = hora_atual
# saída se está dentro ou não do horario comercial
def dentro_horario_comercial(hora_atual):
    if hora_atual >= 8 and hora_atual <= 18:
        print('permitindo acesso')
        return True
    else:
        return False

def dentro_horario_comercial(hora_atual):
    return hora_atual >= 8 and hora_atual <= 18

# Declaração
# def nome_funcao():
#   corpo da função
#   corpo da função

# Função sem retorno
# side effect - efeito colateral
def diga_ola(nome):
    print(f"Olá {nome}")

#chamada
diga_ola('marcos')

# Função com retorno
# Sem side effect = função pura
def montar_frase(nome):
    return f"Olá {nome}"

nome = 'marcos'
print(montar_frase('marcos'))

# Parâmetro e Argumentos
# parâmetros referências que podem ser acessadas dentro da função
# Argumnto são os valores passados para os parãmetros

def somar (numero1, numero2):
    return numero1 + numero2

somar(10.0, 5.0)

# Escopo de variáveis
# variável local
def calcular_media (nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

# variável global
total = 0

def soma(n1, n2, n3):
    global total
    total = n1 + n2 + n3
    return total

print(total)
soma(1, 3, 5)
print(total)

# parâmetros com valor padrão (default)
def boas_vindas(nome, mensagem='Bom dia'):
    return f"{mensagem}, {nome}"

print(boas_vindas('marcos', 'Bom dia'))
print(boas_vindas('Marilene', 'Boa tarde'))
print(boas_vindas('maria'))

# Argumentos nomeados
print(boas_vindas(nome='maria'))

# Docstring
# comentário da documentação
def somar(n1, n2):
    '''
    Função que soma dois números
    :param n1: primeiro número
    :param n2: segundo número
    :return: soma dois números
    '''
    return n1 + n2

# Funções built-in
# print, type, len, sum, max, min, input
