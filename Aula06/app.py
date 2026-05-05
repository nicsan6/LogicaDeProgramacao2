'''
[] -> Lista
{} -> Dicionário
() -> Tupla
Orientação a objeto (POO)
"Profissão":{ "1": Professor / "2": Dev / "3": Profissional}
Pessoa = {"nome": Gomes / "Idade": 27 / "Profissão": Prof}
'''
lista = ['gomes', 'fulano', 'ciclano', 'beltrano', 'maria', 'pedro']

#imprimindo um valor específico
print(lista[0])

#imprimindo último índice
print(lista[-1])

#imprimindo um intervalo
print(lista[2:4])

#ordenar a lista
lista.sort()

#adicionando a lista
lista.append('karyton')

#inserindo em posições específicas (insert recebe dois parâmetros, a posição que você quer inserir e o valor a ser inserido)
lista.insert(2,'joão')

#inseridno vários valores
lista.extend(["ana", "beatriz", "roberto", "david",])

numeros = []
#adicionando valores de forma dinamica
for i in range(10):
    numeros.append(i*2)
print(numeros)

#removendo item da lista
print(f'Lista antes de remover {lista}')

#pop - remove pelo índice
lista.pop(0)

#removendo o último índice
lista.pop()

#removendo pelo valor(se tiver dois valores iguais, ele exclui o primeiro que achar)
lista.remove('ciclano')

#removendo intervalo de valores
lista_numeros = [n for n in range(11)]

#removendo intervalo de valores 
print(f'Lista antes de remover {lista_numeros}')
del lista_numeros[2:4]

print(f'Lista depois de remover {lista_numeros}')

lista_nomes = ['gomes', 'fulano', 'cicrano','beltrano','maria','pedro']
#alterando valor da lista 
lista_nomes[1] = 'lucas'

print(lista_nomes)

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    if numeros[i] > 5:
        numeros[i] = numeros[i] * 2
print(numeros)

numeros2 = [10,20,30,40,50]

#list comprehesion
numeros2 = [n * 2 if n>20 else n for n in numeros2]
print(numeros2)
# for i in range(len(lista)):
#     print(f'{i+1}º valor da lista: {lista[i]}')