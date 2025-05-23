menu = f"""\n
      BEM VINDO AO BANCO-CNAB
    ---------------------------
    Selecione a opção desejada!
    ---------------------------

    1 - Depósito
    2 - Sacar
    3 - Extrato
    4 - Sair

    ---------------------------
    """
#Desenvolvido por okrhuan

Saldo = 0
Limite = 500
Extrato = ""
max_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            Saldo += valor
            Extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > Saldo

        excedeu_limite = valor > Limite

        excedeu_saques = max_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Falha! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Falha! Número máximo de saques excedido.")

        elif valor > 0:
            Saldo -= valor
            Extrato += f"Saque: R$ {valor:.2f}\n"
            max_saques += 1

        else:
            print("Falha! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print()
        print("Não foram realizadas movimentações." if not Extrato else Extrato)
        print(f"\nSaldo: R$ {Saldo:.2f}")
        print()
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")