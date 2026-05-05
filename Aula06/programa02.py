'''
Desenvolva um sistema de gerenciamneto de carros com realização do CRUD
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
        preco = float(input('Digite o preço do carro: '))
        marca = input("Digite a marca: ").title()

        carro = {
            "id": proximo_id,
            "modelo": modelo,
            "preço": preco,
            "marca": marca
        }

        carros.append(carro)
        proximo_id += 1

        print("✅Carro cadastro com sucesso!")

    #read
    elif opcao == '2':
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
                novo_preco = float(input("Digite o novo preço: ").replace(',', '.'))
                novo_marca = input("Digite a nova marca: ").title()

                carro['modelo'] = novo_modelo
                carro['preco'] = novo_preco
                carro['marca'] = novo_marca

                print('✅Carro atualizado com sucesso!')
                econtrado = True
                break

        if not econtrado:
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