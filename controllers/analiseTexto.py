import re
import string


def retorna_composicao(dados):
    input_convertido = dados.lower()
    letras = ""
    numeros = ""
    caracteres = ""
    espacos = len(re.findall(r"\s", input_convertido))
    input_espaco = input_convertido.isspace()
    for caracter in input_convertido:
        if caracter.isdigit():
            numeros += str(caracter)
        elif caracter.isalpha():
            letras += caracter
        else:
            caracteres += caracter
    return {
        "letras": letras,
        "numeros": str(numeros),
        "caracteres": caracteres,
        "espacos": espacos,
        "input_espaco": input_espaco,
        "dado": input_convertido,
    }


def retorna_composicao_mail(dados):
    input_convertido = dados.lower()
    input_convertido = input_convertido.strip()
    caracteres_validos_dominio = "."
    caracteres_validos_local = "+-_.@"
    email = re.search(r"^([^@]+)@(.+)$", input_convertido)
    local = email.group(1)
    inicio = local[:2]
    dominio = email.group(2)
    fim = dominio[len(dominio) - 2 :]
    arroba = input_convertido.count("@")
    caracteres_invalidos_local = verifica_caracteres_invalidos_local(
        local, caracteres_validos_local
    )
    caracteres_invalidos_dominio = verifica_caracteres_invalidos_dominio(
        dominio, caracteres_validos_dominio
    )
    espacos = len(re.findall(r"\s", input_convertido))
    input_espaco = input_convertido.isspace()

    return {
        "local": local,
        "inicio": inicio,
        "dominio": dominio,
        "fim": fim,
        "arroba": arroba,
        "caracteres_invalidos_local": caracteres_invalidos_local,
        "caracteres_invalidos_dominio": caracteres_invalidos_dominio,
        "espacos": espacos,
        "input_espaco": input_espaco,
        "dado": input_convertido,
    }


def verifica_caracteres_invalidos_dominio(dados, caracteres_validos):
    caracteres_invalidos = ""
    for caracter in dados:
        if (
            caracter not in caracteres_validos
            and caracter not in string.ascii_lowercase
        ):
            caracteres_invalidos += caracter

    return caracteres_invalidos


def verifica_caracteres_invalidos_local(dados, caracteres_validos):
    caracteres_invalidos = ""
    for caracter in dados:
        if (
            caracter not in caracteres_validos
            and caracter not in string.ascii_lowercase
        ):
            caracteres_invalidos += caracter

    return caracteres_invalidos
