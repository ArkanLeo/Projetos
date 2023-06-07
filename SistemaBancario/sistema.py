

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == 'd':
        vdepos = float(input("Digite o valor do depósito: "))
        if vdepos > 0:
            saldo += vdepos
            extrato += f"Depósito: R${vdepos:.2f} realizado com sucesso.\n"
            print(f"Depósito: R${vdepos:.2f} realizado com sucesso.\n")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 's':
        vsaq = float(input("Digite o valor para saque: "))

        if vsaq > 0:
                excedeu_saldo = 500
                if LIMITE_SAQUES == 0:
                    print("Limite de saques diário excedido.")

                elif vsaq > excedeu_saldo:
                    print("Operação falhou! Valor de saque excedido.")

                elif vsaq <= saldo:
                    saldo -= vsaq
                    extrato += f"Saque: R${vsaq:.2f} realizado com sucesso.\n"
                    print(f"Saque: R${vsaq:.2f} realizado com sucesso.\n")
                    LIMITE_SAQUES -= 1

                elif vsaq > saldo:
                    print("Operação falhou! Valor de saque maior que saldo disponível.")

                else:
                    print("Operação falhou! Tente novamente.")
        else:
            print("Operação falhou! Tente novamente.")

    elif opcao == 'e':
        print("*"*15 + "Extrato" + "*"*15)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n\nSaldo disponível de R${saldo:.2f}.")
        print("*"*37)

    elif opcao == 'q':
        print("Muito obrigado(a)! Volte sempre ;)")
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")
