'''
conta bancara
possivel depositar valores positivos e negativos 
apenas um usuario
depositos armazenados em uma variavel
serem exibidos no texto, extrato do banco
3 saques diarios
limite 500 por saque
sem saldo informar mensagem
numero de operacoes realizadas e tipo

'''

opcao = '''
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(opcao)

    if opcao == '1':
        print('Deposito')
        valor = float(input('Digite o valor do depósito: '))
        if valor <= 0:
            print(f'Operacao falhou, nao e possivel depositar valores negativos ou iguais a zero')
        else:
            saldo += valor
            extrato += f'Deposito: R${valor} \n'
            print(f'Operacao realizada com sucesso! Saldo atual: R${saldo:.2f}')



    
    elif opcao == '2':
        print('Saque')
        valor = float(input('Digite o valor do saque: '))
     
        if valor > saldo:
            print(f'Operacao falhou, saldo insuficiente. Saldo atual: R${saldo:.2f}')
        elif valor > limite:
            print(f'Operacao falhou, valor do saque excede o limite de R${limite:.2f}')
        elif numero_saques >= LIMITE_SAQUES:
            print(f'Operacao falhou, numero maximo de saques diarios atingido: {LIMITE_SAQUES}')
        else:
            saldo -= valor
            extrato += f'Saque: R${valor} \n'
            numero_saques += 1
            print(f'Operacao realizada com sucesso! Saldo atual: R${saldo:.2f}')
    elif opcao == '3':
        print('Extrato')
        if not extrato:
            print('Nao foram realizadas movimentacoes.')
        else:
            print('Movimentacoes:')
            print(extrato)
    elif opcao == '4':
        print('Sair')
        break
    else:
        print('Opção inválida, tente novamente.')



