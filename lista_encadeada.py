
from pessoa import Pessoa


class No:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self._quantidade = 0

    # Inserir uma pessoa no final da lista
    def inserir_no_fim(self, pessoa):
        novo_no = No(pessoa)

        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio

            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = novo_no

        self._quantidade += 1

    # Buscar uma pessoa pelo nome
    def buscar_por_nome(self, nome):
        atual = self.inicio

        while atual is not None:
            if atual.pessoa.nome.casefold() == nome.strip().casefold():
                return atual.pessoa

            atual = atual.proximo

        return None

    # Consultar quantidade de cadastrados
    def quantidade(self):
        return self._quantidade

    # Verificar se a lista está vazia
    def esta_vazia(self):
        return self.inicio is None

    # Percorrer as pessoas cadastradas
    def iterar_pessoas(self):
        atual = self.inicio

        while atual is not None:
            yield atual.pessoa
            atual = atual.proximo