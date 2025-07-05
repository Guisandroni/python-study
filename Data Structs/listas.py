feira = ['laranja','maça','banana','uva']
feira = [-1]
feira =[-3]
feiraSegunda = []

letras = list('python')

numbers = list(range(10))

automoveis = ['fusca', 'civic', 'gol', 'palio',4200, 5000, 6000, 7000, 8000, 9000, True]

#print (f'{feira,letras,numbers,automoveis}')

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz)


#fatiamento

listas = ['p','y', 't', 'h', 'o', 'n']

listas[2:]
listas[2:4]  # do 2 ao 4
listas[:3]   # do começo ao 3
listas[-1]   # último elemento
listas[-2:]  # do penúltimo ao final
listas[::-1] # inverte a lista

#iterando listas
for lista in listas:
    print(lista)

for lista, indice in enumerate(listas):
    print(f'Indice: {indice}, Valor: {lista}')



# metodos de listas

a