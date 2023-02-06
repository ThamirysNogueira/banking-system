def menu():

    menu='''\n

============= MENU =============

Selecione a opção desejada:

[d]  Depositar
[s]  Sacar
[e]  Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas

[q]  Sair

>>> '''

    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor

        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito realizado com sucesso.")
            
    else:
        print("Operação falhou. O valor informado é inválido.")  

    return saldo, extrato 


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite    
    excedeu_saques = numero_saques >= limite_saques     

    if excedeu_saldo:
        print("\nSaldo insuficiente para o valor do saque.")    

    elif excedeu_limite:
        print("\nFalha na operação. Limite do saque é de R$ 500.")

    elif excedeu_saques:
        print("\nOperação falhou. Você atingiu o limite diário de saques.")


    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque realizado com sucesso.")

    else:
        print("Operação falhou. O valor informado é inválido.")

    return saldo, extrato
             

def exibir_extrato(saldo, /, *, extrato):
    print("\n============== EXTRATO ==============")
    print("Não foram realizadas movimentações. " if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("======================================")

def criar_usuario(usuarios):
    cpf = input("Digite o número do CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com o CPF informado. ")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd--mm--aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

    print("\nUsuário criado com sucesso. ")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso. ")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}

    print("Usuário não encontrado. Fluxo de criação de conta encerrado. Por favor, cadastre o usuário antes de criar a conta. ")
    return None    


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Titular:\t{conta['usuario']['nome']}
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}            
        """

        print("=" * 100)
        print(linha)


def main():
    
    AGENCIA = "0001"
    LIMITE_SAQUES = 3


    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:

        opcao = menu()

        if opcao == "d":
            valor = (float(input("Informe o valor que deseja depositar: R$ " )))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor que deseja sacar: R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            

        elif opcao == "nu":
         criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo da conta...")
            break
        
        else:
            print("Opção inválida. Por favor, selecione novamente a operação desejada.")
                

main()