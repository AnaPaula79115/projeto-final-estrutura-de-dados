
class NoArvore:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None
        self._quantidade = 0

    # Padronizar o nome utilizado nas buscas
    def _chave(self, nome):
        return nome.strip().casefold()

    # Inserir uma pessoa na árvore
    def inserir(self, pessoa):

        novo_no = NoArvore(pessoa)

        if self.raiz is None:
            self.raiz = novo_no
            self._quantidade += 1
            return

        atual = self.raiz

        while True:

            chave_nova = self._chave(pessoa.nome)
            chave_atual = self._chave(atual.pessoa.nome)

            if chave_nova == chave_atual:
                raise ValueError(
                    "Já existe uma pessoa cadastrada com esse nome."
                )

            elif chave_nova < chave_atual:

                if atual.esquerda is None:
                    atual.esquerda = novo_no
                    self._quantidade += 1
                    return

                atual = atual.esquerda

            else:

                if atual.direita is None:
                    atual.direita = novo_no
                    self._quantidade += 1
                    return

                atual = atual.direita

    # Buscar uma pessoa pelo nome
    def buscar(self, nome):

        atual = self.raiz
        chave = self._chave(nome)

        while atual is not None:

            chave_atual = self._chave(atual.pessoa.nome)

            if chave == chave_atual:
                return atual.pessoa

            elif chave < chave_atual:
                atual = atual.esquerda

            else:
                atual = atual.direita

        return None

    # Encontrar o primeiro nome em ordem alfabética
    def menor(self):

        atual = self.raiz

        if atual is None:
            return None

        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual.pessoa

    # Encontrar o último nome em ordem alfabética
    def maior(self):

        atual = self.raiz

        if atual is None:
            return None

        while atual.direita is not None:
            atual = atual.direita

        return atual.pessoa

    # Consultar a quantidade de pessoas
    def quantidade(self):
        return self._quantidade

    # Verificar se a árvore está vazia
    def esta_vazia(self):
        return self.raiz is None

    # Percorrer os cadastros em ordem alfabética
    def iterar_pessoas(self):

        def percorrer(no):

            if no is not None:

                yield from percorrer(no.esquerda)

                yield no.pessoa

                yield from percorrer(no.direita)

        yield from percorrer(self.raiz)

        
    # Excluir uma pessoa pelo nome
    def excluir(self, nome):

        chave = self._chave(nome)

        self.raiz, excluido = self._excluir_no(
            self.raiz, chave
        )

        if excluido:
            self._quantidade -= 1

        return excluido

    # Método auxiliar para realizar a exclusão
    def _excluir_no(self, no, chave):

        if no is None:
            return None, False

        chave_atual = self._chave(no.pessoa.nome)

        if chave < chave_atual:

            no.esquerda, excluido = self._excluir_no(
                no.esquerda, chave
            )

            return no, excluido

        elif chave > chave_atual:

            no.direita, excluido = self._excluir_no(
                no.direita, chave
            )

            return no, excluido

        # Caso 1 e 2: nó sem filhos ou com apenas um filho
        if no.esquerda is None:
            return no.direita, True

        if no.direita is None:
            return no.esquerda, True

        # Caso 3: nó com dois filhos
        sucessor = self._menor_no(no.direita)

        no.pessoa = sucessor.pessoa

        no.direita, _ = self._excluir_no(
            no.direita,
            self._chave(sucessor.pessoa.nome)
        )

        return no, True

    # Encontrar o menor nó de uma subárvore
    def _menor_no(self, no):

        atual = no

        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual