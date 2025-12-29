'''
Crie um programa que simule o funcionamento de uma carteira digital.
O usuário começa com um saldo inicial fictício e pode realizar as seguintes operações através de um menu que se repete:

1 - Ver saldo
2 - Adicionar saldo
3 - Realizar pagamento
4 - Encerrar


Regras:

-O menu deve aparecer repetidamente até o usuário escolher a opção 4
-Não permitir pagamento com valor maior que o saldo
-Valores negativos ou zero não devem ser aceitos
-O saldo deve ser atualizado corretamente após cada operação
-Mostrar mensagens claras para o usuário'''


def mostrar_menu():
    print("\n:=:=:=- CARTEIRA DIGITAL -=:=:=:\n")
    print("1 - Ver saldo")
    print("2 - Adicionar saldo")
    print("3 - Realizar pagamento")
    print("4 - Encerrar")


def ver_saldo(saldo):
    print(f"\nSeu saldo atual é de R${saldo}\n")


def adicionar_saldo(saldo):
    valor = input("\nDigite o valor que deseja depositar: ")

    if valor.strip() == "":
        print("\nErro, o campo não pode estar vazio.\n")
        return saldo

    try:
        valor = int(valor)

        if valor <= 0:
            print("\nErro, digite um valor maior que zero.\n")
        else:
            saldo += valor
            print("\nDepósito realizado com sucesso!\n")

    except ValueError:
        print("\nErro, digite apenas números.\n")

    return saldo


def realizar_pagamento(saldo):
    valor = input("\nDigite o valor que deseja pagar: ")

    if valor.strip() == "":
        print("\nErro, o campo não pode estar vazio.\n")
        return saldo

    try:
        valor = int(valor)

        if valor <= 0:
            print("\nErro, digite um valor maior que zero.\n")

        elif valor > saldo:
            print("\nErro, saldo insuficiente.\n")

        else:
            saldo -= valor
            print("\nPagamento realizado com sucesso!\n")

    except ValueError:
        print("\nErro, digite apenas números.\n")

    return saldo


def main():
    saldo = 200

    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção (1-4): ")

        if opcao == "1":
            ver_saldo(saldo)

        elif opcao == "2":
            saldo = adicionar_saldo(saldo)

        elif opcao == "3":
            saldo = realizar_pagamento(saldo)

        elif opcao == "4":
            print("\nEncerrando o programa. Até mais!\n")
            break

        else:
            print("\nErro, opção inválida.\n")


if __name__ == "__main__":
    main()