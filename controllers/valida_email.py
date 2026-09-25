from controllers.analiseTexto import retorna_composicao_mail


def valida_email(input):
    composicao = retorna_composicao_mail(input)
    validacao = valida_composicao(composicao)
    print(len(composicao))
    print(validacao)


def valida_composicao(composicao):
    return {
        "espacos": composicao["espacos"] > 0,
        "tamanhoMinimo": len(composicao["dado"]) < 3,
        "tamanhoMaximo": len(composicao["dado"]) > 254,
    }


email = "   "

valida_email(email)
