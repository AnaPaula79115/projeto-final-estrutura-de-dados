
import csv
import random
from pathlib import Path

from pessoa import Pessoa
from lista_encadeada import ListaEncadeada


class AtribuicoesSecretario:

    def __init__(self):
        self._lista = ListaEncadeada()

        # Localização do arquivo CSV na pasta principal
        self._arquivo_cidades = (
            Path(__file__).resolve().parent / "cidades_vizinhas.csv"
        )

        self._cidades = self._carregar_cidades()

    # Carregar as cidades existentes no CSV
    def _carregar_cidades(self):
        cidades = set()

        with open(
            self._arquivo_cidades,
            "r",
            encoding="utf-8-sig",
            newline=""
        ) as arquivo:

            leitor = csv.reader(arquivo, delimiter=";")

            for linha in leitor:
                if len(linha) >= 2:
                    cidade1 = linha[0].strip()
                    cidade2 = linha[1].strip()

                    if cidade1:
                        cidades.add(cidade1)

                    if cidade2:
                        cidades.add(cidade2)

        if not cidades:
            raise ValueError(
                "Nenhuma cidade encontrada no arquivo CSV."
            )

        return sorted(cidades)

    # Cadastrar uma pessoa
    def cadastrar_pessoa(self, nome, idade, telefone):

        nome = nome.strip()
        telefone = telefone.strip()

        if not nome:
            raise ValueError("O nome não pode ficar vazio.")

        if not isinstance(idade, int) or isinstance(idade, bool) or idade <= 0:
            raise ValueError("A idade deve ser um número inteiro positivo.")

        if not telefone:
            raise ValueError("O telefone não pode ficar vazio.")

        # Verificar se o nome já está cadastrado
        if self._lista.buscar_por_nome(nome) is not None:
            raise ValueError("Essa pessoa já está cadastrada.")

        # Escolher uma cidade aleatória
        cidade = random.choice(self._cidades)

        # Criar a pessoa
        pessoa = Pessoa(nome, idade, telefone, cidade)

        # Inserir na lista encadeada
        self._lista.inserir_no_fim(pessoa)

        return pessoa

    # Consultar uma pessoa pelo nome
    def consultar_pessoa(self, nome):
        return self._lista.buscar_por_nome(nome)

    # Consultar quantidade de pessoas
    def consultar_quantidade(self):
        return self._lista.quantidade()

    # Verificar se a lista está vazia
    def lista_vazia(self):
        return self._lista.esta_vazia()

    # Disponibilizar cadastros para a próxima etapa
    def obter_cadastros_para_transicao(self):
        return self._lista.iterar_pessoas()