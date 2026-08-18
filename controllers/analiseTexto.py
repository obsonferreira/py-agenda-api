import re


def retornComposicao(input):
    letras = ""
    numeros = ""
    caracteres = ""
    espacos = len(re.findall(r"\s", input))
    for caracter in input:
        if caracter.isdigit():
            numeros += str(caracter)
        elif caracter.isalpha():
            letras += caracter
        else:
            caracteres += caracter
    return {
        "letras": letras,
        "numeros": numeros,
        "caracteres": caracteres,
        "espacos": espacos,
        "dado": input,
    }
