
from atribuicoes_secretario import AtribuicoesSecretario
from atribuicoes_diretor import AtribuicoesDiretor
from atribuicoes_assistente import AtribuicoesAssistente


# Etapa 1 - Menu do Secretário
def executar_secretario(secretario):

    print("\n===== BEM-VINDO(A), SECRETÁRIO(A)! =====")

    while True:

        print("\n===== MENU DO SECRETÁRIO =====")
        print("1 - Cadastrar pessoa na lista de espera")
        print("2 - Consultar pessoa cadastrada")
        print("3 - Consultar quantidade de pessoas")
        print("4 - Finalizar operações")

        opcao = input("\nEscolha uma opção: ").strip()

        # OPÇÃO 1 - CADASTRAR PESSOA
        if opcao == "1":

            print("\n--- CADASTRO DE PESSOA ---")

            nome = input("Nome: ").strip()

            try:
                idade = int(input("Idade: ").strip())

            except ValueError:
                print("Erro: informe uma idade válida.")
                continue

            telefone = input("Telefone: ").strip()

            try:
                pessoa = secretario.cadastrar_pessoa(
                    nome, idade, telefone
                )

                print("\nPessoa cadastrada com sucesso!")
                print(pessoa)

            except ValueError as erro:
                print(f"\nErro: {erro}")

        # OPÇÃO 2 - CONSULTAR PESSOA
        elif opcao == "2":

            print("\n--- CONSULTAR PESSOA ---")

            if secretario.lista_vazia():
                print("A lista de espera está vazia.")
                continue

            nome = input("Informe o nome: ").strip()

            pessoa = secretario.consultar_pessoa(nome)

            if pessoa is None:
                print("Pessoa não encontrada.")

            else:
                print("\nPessoa encontrada:")
                print(pessoa)

        # OPÇÃO 3 - CONSULTAR QUANTIDADE
        elif opcao == "3":

            quantidade = secretario.consultar_quantidade()

            print(
                f"\nQuantidade de pessoas cadastradas: {quantidade}"
            )

        # OPÇÃO 4 - FINALIZAR
        elif opcao == "4":

            print("\nOperações do secretário finalizadas.")
            break

        # OPÇÃO INVÁLIDA
        else:

            print(
                "\nOpção inválida! Digite um número de 1 a 4."
            )

    return secretario


# Etapa 2 - Menu do Diretor
def executar_diretor(diretor):

    print("\n===== BEM-VINDO(A), DIRETOR(A)! =====")

    while True:

        print("\n===== MENU DO DIRETOR =====")
        print("1 - Alterar informações de uma pessoa")
        print("2 - Descadastrar uma pessoa")
        print("3 - Consultar primeiro nome em ordem alfabética")
        print("4 - Consultar último nome em ordem alfabética")
        print("5 - Finalizar operações")

        opcao = input("\nEscolha uma opção: ").strip()

        # OPÇÃO 1 - ALTERAR INFORMAÇÕES
        if opcao == "1":

            nome = input("Nome da pessoa: ").strip()

            pessoa = diretor.consultar_pessoa(nome)

            if pessoa is None:
                print("Pessoa não encontrada.")
                continue

            print("\nDados atuais:")
            print(pessoa)

            print("\nO que deseja alterar?")
            print("1 - Nome")
            print("2 - Idade")
            print("3 - Telefone")

            escolha = input(
                "\nEscolha uma opção: "
            ).strip()

            try:

                # ALTERAR NOME
                if escolha == "1":

                    novo_nome = input(
                        "Novo nome: "
                    ).strip()

                    pessoa = diretor.alterar_nome(
                        nome, novo_nome
                    )

                # ALTERAR IDADE
                elif escolha == "2":

                    nova_idade = int(
                        input("Nova idade: ").strip()
                    )

                    pessoa = diretor.alterar_idade(
                        nome, nova_idade
                    )

                # ALTERAR TELEFONE
                elif escolha == "3":

                    novo_telefone = input(
                        "Novo telefone: "
                    ).strip()

                    pessoa = diretor.alterar_telefone(
                        nome, novo_telefone
                    )

                else:
                    print("Opção inválida.")
                    continue

                print(
                    "\nInformações alteradas com sucesso!"
                )

                print(pessoa)

            except ValueError as erro:
                print(f"Erro: {erro}")

        # OPÇÃO 2 - DESCADASTRAR
        elif opcao == "2":

            nome = input(
                "Nome da pessoa a descadastrar: "
            ).strip()

            pessoa = diretor.consultar_pessoa(nome)

            if pessoa is None:
                print("Pessoa não encontrada.")
                continue

            print("\nPessoa encontrada:")
            print(pessoa)

            # Solicitar confirmação
            while True:

                confirmacao = input(
                    "Deseja realmente descadastrar? (S/N): "
                ).strip().upper()

                if confirmacao in ("S", "N"):
                    break

                print(
                    "Resposta inválida. Digite S ou N."
                )

            if confirmacao == "S":

                diretor.excluir_pessoa(nome)

                print(
                    "Pessoa descadastrada com sucesso!"
                )

            else:
                print("Descadastro cancelado.")

        # OPÇÃO 3 - PRIMEIRO NOME
        elif opcao == "3":

            pessoa = diretor.primeiro_nome()

            if pessoa is None:

                print(
                    "Não existem pessoas cadastradas."
                )

            else:

                print(
                    "\nPrimeira pessoa em ordem alfabética:"
                )

                print(pessoa)

        # OPÇÃO 4 - ÚLTIMO NOME
        elif opcao == "4":

            pessoa = diretor.ultimo_nome()

            if pessoa is None:

                print(
                    "Não existem pessoas cadastradas."
                )

            else:

                print(
                    "\nÚltima pessoa em ordem alfabética:"
                )

                print(pessoa)

        # OPÇÃO 5 - FINALIZAR
        elif opcao == "5":

            print(
                "\nOperações do diretor finalizadas."
            )

            break

        # OPÇÃO INVÁLIDA
        else:

            print(
                "Opção inválida! Digite um número de 1 a 5."
            )

    return diretor


# Etapa 3 - Menu do Assistente
def executar_assistente(assistente):

    print("\n===== BEM-VINDO(A), ASSISTENTE! =====")

    while True:

        print("\n===== MENU DO ASSISTENTE =====")
        print("1 - Menor distância até uma pessoa cadastrada")
        print("2 - Menor distância passando por Indaiatuba")
        print("3 - Cidade mais próxima com moradores cadastrados")
        print("4 - Finalizar operações")

        opcao = input("\nEscolha uma opção: ").strip()

        # OPÇÃO 1 - MENOR DISTÂNCIA
        if opcao == "1":

            nome = input(
                "Nome da pessoa: "
            ).strip()

            pessoa, distancia, caminho = (
                assistente.menor_distancia_para_pessoa(nome)
            )

            if pessoa is None:

                print("Pessoa não encontrada.")
                continue

            print("\nDados da pessoa:")
            print(pessoa)

            if distancia is None:

                print(
                    "Não existe um caminho disponível."
                )

                continue

            print("\nMenor caminho:")
            print(" -> ".join(caminho))

            print(
                f"Distância total: {distancia} km"
            )

        # OPÇÃO 2 - CAMINHO VIA INDAIATUBA
        elif opcao == "2":

            nome = input(
                "Nome da pessoa: "
            ).strip()

            pessoa, distancia, caminho = (
                assistente.menor_distancia_via_indaiatuba(nome)
            )

            if pessoa is None:

                print("Pessoa não encontrada.")
                continue

            print("\nDados da pessoa:")
            print(pessoa)

            if distancia is None:

                print(
                    "Não existe um caminho disponível."
                )

                continue

            print(
                "\nMenor caminho passando por Indaiatuba:"
            )

            print(" -> ".join(caminho))

            print(
                f"Distância total: {distancia} km"
            )

        # OPÇÃO 3 - CIDADE MAIS PRÓXIMA
        elif opcao == "3":

            cidade, distancia, moradores = (
                assistente.cidade_mais_proxima_com_moradores()
            )

            if cidade is None:

                print(
                    "Não existem moradores cadastrados "
                    "em cidades alcançáveis."
                )

                continue

            print(
                "\nCidade mais próxima com moradores:"
            )

            print(f"Cidade: {cidade}")
            print(f"Distância: {distancia} km")

            print("\nMoradores cadastrados:")

            for pessoa in moradores:

                print("\n--------------------------")
                print(pessoa)

        # OPÇÃO 4 - FINALIZAR
        elif opcao == "4":

            print(
                "\nOperações do assistente finalizadas."
            )

            print(
                "Sistema encerrado com sucesso!"
            )

            break

        # OPÇÃO INVÁLIDA
        else:

            print(
                "Opção inválida! Digite um número de 1 a 4."
            )

    return assistente


# Função principal - Integração dos três perfis
def executar():

    # ETAPA 1 - SECRETÁRIO
    secretario = AtribuicoesSecretario()

    executar_secretario(secretario)

    # ETAPA 2 - DIRETOR
    # Converter a lista encadeada em árvore binária

    diretor = AtribuicoesDiretor(
        secretario.obter_cadastros_para_transicao()
    )

    executar_diretor(diretor)

    # ETAPA 3 - ASSISTENTE
    # Utilizar os cadastros atualizados pelo diretor

    assistente = AtribuicoesAssistente(diretor)

    executar_assistente(assistente)


# Inicialização do programa
if __name__ == "__main__":
    executar()