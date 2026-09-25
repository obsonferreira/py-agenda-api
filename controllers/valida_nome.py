from controllers.analiseTexto import retorna_composicao


def valida_nome(componentes, campo):
    composicao = retorna_composicao(componentes)
    validacao = valida_composicao(composicao)
    resultado = {}

    if validacao["espacos"]:
        resultado = contrato_validacao_com_erro(
            campo, composicao, mensagem=f"{campo} contém espaço."
        )
    elif validacao["tamanho_minimo"]:
        resultado = contrato_validacao_com_erro(
            campo, composicao, mensagem=f"{campo} deve ter no mínimo 3 letras."
        )
    elif validacao["tamanho_maximo"]:
        resultado = contrato_validacao_com_erro(
            campo, composicao, mensagem=f"{campo} deve ter no máximo 30 letras."
        )
    elif validacao["caracteres_invalidos"]:
        resultado = contrato_validacao_com_erro(
            campo,
            composicao,
            mensagem=f"{campo} contém {'caracteres inválidos' if len(composicao['numeros'] + composicao['caracteres']) > 1 else 'caractere inválido'} : '{composicao['numeros'] + composicao['caracteres']}'.",
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
        "tamanho_minimo": len(composicao["dado"]) < 3,
        "tamanho_maximo": len(composicao["dado"]) > 30,
        "caracteres_invalidos": len(composicao["numeros"] + composicao["caracteres"])
        > 0,
        "espacos": composicao["espacos"] > 0,
        "input_espaco": composicao["input_espaco"] == True,
    }


def contrato_validacao_com_erro(campo, componentes, mensagem):
    return {
        "campo": campo,
        "valor": componentes["dado"],
        "erro": True,
        "mensagem": mensagem,
    }


def contrato_validacao_sem_erro(campo, componentes):
    return {"campo": campo, "valor": componentes["dado"], "erro": False, "mensagem": ""}
