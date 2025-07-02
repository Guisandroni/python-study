'''
# uso de if e else
saldo = 2000
saque = float(input('Digite o valor do saque: '))


if saldo >= saque:
    print('saque realizado')
else: 
    print('saldo insuficiente')
'''

# repeat

"""a = 1
for a in range ( 1,5):
    a += a
    print(a)
"""

enter = 1

while enter != 0: 
    enter = int(input('Digite 1 para sair e 2 para continuar'))

    if enter ==1:
        print('Saindo...')
    elif enter == 2:
        print('Continuando...')
    else:
        print('Opção inválida, tente novamente.')
        enter = 1

