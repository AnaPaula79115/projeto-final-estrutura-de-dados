
from grafo import Grafo


class AtribuicoesAssistente:

    def __init__(self, diretor):

        # Utilizar os cadastros atualizados pelo diretor
        self._diretor = diretor

        # Criar o grafo das cidades
        self._grafo = Grafo()

        # Cidades definidas pelo enunciado
        self._origem = "Guarujá"
        self._intermediaria = "Indaiatuba"

    # Consultar pessoa cadastrada
    def consultar_pessoa(self, nome):

        return self._diretor.consultar_pessoa(nome)

    # OPÇÃO 1 - Menor distância até uma pessoa
    def menor_distancia_para_pessoa(self, nome):

        pessoa = self.consultar_pessoa(nome)

        if pessoa is None:
            return None, None, []

        distancia, caminho = self._grafo.menor_caminho(
            self._origem,
            pessoa.cidade
        )

        return pessoa, distancia, caminho

    # OPÇÃO 2 - Menor caminho passando por Indaiatuba
    def menor_distancia_via_indaiatuba(self, nome):

        pessoa = self.consultar_pessoa(nome)

        if pessoa is None:
            return None, None, []

        distancia, caminho = self._grafo.menor_caminho_via(
            self._origem,
            self._intermediaria,
            pessoa.cidade
        )

        return pessoa, distancia, caminho

    # OPÇÃO 3 - Cidade mais próxima com moradores
    def cidade_mais_proxima_com_moradores(self):

        # Agrupar os estudantes por cidade
        moradores_por_cidade = {}

        for pessoa in self._diretor.obter_cadastros_para_transicao():

            cidade = pessoa.cidade

            if cidade not in moradores_por_cidade:
                moradores_por_cidade[cidade] = []

            moradores_por_cidade[cidade].append(pessoa)

        # Verificar se existem estudantes
        if not moradores_por_cidade:
            return None, None, []

        cidade_mais_proxima = None
        menor_distancia = None

        # Comparar as distâncias das cidades
        for cidade in sorted(
            moradores_por_cidade,
            key=str.casefold
        ):

            distancia, caminho = self._grafo.menor_caminho(
                self._origem,
                cidade
            )

            if distancia is None:
                continue

            if (
                menor_distancia is None
                or distancia < menor_distancia
            ):

                menor_distancia = distancia
                cidade_mais_proxima = cidade

        # Nenhuma cidade alcançável
        if cidade_mais_proxima is None:
            return None, None, []

        moradores = moradores_por_cidade[
            cidade_mais_proxima
        ]

        return (
            cidade_mais_proxima,
            menor_distancia,
            moradores
        )