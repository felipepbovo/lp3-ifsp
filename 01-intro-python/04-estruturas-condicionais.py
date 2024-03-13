# if, if/else, if, elif, ternario, match

# if
# if condição
#    corpo
#    corpo
#    corpo

idade = 20

if idade >= 18:
    print('Maior de idade')
    print('Acabou o programa')

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

print('Agora acabou')


# criança(0-12), adolescente(13-17), adulto(18-59) ou idoso(60+)

if idade <= 12:
    print('Crianca')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
else:
    print('Idoso')


# if aninhado (evitar)

email = 'joao@email.com'
senha = '123456'

if email == 'joao@email.com':
    if senha == '123456':
        print('Acesso liberado')
    else:
        print('Email ou senha incorretos')

# código melhorado
if email == 'joao@email.com' and senha == '123456':
    print('acesso liberado')
else:
    print('Email ou senha incorretos')

# condição complexa no if
# permitir a entrada se:
# o usuario não estiver bloqueado E
# o usuario for um funcionario
# o hora atual entre 8 e 18
# ou
# o usuario é admin

usuario_bloqueado = False
usuario_funcionario = True
hora_atual = 19
usuario_admin = False

if not (usuario_bloqueado and usuario_funcionario and hora_atual >=8 and hora_atual <= 18) or usuario_admin:
    print('Liberado')
else:
    print('Nao liberado')


horario_comercial = hora_atual >=8 and hora_atual <= 18
usuario_ativo = usuario_funcionario and not usuario_bloqueado
liberado = (usuario_ativo and horario_comercial) or usuario_admin

if liberado:
    print('liberado')
else:
    print('nao liberado')

# entrada: hora_atual 
# saída: hora_atual está dentro do horario comercial (bool)

def dentro_horario_comercial(hora_atual):
    return hora_atual >=8 and hora_atual <=18


#operador ternario
if idade >=18:
    status = 'maior'
else:
    status = 'menor'

status = 'maior' if idade >=18 else 'menor'

# usuario  passa o dia (int)
# devolve String nome
# 1 - Domingo, 2 - Segunda ... 7 - sábado
dia = 4

dias = {
    1: 'Domingo',
    2: 'Segunda',
    3: 'terca',
    4: 'Quarta',
    5: 'Quinta',
    6: 'Sexta',
    7: 'Sabado'
}

if dia in dias:
    print(dias[dia])

# match
# python
# 'switch case' mais poderoso

dia = 2
match dia:
    case 1:
        print('domingo')
    case 2:
        print('segunda')
    case 3:
        print('terca')
    case 4:
        print('quarta')
    case 5:
        print('quinta')
    case 6:
        print('sexta')
    case 7:
        print('sabado')

match dia:
    case 1 | 7:
        print('Dim de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('Dia útil')
    case _:
        print('Inválido')