# coding: UTF-8

import getpass
import sys

def menu():
	print("+---------------------------+\n"
		  "|[1] Múltiplo de cinco      |\n"
		  "|[2] Valor ao cubo          |\n"
		  "|[3] Par ou ímpar           |\n"
		  "|[4] Sucessor e antecessor  |\n"
		  "|[0] Sair                   |\n"
		  "+---------------------------+\n")

def mult_cinco(valor):
	if(valor % 5 == 0):
		return print("É múltiplo de cinco")
	else:
		return print("Não é múltiplo de cinco")

# Início da autenticação

erro = 0

while(erro <= 3):
    user = input('Username: ')
    password = getpass.getpass('Password: ')

    if(user == "admin" and password == "root"):
        print('[*] Login successful')
        break

    else:
        erro = erro + 1

        if(erro < 3):
            print('[!] Username or password is incorrect. Try Again')

        elif(erro >= 3):
            print('[!] Wrong for three times. Bye')
            exit()

# Fim da autenticação

# Início das funcionalidades

while(True):
	try:
		menu()
		opcao = int(input(">> "))
	except:
		print("[!] Erro. Se persistir, contacte o administrador")
	else:
		pass

	if(opcao == 0):
		print("[*] Programa finalizado")
		exit()

	if(opcao == 1):
		try:
			valor = int(input("Valor: "))
			mult_cinco(valor)
		except:
			print("[!] Valor inválido. Se persistir, contacte o administrador")
		else:
			pass
