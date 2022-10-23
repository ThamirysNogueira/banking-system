menu = '''

Selecione a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

>>> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = str((input(menu)))

    if opcao == "d":
        deposito = (float(input("Informe o valor que deseja depositar: R$ " )))

        if deposito > 0:
            saldo += deposito

            print(f"\nDepósito realizado. Seu saldo agora é R$ {saldo:.2f}")
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print("Operação falhou. O valor informado é inválido.")   


    elif opcao == "s":
        saque = float(input("Informe o valor que deseja sacar: R$ "))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nSaldo insuficiente para o valor do saque.")

        elif excedeu_limite:
            print("\nFalha na operação. Limite do saque é de R$ 500.")

        # corrigir aqui:
        elif excedeu_saques:
            print("\nVocê atingiu o limite diário de saques. Tente novamente outro dia.")


        elif saque > 0:
            saldo -= saque
            print(f"\nSaque realizado com sucesso. Seu saldo agora é R$ {saldo:.2f}")
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            

    elif opcao == "e":
        print("\n============== EXTRATO ==============")
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")

    elif opcao == "q":
        print("Saindo da conta...")
        break
    
    else:
        print("Opção inválida. Por favor, selecione novamente a operação desejada.")
             