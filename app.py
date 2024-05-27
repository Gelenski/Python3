import os

# Variáveis globais do projeto:


# //restaurantes = ["Laçador", "Pedra Chata"]
restaurantes = [
    {"nome": "Laçador", "categoria": "Churrascaria", "ativo": True},
    {"nome": "Pedra Chata", "categoria": "Buffet", "ativo": True},
    {"nome": "Veneza", "categoria": "Comida Italiana", "ativo": False}]


def chama_nome_app():
    """
    Função responsável por mostrar o nome da aplicação.

    outputs:
    - Mostra o nome da aplicação.
    """
    print("\n ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕠 LUCAS. \n")


def mostrar_subtitulo(t):
    """
    Função responsável por mostrar textos com ênfase na aplicação.

    inputs:
    - Texto que deseja dar ênfase.

    outputs:
    - Texto com ênfase
    """
    os.system("cls")
    linha = "*" * (len(t))
    print(linha)
    print(t)
    print(linha)
    print()


def sair():
    """
    Função responsável por finalizar a aplicação, limpando o terminal antes de finalizá-la.

    outputs:
    - Função mostrar_subtitulo() com o seguinte parâmetro: Finalizando aplicação.
    """
    os.system("cls")
    mostrar_subtitulo("Finalizando aplicação.")


def voltar_menu_principal():
    input("\n Pressione a tecla Enter para retornar ao menu principal: ")
    main()


def opcao_invalida():
    """
    Função responsável por responder caso o usuário digite uma opção inválida.

    outputs:
    - Mostra o texto: Opção Inválida. Em seguida retorna a função voltar_menu_principal().
    """
    print("Opção Inválida.\n")
    voltar_menu_principal()


def exibir_opcoes():
    """
    Função responsável por mostrar as opções responsáveis por dar continuidade na aplicação.

    outputs:
    - Mostra as opções que dão continuidade no programa.
    """
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar/Desativar restaurante")
    print("4 - Sair\n")


# Funcionalidades das opções:

def cadastrar_novo_restaurantes():
    """
    Função responsável por cadastrar novos restaurantes.

    inputs:
    - Nome do restaurante;
    - Categoria do restaurante.

    outputs:
    - Adiciona o novo restaurante recém cadastrado ao dicionário.
    """

    os.system("cls")
    nome_do_restaurante = input("Digite o nome do seu novo restaurante: \n")
    categoria = input(f"Digite a categoria do restaurante {
                      nome_do_restaurante}: \n")
    dados_restaurante = {"nome": nome_do_restaurante,
                         "categoria": categoria, "ativo": False}
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_menu_principal()


def listar_restaurantes():
    """
    Função responsável por listar as informações dos restaurantes como nome, categoria e estado.
    inputs:
    - Dicionário de restaurantes.

    outputs:
    - Mostra em forma de tabela os restaurantes com suas respectivas informações. Após isso retorna a função voltar_menu_principal().
    """
    os.system("cls")
    mostrar_subtitulo("Listando os restaurantes")
    print(f"{'*Nome do Restaurante*'.ljust(22)
             } | {'*Categoria*'.ljust(22)} | {'*Status*'.ljust(20)}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f"- {nome_restaurante.ljust(20)
                   } | {categoria_restaurante.ljust(22)} | {ativo}")
    voltar_menu_principal()


def alterar_estado_restaurantes():
    """
    Função responsável por alterar o estado(status) do restaurante, se ativo para desativado e vice versa.

    inputs:
    - Nome do restaurante que se deseja alterar o estado.

    outputs:
    - Altera o estado do respectivo restaurante.
    - Ou se caso não encontre o restaurante mostra: O restaurante não foi encontrado. Em seguida retorna a função voltar_menu_principal().
    """
    mostrar_subtitulo("Alterando o estado do restaurante")
    nome_restaurante = input(
        "Digite o nome do restaurante que deseja alterar o estado: \n")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso! " if restaurante["ativo"] else f"O restaurante {
                nome_restaurante} foi desativado com sucesso!"
            print(mensagem)
    if not restaurante_encontrado:
        print(f"O restaurante não foi encontrado.")

    voltar_menu_principal()


# Escolha das opções:

def escolha_opcoes():
    """
    Função responsável por definir a chamada das funções respectivas a escolha definida.

    inputs:
    - Número referente a opção que o usuário deseja escolher.

    outputs:
    - Caso a opção esteja certa retorna: Você escolheu a opção: opção_digitada e a função respectiva a opção escolhida;
    - Caso não retorna a função opçao_invalida().
    """
    try:
        opcao_digitada = int(input("Selecione uma opção:\n"))
        print("\nVocê escolheu a opção:", opcao_digitada)
    #     match opcao_digitada:
    #         case 1:
    #             cadastrar_novo_restaurantes()
    #         case 2:
    #             listar_restaurantes()
    #         case 3:
    #             # //print("Você escolheu ativar seu restaurante.")
    #             alterar_estado_restaurantes()
    #         case 4:
    #             sair()
    #         case _:
    #             opcao_invalida()
    # except:
    #     opcao_invalida()
        if opcao_digitada == 1:
            cadastrar_novo_restaurantes()
        elif opcao_digitada == 2:
            listar_restaurantes()
        elif opcao_digitada == 3:
            alterar_estado_restaurantes()
        elif opcao_digitada == 4:
            sair()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    """
    Função responsável por ordenar a execução da aplicação;

    outputs:
    - Retorna as funções na ordem:
        chama_nome_app()
        exibir_opcoes()
        escolha_opcoes()
    """
    os.system("cls")
    chama_nome_app()
    exibir_opcoes()
    escolha_opcoes()


if __name__ == "__main__":
    main()
