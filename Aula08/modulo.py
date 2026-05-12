import os

def main():
     while True:
        print('Calculadora')
        print('1. Soma')
        print('2. Subtrair')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Limpar terminal')
        print('0. Sair')

#match-case é melhor que if-elif nesse caso porque vai direto na opção desejada (ideal para menus).
        opcao=input('Digite a opção desejada: ')
        match opcao:
            case "1":
                print('-----SOMA-----')
                num1=int(input('Digite um número para somar: '))
                num2=int(input('Digite outro número para somar: '))
                result = soma(num1,num2)
                print(f'Resultado: {result}')
                break
            case "2":
                print('-----SUBTRAÇÃO-----')
                num1=int(input('Digite um número para subtrair: '))
                num2=int(input('Digite outro número para subtrair: '))
                result = sub(num1,num2)
                print(f'Resultado: {result}')
                break
            case "3":
                print('-----MULTIPLICAÇÃO-----')
                num1=int(input('Digite um número para multiplicar: '))
                num2=int(input('Digite outro número para multiplicar: '))
                result = multiplicacao(num1,num2)
                print(f'Resultado: {result}')
                break
            case "4":
                print('-----DIVISÃO-----')
                num1=int(input('Digite um número para divisão: '))
                num2=int(input('Digite outro número para divisão: '))
                result = divisao(num1,num2)
                print(f'Resultado: {result}')
                break
            case "5":
                limpa_terminal

            case '0':
                break

            case _:
                print('Opção inválida!')
            

def soma(a,b):
    return a+b

def sub(a,b):
    return a -b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a/b

def limpa_terminal():
    os.system('cls' if os.name == 'nt' 'clear' else 'clear')