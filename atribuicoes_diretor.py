
from arvore_binaria import ArvoreBinariaBusca


class AtribuicoesDiretor:

    def __init__(self, pessoas_iniciais=()):

        self._arvore = ArvoreBinariaBusca()

        # Transferir os cadastros da lista para a árvore
        for pessoa in pessoas_iniciais:
            self._arvore.inserir(pessoa)

    # Consultar uma pessoa pelo nome
    def consultar_pessoa(self, nome):
        return self._arvore.buscar(nome)

    # Alterar o nome de uma pessoa
    def alterar_nome(self, nome_atual, novo_nome):

        novo_nome = novo_nome.strip()

        if not novo_nome:
            raise ValueError("O nome não pode ficar vazio.")

        pessoa = self._arvore.buscar(nome_atual)

        if pessoa is None:
            return None

        # Verificar se o novo nome já existe
        existente = self._arvore.buscar(novo_nome)

        if existente is not None and existente is not pessoa:
            raise ValueError(
                "Já existe uma pessoa cadastrada com esse nome."
            )

        # Se a chave não mudou, basta atualizar a escrita
        if pessoa.nome.casefold() == novo_nome.casefold():
            pessoa.nome = novo_nome
            return pessoa

        # Remover a chave antiga
        self._arvore.excluir(pessoa.nome)

        # Atualizar o nome
        pessoa.nome = novo_nome

        # Reinserir para manter a organização da árvore
        self._arvore.inserir(pessoa)

        return pessoa

    # Alterar a idade
    def alterar_idade(self, nome, nova_idade):

        if (
            not isinstance(nova_idade, int)
            or isinstance(nova_idade, bool)
            or nova_idade <= 0
        ):
            raise ValueError(
                "A idade deve ser um número inteiro positivo."
            )

        pessoa = self._arvore.buscar(nome)

        if pessoa is None:
            return None

        pessoa.idade = nova_idade

        return pessoa

    # Alterar o telefone
    def alterar_telefone(self, nome, novo_telefone):

        novo_telefone = novo_telefone.strip()

        if not novo_telefone:
            raise ValueError(
                "O telefone não pode ficar vazio."
            )

        pessoa = self._arvore.buscar(nome)

        if pessoa is None:
            return None

        pessoa.telefone = novo_telefone

        return pessoa

    # Excluir pessoa cadastrada
    def excluir_pessoa(self, nome):
        return self._arvore.excluir(nome)

    # Primeiro nome em ordem alfabética
    def primeiro_nome(self):
        return self._arvore.menor()

    # Último nome em ordem alfabética
    def ultimo_nome(self):
        return self._arvore.maior()

    # Consultar quantidade de cadastrados
    def consultar_quantidade(self):
        return self._arvore.quantidade()

    # Verificar se a árvore está vazia
    def arvore_vazia(self):
        return self._arvore.esta_vazia()

    # Disponibilizar os cadastros para o assistente
    def obter_cadastros_para_transicao(self):
        return self._arvore.iterar_pessoas()