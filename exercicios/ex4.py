import re

def verificador_de_codigo(codigo):
    codigo_padrao = r'^BR\d{4}X$'

    if re.match(codigo_padrao, codigo):
        return True
    else:
        return False
    
codigo_funcionario = input("Insira o código de funcionário: ")

if verificador_de_codigo(codigo_funcionario):
    print("O código do funcionário está correto")
else:
    print("O código do funcionário não está correto")