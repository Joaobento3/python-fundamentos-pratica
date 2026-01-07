'''
Criar um programa em Python que simule um sistema simples de cadastro de usuários, executado no terminal, utilizando menu interativo e estruturas básicas da linguagem.

opcões:
    Cadastrar usuário
    Listar usuários
    Buscar usuário pelo nome
    Remover usuário
    Sair
'''


def mostrar_menu():
    print("\n\n----- MENU DO USUÁRIO -----\n")
    print("1- Cadastrar usuário")
    print("2- Listar usuários")
    print("3- Buscar usuário pelo nome")
    print("4- Remover usuário")
    print("5- Sair\n")


def cadastrar_usuario(usuarios):
    nome = input("\nDigite o nome do usuário: ")
    idade = input("Digite a idade do usuário: ")
    curso = input("Informe qual o seu curso: ")


    if nome.strip() == "":
        print("\nErro, o campo não pode estar vazio.\n")
        return

    if idade.strip() == "":
        print("\nErro, o campo não pode estar vazio.\n")
        return

    if curso.strip() == "":
        print("\nErro o campo não pode estar vazio.\n")
        return

    try:
        idade = int(idade)

        if idade <= 0:
            print("\nErro, idade não pode ser menor ou igual a zero.\n")
            return

    except ValueError:
        print("\nResposta inválida.\n")
        return

    
    else:
        usuarios.append(
            {"Nome": nome, "Idade": idade, "Curso": curso}
            )
        print("\nUsuário cadastrado com sucesso!\n")


def listar_usuario(usuarios):
    if not usuarios:
        print("\nNenhum usuário cadastrado ainda.\n")
        return
    

    for usuario in usuarios:
        print("Nome:", usuario["Nome"])
        print("Idade:", usuario["Idade"])
        print("Curso:", usuario["Curso"])
        print("-" * 20)


def buscar_por_nome(usuarios):
    nome = input("\nDigite o nome do usuário: ").strip()

    if not usuarios:
        print("\nNenhum usuário cadastrado ainda.\n")
        return

    if nome == "":
        print("\nErro, o campo não pode estar vazio.\n")
        return
    
    encontrado = False
    
    
    for usuario in usuarios:
        if usuario["Nome"].lower() == nome.lower():
            print("\nUsuário encontrado:\n")
            print("-" * 20)
            print("Nome:", usuario["Nome"])
            print("Idade:", usuario["Idade"])
            print("Curso:", usuario["Curso"])
            print("-" * 20)
            encontrado = True
        
        if not encontrado:
            print("\nErro, usuário não encontrado.\n")


def remover_usuario(usuarios):
    nome = input("\nDigite o nome do usuário que deseja remover: ").strip()

    if not usuarios:
        print("\nNenhum usuário cadastrado ainda.\n")
        return

    if nome == "":
        print("\nErro, o campo não pode estar vazio.\n")
        return
    
    encontrado = False

    for usuario in usuarios:
        if usuario["Nome"].lower() == nome.lower():
            usuarios.remove(usuario)
            print("\nUsuário removido com sucesso!\n")
            encontrado = True
            return
        
    if not encontrado:
        print("\nErro, usuário não encontrado.\n")




def main():
    usuarios = []

    while True:
        mostrar_menu()
        opcao = input("\nDigite a opção que deseja (1-5): ")

        if opcao.strip() == "":
            print("Erro, campo vazio.")
            continue

        if opcao == "1":
            cadastrar_usuario(usuarios)

        elif opcao == "2":
            print("\n\n")
            print("-" * 20)
            listar_usuario(usuarios)

        elif opcao == "3":
            buscar_por_nome(usuarios)

        elif opcao == "4":
            remover_usuario(usuarios)

        elif opcao == "5":
            print("\nEncerrando o programa.\n")
            break

        else:
            print("\nErro, opcão inválida.\n")



if __name__ == "__main__":
    main()