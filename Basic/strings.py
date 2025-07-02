
#Metodos de strings

# strip, lstrip, rstrip

curso = 'Curso de Python'
curso_Espaco = '   Curso de Python   '
print(curso_Espaco.strip())
print(curso_Espaco.lstrip())
print(curso_Espaco.rstrip())

print(curso_Espaco.center(20,'*'))

print(curso.lower())
print(curso.upper())
print(curso.title())
print(curso.capitalize())

#Concatenação de strings


nome, idade, profissao, cidade = 'João', 30, 'Engenheiro', 'São Paulo'

print(f'O nome dele é {nome}, ele tem {idade} anos, trabalho como {profissao} e mora em {cidade}')

print('O nome dele é {}, ele tem {} anos, trabalho como {} e mora em {}'.format(nome, idade, profissao, cidade))

print(f''' tste 
      a
      b
      c
      a
      d
      ''')
# fatiamento de strings

fat = 'Curso de Python'

print(fat[0])
print(fat[0:5])  # do 0 ao 5
print(fat[6:])   # do 6 ao final
print(fat[-1])   # último caractere

curso = "Python" 
print(curso[::-1]) 