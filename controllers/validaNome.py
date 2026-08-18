import string
from analiseTexto import retornComposicao
# string.ascii_lowercase +  "11223"
letras = "àáâãäçèéêìíîòóôõöùúûüýÿ" +  "$%¨&*()"
composicaoTeste = retornComposicao(letras)


def validaNome(componentes, campo):
    validacao = verificaComposicao(componentes)
    resultado = {}
    if not validacao["dadoValido"]:
        if validacao["espacos"]:
            resultado = contratoOperacaoComErro(
                campo, componentes, mensagem=f"{campo} contém espaço."
            )
        elif validacao["tamanhoMinimo"]:
            resultado = contratoOperacaoComErro(
                campo, componentes, mensagem=f"{campo} deve ter no mínimo 3 letras."
            )
        elif validacao["tamanhoMaximo"]:
            resultado = contratoOperacaoComErro(
                campo, componentes, mensagem=f"{campo} deve ter no máximo 30 letras."
            )
        elif validacao["caracteresInvalidos"]:
            resultado = contratoOperacaoComErro(
                campo,
                componentes,
                mensagem=f"{campo} contém caracteres inválido: '{componentes["numeros"] + componentes["caracteres"]}'.",
            )
        else:
            pass
    else:
        resultado = contratoOperacaoSemErro(campo, componentes)
    return resultado


def verificaComposicao(composicao):
    return {
        "tamanhoMinimo": len(composicao["dado"]) < 3,
        "tamanhoMaximo": len(composicao["dado"]) > 30,
        "caracteresInvalidos": len(composicao["numeros"] + composicao["caracteres"])
        > 0,
        "espacos": composicao["espacos"] > 0,
        "dadoValido": composicao["dado"].isalpha(),
    }


def contratoOperacaoComErro(campo, componentes, mensagem):
    return {
        "campo": campo,
        "valor": componentes["dado"],
        "erro": True,
        "mensagem": mensagem,
    }


def contratoOperacaoSemErro(campo, componentes):
    return {
        "campo": campo,
        "valor": componentes["dado"],
        "erro": False,
        "mensagem": "",
    }


validacao = validaNome(composicaoTeste, "nome")
print(validacao)
