import os

# Variáveis globais do projeto:


restaurantes = ["Laçador", "Pedra Chata"]


def sair():
    os.system("cls")
    print("Finalizando aplicação.\n")


def voltar():
    input("Digite qualquer tecla para retornar ao menu principal: ")
    main()


def opcao_invalida():
    print("Opção Inválida\n")
    voltar()


def chama_nome_app():
    print("Programa Expresso")


def exibir_opcoes():
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")

# Funcionalidades das opções:


def cadastrar_novo_restaurante():
    os.system("cls")
    nome_do_restaurante = input("Digite o nome do seu novo restaurante: \n")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar()


def listar_restaurantes():
    os.system("cls")
    print("Listando os restaurantes\n")
    for restaurante in restaurantes:
        print(f"- {restaurante}")
    voltar()
# Escolha das opções:


def escolha_opcoes():
    try:
        opcao_digitada = int(input("Selecione uma opção:\n"))
        print("\nVocê escolheu a opção:", opcao_digitada)
        match opcao_digitada:
            case 1:
                print("Você escolheu cadastrar seu restaurante.")
                cadastrar_novo_restaurante()
            case 2:
                print("Você escolheu listar seu restaurante.")
                listar_restaurantes()
            case 3:
                print("Você escolheu ativar seu restaurante.")
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
