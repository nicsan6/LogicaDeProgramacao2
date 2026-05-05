"""
Cálculos e manipulações de variáveis
"""
nome = input("Digite o seu nome:")
idade = input("Digite a sua idade:")
peso = input("Digite o seu peso:")
altura = input("Digite a sua altura:")

#tratamento de exceção
try:
    idade = int(idade)
    peso = float(peso)
    altura = float(altura)
except ValueError as e:
    print(e)

idade = int(idade)

imc = peso / altura**altura

print("Seu IMC é: ",imc)