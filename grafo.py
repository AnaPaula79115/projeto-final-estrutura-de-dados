import csv
import heapq
from pathlib import Path


class Grafo:

    def __init__(self):

        # Dicionário que armazenará o grafo
        self.adjacencias = {}

        # Caminho do arquivo CSV
        self.arquivo_cidades = (
            Path(__file__).resolve().parent / "cidades_vizinhas.csv"
        )

        # Construir o grafo a partir do CSV
        self.carregar_csv()

    # Adicionar conexão entre duas cidades
    def adicionar_aresta(self, cidade1, cidade2, distancia):

        if distancia < 0:
            raise ValueError(
                "A distância não pode ser negativa."
            )

        # Criar as cidades caso ainda não existam
        if cidade1 not in self.adjacencias:
            self.adjacencias[cidade1] = {}

        if cidade2 not in self.adjacencias:
            self.adjacencias[cidade2] = {}

        # Conexão nos dois sentidos
        self.adjacencias[cidade1][cidade2] = distancia
        self.adjacencias[cidade2][cidade1] = distancia

    # Ler o arquivo CSV
    def carregar_csv(self):

        with open(
            self.arquivo_cidades,
            "r",
            encoding="utf-8-sig",
            newline=""
        ) as arquivo:

            leitor = csv.reader(arquivo, delimiter=";")

            for numero_linha, linha in enumerate(leitor, start=1):

                # Ignorar linhas completamente vazias
                if not linha or not any(campo.strip() for campo in linha):
                    continue

                if len(linha) != 3:
                    raise ValueError(
                        f"Formato inválido na linha {numero_linha}."
                    )

                cidade1 = linha[0].strip()
                cidade2 = linha[1].strip()

                if not cidade1 or not cidade2:
                    raise ValueError(
                        f"Cidade inválida na linha {numero_linha}."
                    )

                try:
                    distancia = int(linha[2].strip())

                except ValueError:
                    raise ValueError(
                        f"Distância inválida na linha {numero_linha}."
                    )

                self.adicionar_aresta(
                    cidade1,
                    cidade2,
                    distancia
                )

    # Verificar se uma cidade existe
    def existe_cidade(self, cidade):
        return cidade in self.adjacencias

    # Consultar as cidades vizinhas
    def vizinhos(self, cidade):
        return self.adjacencias.get(cidade, {})

    # Consultar quantidade de cidades
    def quantidade_cidades(self):
        return len(self.adjacencias)

    # Calcular o menor caminho utilizando Dijkstra
    def menor_caminho(self, origem, destino):

        if not self.existe_cidade(origem):
            return None, []

        if not self.existe_cidade(destino):
            return None, []

        # Distâncias iniciais
        distancias = {
            cidade: float("inf")
            for cidade in self.adjacencias
        }

        distancias[origem] = 0

        # Guardar a cidade anterior
        anteriores = {}

        # Fila de prioridade
        fila = [(0, origem)]

        while fila:

            distancia_atual, cidade_atual = heapq.heappop(fila)

            if distancia_atual > distancias[cidade_atual]:
                continue

            if cidade_atual == destino:
                break

            # Percorrer as cidades vizinhas
            for vizinho, peso in self.vizinhos(cidade_atual).items():

                nova_distancia = distancia_atual + peso

                if nova_distancia < distancias[vizinho]:

                    distancias[vizinho] = nova_distancia

                    anteriores[vizinho] = cidade_atual

                    heapq.heappush(
                        fila,
                        (nova_distancia, vizinho)
                    )

        # Verificar se existe um caminho
        if distancias[destino] == float("inf"):
            return None, []

        # Reconstruir o caminho
        caminho = []

        cidade = destino

        while cidade != origem:

            caminho.append(cidade)

            cidade = anteriores[cidade]

        caminho.append(origem)

        caminho.reverse()

        return distancias[destino], caminho

    
    # Calcular caminho passando por uma cidade intermediária
    def menor_caminho_via(self, origem, intermediaria, destino):

        # Primeira parte do percurso
        distancia1, caminho1 = self.menor_caminho(
            origem, intermediaria
        )

        # Segunda parte do percurso
        distancia2, caminho2 = self.menor_caminho(
            intermediaria, destino
        )

        # Verificar se os caminhos existem
        if distancia1 is None or distancia2 is None:
            return None, []

        # Somar as distâncias
        distancia_total = distancia1 + distancia2

        # Unir os caminhos sem duplicar a cidade de junção
        caminho_completo = caminho1 + caminho2[1:]

        # Garantir que a cidade obrigatória fique no
        # interior do percurso, mesmo quando coincidir
        # com a origem ou com o destino.
        if intermediaria not in caminho_completo[1:-1]:

            vizinhos = [
                (peso, cidade)
                for cidade, peso in self.vizinhos(intermediaria).items()
                if cidade != intermediaria
            ]

            if not vizinhos:
                return None, []

            peso, vizinho = min(vizinhos)

            volta = [vizinho, intermediaria]

            caminho_completo = caminho1 + volta + caminho2[1:]
            distancia_total += 2 * peso

            # Caso especial: origem e destino são a
            # própria cidade intermediária.
            if intermediaria not in caminho_completo[1:-1]:
                caminho_completo = caminho1 + volta + volta + caminho2[1:]
                distancia_total += 2 * peso

        return distancia_total, caminho_completo