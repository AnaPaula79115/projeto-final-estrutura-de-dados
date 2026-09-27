
class Pessoa:
    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Idade: {self.idade} | "
            f"Telefone: {self.telefone} | "
            f"Cidade: {self.cidade}"
        )