from controllers.valida_nome import valida_nome


class DadosPessoais:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def validar_nome(self):
        return valida_nome(self.nome, "nome")

    def validar_sobrenome(self):
        return valida_nome(self.sobrenome, "sobrenome")


if __name__ == "__main__":
    pessoa = Pessoa("obson22", "ferreira22")
    print(pessoa.validar_nome())
    print(pessoa.validar_sobrenome())
