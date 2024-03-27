def contar_palavras(frase):
    frase = frase.lower()
    for char in '.,!?;:':
        frase = frase.replace(char, '')
    
    palavras = frase.split()

    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem

texto = input("Digite o texto: ")
resultado = contar_palavras(texto)
print("Contagem de palavras:")
print(resultado)