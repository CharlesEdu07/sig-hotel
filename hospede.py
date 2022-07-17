import os
import pickle

hospede = {}

def menu_hospede():
    os.system('cls')

    print("------------------------------")
    print("---------  Hóspedes  ---------")
    print("------------------------------")
    print('1 - Cadastrar hóspedes')
    print('2 - Atualizar hóspedes')
    print("3 - Consultar hóspedes")
    print("4 - Pesquisar hóspedes")
    print("5 - Deletar hóspedes")
    print("0 - Voltar")

    op = input("\nDigite a opção: ")

    return op

def hosp_write_file():  
    arq_hospede = open("hospede.dat", "wb")

    pickle.dump(hospede, arq_hospede)

    arq_hospede.close()
            
def hosp_load_file():
    ld_hospede = {}

    try:
        arq_hospede = open("hospede.dat", "rb")
        ld_hospede = pickle.load(arq_hospede)
        arq_hospede.close()

    except:
        arq_hospede = open("hospede.dat", "wb")
        arq_hospede.close()

    return ld_hospede

def hosp_create(data):
    if data["cpf"] not in hospede:
        hospede[data['cpf']] = {'nome': data['nome'], 'cpf': data['cpf'], 'email': data['email'], 'endereco': data['endereco'], 'telefone': data['telefone']}

        print('\nHóspede cadastrado com sucesso')
    else:
        print('\nHóspede já cadastrado')

def hosp_update(cpf):    
    if cpf in hospede:
        email = input("\nDigite o email: ")
        endereco = input("Digite o endereco: ")
        telefone = input("Digite o telefone: ")
        
        hospede[cpf]['email'] = email
        hospede[cpf]['endereco'] = endereco
        hospede[cpf]['telefone'] = telefone 
            
        print('\nHóspede atualizado com sucesso')

    else:
        print('\nHóspede não encontrado')

def hosp_read():
    print()
    print("---------------------------------------")
    print("-------- Relatório de Hóspedes --------")
    print("---------------------------------------")
    
    for key, value in hospede.items():
        print("\nNome: ", value['nome'],
            "\nCPF: ", value['cpf'],
            "\nTelefone: ", value['telefone'],
            "\nEmail: ", value['email'],
            "\nEndereço: ", value['endereco'])

def hosp_search():
    cpf = input('\nDigite o CPF do Hóspede (Se não souber, tecle ENTER): ')
    name = input('Digite o nome do Hóspede: ')

    for key, value in hospede.items():
        if key == cpf or value['nome'] == name:
            print("Nome: ", value['nome'], "\tCPF: ", value['cpf'], "\tTelefone: ", value['telefone'], "\tEmail: ", value['email'], "\tEndereço: ", value['endereco'])
            return

    print('\nHóspede não encontrado')

def hosp_delete(cpf):
    if cpf in hospede:
        del hospede[cpf]

        print('\nHóspede deletado com sucesso')

    else:
        print('\nHóspede não encontrado')

def hosp_read_data():
    nome = input("\nDigite o nome do hospede: ")
    cpf = input("Digite o CPF do hospede: ")
    email = input("Digite o email do hospede: ")
    endereco = input("Digite o endereco do hospede: ")
    telefone = input("Digite o telefone do hospede: ")

    data = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "endereco": endereco,
        "telefone": telefone
    }

    hosp_create(data)

def modulo_hospede():
    op = menu_hospede()

    global hospede
    hospede = hosp_load_file()

    while op != '0':
        if op == '1':
            print("\nCADASTRO DE HÓSPEDES")

            hosp_read_data()

        elif op == '2':
            print("\nATUALIZAÇÃO DE HÓSPEDES")

            cpf = input("\nDigite o CPF do hospede: ")

            hosp_update(cpf)

        elif op == '3':
            print("\nCarregando relatório...")

            hosp_read()

        elif op == '4':
            hosp_search()
            
        elif op == '5':
            print("\nDELETAR HÓSPEDE")

            cpf = input('\nDigite o CPF do hospede: ')
            
            hosp_delete(cpf)

        else:
            print('\nSeleção inválida') 
        
        hosp_write_file()

        print()
        input('Tecle ENTER para continuar')

        
        op = menu_hospede()