menu="""

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """


saldo=0
limite=500
extrato=""
numero_saque=0
LIMITE_SAQUES=3


while True:
    opcao= input(menu)

    if opcao=="d":
        valor_deposito=float(input("Qual o valor que você deseja depositar?"))
        if valor_deposito>0:
            saldo+=valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao=="s":
        valor_saque=float(input("Qual o valor que você quer sacar?"))

        excedeu_saldo= valor_saque>saldo

        excedeu_limite= valor_saque>limite

        excedeu_saques= numero_saque>= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print(" Operação falhou! o valor do saque excede o limite!")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor_saque>0:
            saldo -=valor_saque
            extrato += f"Saque: R${valor_saque:.2f}\n"
            numero_saque +=1
        else:
            print("")



    elif opcao=="e":
        print("\n=================Extrato:================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("============================================")

    elif opcao=="q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada. ")




