'''
função - variáveis de uma função são parâmetros. Função tem que ter parênteses.
Exemplo: print('coloque os parâmetros')
Em POO, nomeclatura Pascal Case ou Capital Case.
Para funções e variáveis em Python, utiliza-se snake case ou undescore case.
'''
import os
#função com parâmetro
def funcao_segundo_grau(a, b, c):
    print("Olá, Mundo!")
    return a,b,c

#chamando a função e armazenando o valor em variável
# x = funcao_segundo_grau(1,2,3)
# print(x)

# def soma(a,b):
#     resultado = a + b
#     return a + b
# resultado = soma(10, 10)
# print(resultado)

# def soma(a,b):
#     resultado = a + b
#     return resultado
# num1=float(input("Digite um número qualquer: "))
# num2=float(input("Digite um número qualquer: "))
# result = soma(num1,num2)
# print (result)

# def mostrar_msg():
#     print('Olá, mundo das funções!')

# def mostrar_saudacao(nome):
#     print(f'Olá {nome}, seja bem-vindo!')

# mostrar_saudacao('Nic')

#função recursiva
def fatorial(n):
    #n!
    return 1 if n == 0 else n * fatorial(n-1)

lista_fatorial = [7,6,5,4,3,2,1]
print(7 * 6 * 5 * 4 * 3 * 2 * 1)

# funções lambda
somar = lambda x, y: x+y
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

# algoritmo principal
if "__name__" == "__main__":
    try:
        x = int(input('Informe o valor de x: '))
        y = int(input('Informe o valor de x: '))
        result = somar (x,y)

        limpar()
        print(f'O resultado da soma é: {result}.')
    except Exception as e:
        print(f'Não foi possível somar. {e}.')

        








