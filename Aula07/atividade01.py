'''
    Desenvolva um sistema de gerenciamento de veículos, permita cadastrar o veículo pagando do usuário os seguintes dados (modelo, marca, preço)

        - os dados devem ser armazenados em um arquivo.
        - o usuário deve poder cadastrar quantos carros quiser sem ter que rodar o sistema novamente.
        - deve ter a opção de ler os carros existentes
        - devem ser cadastrados em um arquivo .txt e usar dicionário
'''
import os
import time
carros = []
proximo_id = 1

os.system('cls')
while True:
    print("\n===== Sistema de Carros 🚗 =====")
    print('1. - Cadastrar carro')
    print('2. - Listar carros')
    print('3. - Atualizar carro')
    print('4. - Deletar carro')
    
    opcao = input("Escolha uma opção: ")
    
    #criar
    if opcao == '1':
        modelo = input("Digite o modelo do carro: ").title()
        preco = input('Digite o preço do carro: ')
        marca = input("Digite a marca: ").title()

        carro = {
            "id": proximo_id,
            "modelo": modelo,
            "preço": preco,
            "marca": marca
        }

    with open('carros.txt', 'w') as arquivo:
        arquivo.write(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')
       

        proximo_id += 1

        print("✅Carro cadastro com sucesso!")
        




#read
    if opcao == '2':
        if not carros:
            print('⚠️Nenhum carro cadastrado.')
        else:
            print('\n📋Lista de carros')
        for carro in carros:
            print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')
    #update 
    elif opcao == '3':
        print('\n📋Lista de carros')
        for carro in carros:
            print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')
        id_busca = int(input("Digite o ID do carro para editar: "))

        encontrado = False
        for carro in carros:
            if carro ['id'] == id_busca:
                novo_modelo = input("Digite o novo modelo: ").title()
                novo_preco = input("Digite o novo preço: ").replace(',', '.')
                novo_marca = input("Digite a nova marca: ").title()

                carro['modelo'] = novo_modelo
                carro['preco'] = novo_preco
                carro['marca'] = novo_marca

                with open('carros.txt', 'w') as arquivo:
                    arquivo.write(f'Modelo {novo_modelo['modelo']} | Preço {novo_preco['preco']} | Marca: {novo_marca['marca']}')

                print('✅Carro atualizado com sucesso!')
                econtrado = True
                break

        if not encontrado:
            print("❌O carro não foi encontrado!")

    #delete
    elif opcao == '4':
        print('\n📋Lista de carros')
        for carro in carros:
            print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')
        id_busca = int(input("Digite o ID do carro para deletar: "))

        #variável de controle (não precisa fazer um else n o acesso da lista)
        econtrado = False

        #acessando e percorrendo a lista para verificar 
        for carro in carros:
            if carro ['id'] == id_busca:
                carros.remove(carro)
                print('✅Carro deletado com sucesso!')
                econtrado = True
                break
        if not econtrado:
            print("❌O carro não foi encontrado!")
    #sair
    elif opcao == '0':
        total = 10
        barra = ""
        print('Saindo do sistema...')
        for i in range(total + 1):
            barra += "🟩"
            porcentagem = int((i / total *100)) 
            vazio = "-" * (total-1)
            print(f'\r[{barra}] {porcentagem}%')
        time.sleep(0.3)
        break
    else: print('❌Opção inválida.')
