'''
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
 #operador ternário
result = "num 1 é maior" if num1 > num2 else "num2 é maior"
print(result)
'''
nome1 = input("Digite o primeiro nome completo: ")
nome2 = input("Digite o segundo nome completo: ")

# separando o nome do sobrenome
parte1 = nome1.split()
parte2 = nome2.split()

# pegar o primeiro nome e sobrenome
primeiro_nome1 = parte1[0]
sobrenome1 = parte1[-1]

primeiro_nome2 = parte2[0]
sobrenome2 = parte2[-1]

novo_nome1 = primeiro_nome1 +' '+ sobrenome2
novo_nome2 = primeiro_nome2 +' '+ sobrenome1

print(novo_nome1)
print(novo_nome2)
