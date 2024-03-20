import re
def verificador_de_codigo(codigo):
    codigo_correto = r'^[a-zA-Z_]*$'

    if re.match(codigo_correto, codigo):
        return True
    else:
        return False
    
codigo_usuario = input("Insira o codigo de usuario: ")

if verificador_de_codigo(codigo_usuario):
    print("O código está correto")
else:
    print("O código não pode ter numero")