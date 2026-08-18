from analiseTexto import retornaComposicao


def validaTelefone(componentes, campo):
    composicao = retornaComposicao(componentes)
    validacao = verificaComposicao(composicao)
    print(composicao)
    resultado = {}
    if not validacao["dadoValido"]:
        if validacao["espacos"]:
            resultado = contratoOperacaoComErro(campo, composicao, mensagem=f"{campo} contém espaço.")
        elif validacao["caracteresInvalidos"]:
            resultado = contratoOperacaoComErro(campo, composicao, mensagem=f"{campo} contém caracteres inválido: '{composicao["letras"] + composicao["caracteres"]}'.")
        elif validacao["tamanhoMinimo"]:
            resultado = contratoOperacaoComErro(campo, composicao, mensagem=f"{campo} deve ter no mínimo 3 letras.")
        elif validacao["tamanhoMaximo"]:
            resultado = contratoOperacaoComErro(campo, composicao, mensagem=f"{campo} deve ter exatos 9 digitos.")
        elif validacao["caracteresInvalidos"]:
            resultado = contratoOperacaoComErro(campo, composicao, mensagem=f"{campo} contém caracteres inválido: '{composicao["letras"] + composicao["caracteres"]}'.")
    else:
        resultado = contratoOperacaoSemErro(campo, composicao)
    return resultado


def verificaComposicao(composicao):
    return {"tamanhoMinimo": len(composicao["dado"]) < 9, "tamanhoMaximo": len(composicao["dado"]) > 9, "caracteresInvalidos": len(composicao["letras"] + composicao["caracteres"]) > 0, "espacos": composicao["espacos"] > 0, "dadoValido": composicao["dado"].isdigit()}


def contratoOperacaoComErro(campo, componentes, mensagem):
    return {"campo": campo, "valor": componentes["dado"], "erro": True, "mensagem": mensagem}


def contratoOperacaoSemErro(campo, componentes):
    return {"campo": campo, "valor": componentes["dado"], "erro": False, "mensagem": ""}


telefone = "991527102a"

teste = validaTelefone(telefone, campo="telefone")

print(teste)
