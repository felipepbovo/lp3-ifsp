def criar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    invertido = texto[::-1]
    
    if texto == invertido:
        return True
    else:
        return False

entrada = input("insira uma palavra ou frase: ")
if criar_palindromo(entrada):
    print("É palíndromo!")
else:
    print("Não é palíndromo!")