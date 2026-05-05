"""
Desenvolva um sistema que receba do usuário 
seu nome, data de nascimento, peso e altura.
Formate a saída para aparecer na tela so usuário:
Olá {nome_informado}, seja bem-vindo ao sistema Python 
Aqui está suas informações:
    Data nascimento: 
    Altura:
    Peso: 
"""
nome_teste = input("Digite seu nome: ")
data_nascimento = input("Digite sua data de nascimento: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso em kilogramas: "))

print("Olá",nome_teste,"seja bem-vindo ao sistema Python.")
print("Data de nascimento:",data_nascimento)
print("Sua altura:",altura)
print("Seu peso:",peso)

