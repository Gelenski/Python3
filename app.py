import os

# Variáveis globais do projeto:


# //restaurantes = ["Laçador", "Pedra Chata"]
restaurantes = [
    {"nome": "Laçador", "categoria": "Churrascaria", "ativo": True},
    {"nome": "Pedra Chata", "categoria": "Buffet", "ativo": True},
    {"nome": "Veneza", "categoria": "Comida Italiana", "ativo": False}]


def chama_nome_app():
    print("\n ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕠. \n")


def mostrar_subtitulo(t):
    os.system("cls")
    print(t)
    print()


def sair():
    os.system("cls")
    mostrar_subtitulo("Finalizando aplicação.\n")


def voltar_menu_principal():
    input("\n Pressione a tecla Enter para retornar ao menu principal: ")
    main()


def opcao_invalida():
    print("Opção Inválida\n")
    voltar_menu_principal()


def exibir_opcoes():
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")


# Funcionalidades das opções:

def cadastrar_novo_restaurantes():
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
    os.system("cls")
    mostrar_subtitulo("Listando os restaurantes")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f"- {nome_restaurante} | {categoria_restaurante} | {ativo}")
    voltar_menu_principal()


def alterar_estado_restaurantes():
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
    try:
        opcao_digitada = int(input("Selecione uma opção:\n"))
        print("\nVocê escolheu a opção:", opcao_digitada)
        match opcao_digitada:
            case 1:
                cadastrar_novo_restaurantes()
            case 2:
                listar_restaurantes()
            case 3:
                # //print("Você escolheu ativar seu restaurante.")
                alterar_estado_restaurantes()
            case 4:
                sair()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("cls")
    chama_nome_app()
    exibir_opcoes()
    escolha_opcoes()


if __name__ == "__main__":
    main()
