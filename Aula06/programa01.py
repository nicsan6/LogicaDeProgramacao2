'''
1. Crie um programa que o usuario possa digitar quantos numeros quiser e ao terminar imprima a lista em ordem crescente

2. Crie um programa que o usuario digitar a quantidade desejada de notas de um determinado aluno (nota minima 0 e nota maxima 10) 
e o programa calcula a media desse aluno e, ao final, imprime se o aluno está (aprovado >=7), reprovado (recuperação >=)
'''

#programa 01
import os
lista = []

while True:
    numeros = int(input("Digite um número: "))
    lista.append(numeros)
    opcao = input('Deseja continuar? (s - sim ou enter para parar!').lower()
    os.system('cls')
    if opcao != 's':
    
        break
lista.sort()
print(lista)

#programa 02
import os 
print(30*'-', 'Boletim Escolar', 30*'-')
lista_notas =[]
while True:
    nota = float(input("Digite a nota que desejar do aluno: "))
    lista_notas.append(nota)
    if 0 <= nota <= 10:
        lista_notas.append(nota)

    else:
        print("nota invalida")
        break

    opcao = input('Deseja continuar? (s - sim ou enter para parar!').lower()
    os.system('cls')
    if opcao != 's':
        break
    
if lista_notas:
    media = sum(lista_notas)/len(lista_notas)
    print(f"A média do aluno foi: {media}")
    if media >= 7:
        print("APROVADO")

    elif media >= 5:
        print('RECUPERAÇÃO')

    else:
        print('REPROVADO')

else:
    print("Nenhuma nota foi registrada")