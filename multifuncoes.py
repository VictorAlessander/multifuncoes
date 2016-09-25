# coding: UTF-8

import getpass
import sys

def menu():
	print("+---------------------------+\n"
		  "|[1] Múltiplo de cinco      |\n"
		  "|[2] Valor ao cubo          |\n"
		  "|[3] Par ou ímpar           |\n"
		  "|[4] Sucessor e antecessor  |\n"
		  "|[5] Contador de vogais     |\n"
		  "|[0] Sair                   |\n"
		  "+---------------------------+\n")

def mult_cinco(valor):
	if(valor % 5 == 0):
		return print("É múltiplo de cinco")
	else:
		return print("Não é múltiplo de cinco")

def aocubo(valor):
	return valor ** 3

def par_impar(valor):
	if(valor % 2 == 0):
		return print("O valor informado é par")
	else:
		return print("O valor informado é ímpar")

def sucessor_antecessor(valor):
	return(valor - 1), (valor + 1)

def cont_vogais(word):
	vogais = 0
	consoantes = 0

	dicionario = "aeiouAEIOUÁÉÍÓÚáéíóúâêôàèÌÒÙìãẽõÃẼÕ"

	for letra in word:
		if letra in dicionario:
			vogais += 1
		elif(letra != " "):
			consoantes += 1

	return print("Vogais: {:d} / Consoantes: {:d}" .format(vogais, consoantes))

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
			valor = int(input("Valor a ser avaliado: "))
			mult_cinco(valor)
		except:
			print("[!] Valor inválido. Se persistir, contacte o administrador")
		else:
			pass

	elif(opcao == 2):
		try:
			valor = int(input("Valor: "))
			aocubo(valor)
		except:
			print("[!] Valor inválido. Se persistir, contacte o administrador")
		else:
			pass

	elif(opcao == 3):
		try:
			valor = int(input("Insira o valor: "))
			par_impar(valor)
		except:
			print("[!] Valor inválido. Se persistir, contacte o administrador")
		else:
			pass

	elif(opcao == 4):
		try:
			valor = int(input("Valor: "))
			sucessor_antecessor(valor)
		except:
			print("[!] Valor inválido. Se persistir, contacte o administrador")
		else:
			pass

	elif(opcao == 5):
		try:
			word = str.lower(input("Insira uma palavra: "))
			cont_vogais(word)
		except:
			print("[!] Palavra inválida. Tente novamente")
		else:
			pass