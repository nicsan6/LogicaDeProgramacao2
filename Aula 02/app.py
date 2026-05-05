""""
    TIPOS DE DADOS
"""

str()
int()
bool()
float()

nome = "Nicollas Sanches"
idade = 16
altura = 1.75
professor = True

# entrada de dados (usuário que passa informação)
novo_nome = input("Digite o seu nome: ")
print("Nome: ",nome)
print("Novo nome: ",novo_nome)

# variável com valor definido (pré-definida)
print("Nome:",nome)
print("Idade:",idade)
print("Altura:",altura)
print("É professor?",professor)

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
altura = input("Digite sua altura: ")
peso = input("Digite seu peso em kilogramas: ")
print("Olá",nome_teste,"seja bem-vindo ao sistema Python.")
print("Data de nascimento:",data_nascimento)
print("Sua altura:",altura)
print("Seu peso:",peso)
#input é, por padrão, do tipo string
print(type(nome))

