from controllers.analiseTexto import retorna_composicao


def valida_telefone(componentes, campo):
    composicao = retorna_composicao(componentes)
    validacao = valida_composicao(composicao)
    resultado = {}

    if validacao["espacos"]:
        resultado = contrato_validacao_com_erro(
            campo, composicao, mensagem=f"{campo} contém espaço."
        )
    elif validacao["caracteres_invalidos"]:
        resultado = contrato_validacao_com_erro(
            campo,
            composicao,
            mensagem=f"{campo} contém caracteres inválido: '{composicao["letras"] + composicao["caracteres"]}'.",
        )
    elif validacao["tamanho_minimo"]:
        resultado = contrato_validacao_com_erro(
            campo, composicao, mensagem=f"{campo} deve ter no mínimo 3 letras."
        )
    elif validacao["tamanho_maximo"]:
        resultado = contrato_validacao_com_erro(
            campo, composicao, mensagem=f"{campo} deve ter exatos 9 digitos."
        )
    elif validacao["input_espaco"]:
        resultado = contrato_validacao_com_erro(
            campo, composicao, mensagem=f"{campo} obrigatório."
        )
    else:
        resultado = contrato_validacao_sem_erro(campo, composicao)
    return resultado


def valida_composicao(composicao):
    return {
        "tamanho_minimo": len(composicao["dado"]) < 9,
        "tamanho_maximo": len(composicao["dado"]) > 9,
        "caracteres_invalidos": len(composicao["letras"] + composicao["caracteres"])
        > 0,
        "espacos": composicao["espacos"] > 0,
        "input_espaco": composicao["espacos"] > 0,
    }


def contrato_validacao_com_erro(campo, componentes, mensagem):
    return {
        "campo": campo,
        "valor": componentes["dado"],
        "erro": True,
        "mensagem": mensagem,
    }


def contrato_validacao_sem_erro(campo, componentes):
    return {
        "campo": campo, 
        "valor": componentes["dado"], 
        "erro": False, 
        "mensagem": ""}
