saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(saldo_atual, extrato_atual):

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo_atual += valor
        extrato_atual += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo_atual, extrato_atual


def saque(saldo_atual, extrato_atual, valor_limite, limite_saques, saques):

    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo_atual

    excedeu_limite = valor > valor_limite

    excedeu_saques = saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo_atual -= valor
        extrato_atual += f"Saque: R$ {valor:.2f}\n"
        saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo_atual, extrato_atual, saques

def ver_extrato(saldo_atual, extrato_atual):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_atual else extrato_atual)
    print(f"\nSaldo: R$ {saldo_atual:.2f}")
    print("==========================================")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:

    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == "s":
        saldo, extrato,numero_saques = saque(saldo, extrato, limite, LIMITE_SAQUES, numero_saques)

    elif opcao == "e":
        ver_extrato(saldo, extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")