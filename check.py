import os
import pickle
from hospede import hosp_read
from reserva import res_read, reservas, res_load_file
from datetime import datetime

def menu_check():
    os.system('cls')

    print("------------------------------------------")
    print("---------  Check-in e Check-Out  ---------")
    print("------------------------------------------")
    print("1 - Check-in")
    print("2 - Check-out")
    print("0 - Voltar")

    op = input("\nDigite a opção: ")

    return op

def res_write_file():
    arq_reserva = open("reserva.dat", "wb")

    pickle.dump(reservas, arq_reserva)

    arq_reserva.close()

def check_in(apt):
    if reservas[apt]['is_ocupado'] == 'vazio':
        data_entrada = datetime.now()
        data_entrada = data_entrada.strftime("%d/%m/%Y")

        reservas[apt] = {
            **reservas[apt],
            'data_entrada': data_entrada,
            'is_ocupado': 'sim'
        }

        print("\nCheck-in feito com sucesso. O quarto está agora ocupado")

    else:
        print("\nQuarto ocupado")

def check_out(apt):
    if  reservas[apt]['is_ocupado'] == 'sim':
        data_saida = datetime.now()
        data_saida = data_saida.strftime("%d/%m/%Y")

        reservas[apt].update({'data_saida': data_saida})
        reservas[apt]['is_ocupado'] = 'nao'

        d1_aux = (reservas[apt]['data_saida'])
        d2_aux = (reservas[apt]['data_entrada'])

        d1 = datetime.strptime(d1_aux, "%d/%m/%Y")
        d2 = datetime.strptime(d2_aux, "%d/%m/%Y")

        delta = d1 - d2

        aux = (reservas[apt]['valor'] * delta.days)

        if aux > 0:
            print("\nValor da hospedagem: R$", aux)

        else:
            print("\nValor da hospedagem: R$", reservas[apt]['valor']) 
        
        res = input('\nDeseja realmente finalizar a reserva? (S/N): ')

        if res.upper() == 'S':
            del reservas[apt]
            print('\nReserva Finalizada')

        else:
            print('\nReserva não finalizada')
           
    else:
        print("\nQuarto não ocupado")

def check_read_data(code):
    if res_read():
        print()

        apt = input("Digite o número do quarto: ")

        hosp_read()

        cpf = input("\nDigite o CPF: ")
            
        if apt in reservas:
            if cpf in reservas[apt]['cpf']:
                if code == '1':
                    check_in(apt)

                else:
                    check_out(apt)

            else:
                print('\nCPF não vinculado ao quarto')
                    
        else:
            print("\nReserva não encontrada")

def modulo_check():
    op = menu_check()

    global reservas
    reservas = res_load_file()

    while op != '0':
        if op == '1':
            os.system('cls')

            check_read_data('1')

        elif op == '2':
            os.system('cls')

            print("\nCHECK-OUT")

            check_read_data('2')

        else:
            print("Seleção inválida")

        res_write_file()

        print()
        input('Tecle ENTER para continuar')

        op = menu_check()