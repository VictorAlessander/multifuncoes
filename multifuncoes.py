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
		  "|[6] Buscar arquivo .txt    |\n"
		  "|[0] Sair                   |\n"
		  "+---------------------------+\n")

def ajuda():
	print("[1] Será avaliado se o valor digitado é múltiplo de cinco ou não\n"
		  "[2] Digite um valor qualquer e será imprimido na tela o valor digitado elevado ao cubo\n"
		  "[3] Será avaliado se o valor enviado é par ou ímpar\n"
		  "[4] Exibirá na tela o sucessor e antecessor do número informado\n"
		  "[5] Esta função contará quantas vogais e quantas consoantes estão presentes na palavra enviada\n"
		  "[6] Procura um arquivo .txt e abre-o para leitura")

def mult_cinco(valor):
	if(valor % 5 == 0):
		return print("É múltiplo de cinco")
	else:
		return print("Não é múltiplo de cinco")

def aocubo(valor):
	return print("Valor ao cubo: {:d}" .format(valor ** 3))

def par_impar(valor):
	if(valor % 2 == 0):
		return print("O valor informado é par")
	else:
		return print("O valor informado é ímpar")

def sucessor_antecessor(valor):
	return print("Sucessor: {:d} / Antecessor: {:d}" .format((valor + 1), (valor - 1)))

def cont_vogais(word):
	vogais = 0
	consoantes = 0

	#dicionario = "aeiouAEIOUÁÉÍÓÚáéíóúâêôàèÌÒÙìãẽõÃẼÕ"
	dicionario = "aeiouáéíóãẽõàèìòâêô"

	for letra in word:
		if letra in dicionario:
			vogais += 1
		elif(letra != " "):
			consoantes += 1

	return print("Vogais: {:d} / Consoantes: {:d}" .format(vogais, consoantes))

# Início da autenticação

erro = 0

while(erro <= 3):
    user = input('Usuário: ')
    password = getpass.getpass('Senha: ')

    if(user == "admin" and password == "root"):
        print('[*] Login efetuado com sucesso!')
        break

    else:
        erro = erro + 1

        if(erro < 3):
            print('[!] Usuário ou senha incorretos. Tente novamente')

        elif(erro >= 3):
            print('[!] Errado por três vezes. Até mais')
            exit()

# Fim da autenticação

# Início das funcionalidades

while(True):
	try:
		menu()
		print("Digite 'ajuda' para mais informações\n")
		opcao = str(input(">> "))
	except:
		print("[!] Erro. Se persistir, contacte o administrador")
	else:
		pass

	if(opcao == '0'):
		print("[*] Programa finalizado")
		exit()

	if(opcao == '1'):
		try:
			valor = int(input("Valor a ser avaliado: "))
			mult_cinco(valor)
		except:
			print("[!] Valor inválido. Se persistir, contacte o administrador")
		else:
			pass

	elif(opcao == '2'):
		try:
			valor = int(input("Valor: "))
			aocubo(valor)
		except:
			print("[!] Valor inválido. Se persistir, contacte o administrador")
		else:
			pass

	elif(opcao == '3'):
		try:
			valor = int(input("Insira o valor: "))
			par_impar(valor)
		except:
			print("[!] Valor inválido. Se persistir, contacte o administrador")
		else:
			pass

	elif(opcao == '4'):
		try:
			valor = int(input("Valor: "))
			sucessor_antecessor(valor)
		except:
			print("[!] Valor inválido. Se persistir, contacte o administrador")
		else:
			pass

	elif(opcao == '5'):
		try:
			word = str.lower(input("Insira uma palavra: "))
			cont_vogais(word)
		except:
			print("[!] Palavra inválida. Tente novamente")
		else:
			pass

	elif(opcao == '6'):
		try:
			nome_arquivo = input("Nome do arquivo: ")
			try:
				a1 = open(nome_arquivo, 'r')
				texto = a1.read()
				print(texto)
				a1.close()
			
			except:
				print("[!] O arquivo {:s} não existe" .format(nome_arquivo))
		except:
			print("[!] Nome do arquivo inválido")

	elif(opcao == "ajuda"):
		ajuda()