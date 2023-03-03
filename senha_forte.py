from random import choice
import string

#Abre o arquivo em que as senhas serão armazenadas para acrescentar novas senhas
arq = open("senhas_salvas.txt", "a")

#Cria novas senhas fortes
nome_do_site = (input("Qual o nome do site da senha nova? "))
tamanho_da_senha = int(input("Quantos dígitos você quer na sua senha? "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha_segura = ''
for i in range(tamanho_da_senha):
  senha_segura += choice(caracteres)

#Printa o site e a senha
print("O site da senha é:", nome_do_site, "\nA senha gerada é: ",senha_segura, "\nOs dados forma armazenados no arquivo!")

#Junta a senha nova com as demais já salvas
arq.write("\n")
arq.write(nome_do_site)
arq.write(": ")
arq.write(senha_segura)
arq.close()