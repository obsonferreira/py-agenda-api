from controllers.valida_email import valida_email
from controllers.valida_telefone import valida_telefone


class Contatos:
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email

    def validar_telefone(self):
        return valida_telefone(self.telefone, "telefone")

    def valida_email(self):
        return valida_email(self.email, "email")
