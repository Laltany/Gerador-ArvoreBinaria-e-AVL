import sys
import os
from random import randint

diretorio = str(sys.argv[1])
quantidade = int(sys.argv[2])
inicio = int(sys.argv[3])
maximo= inicio + quantidade

provedor = ['@gmail.com', '@hotmail.com']

dir= './'+ diretorio
os.makedirs(dir)

nomes = open ('./info/nomes.txt', 'r')
nomes = nomes.readlines()
cursos = open ('./info/cursos.txt', 'r')
cursos = cursos.readlines()
telefone = "\n"
j=0
for i in range(quantidade):
	inicio2 = str(inicio)
	matricula = inicio2 + "\n"
	nomearquivo = inicio2 + '.txt'
	dirarquivo= dir + "/" + nomearquivo 
	arquivo = open (dirarquivo, 'w')
	qtdNomes = int(len(nomes))	#Quantidade de nomes na lista
	random = randint(1, qtdNomes )
	qtdCursos = int(len(cursos)) #Quantidade de Cursos
	randomCurso = randint(0, 5 ) #curso aleatório
	randomEmail = randint(0, 1)	
	nome = nomes[random].split("\n")
	tuplaemail = (nome[0], provedor[randomEmail])
	while j < 11:
		if j == 2:
			telefone+= " "
		numero = randint(0,9)
		numero = str(numero)
		telefone += numero
		j+=1
	email = "%s%s" %(tuplaemail[0], tuplaemail[1])

	arquivo.write(matricula)
	arquivo.write(nomes[random])
	arquivo.write(cursos[randomCurso])
	arquivo.write(email)
	arquivo.write(telefone)
	arquivo.close()	
	inicio +=1
print("Todos os dados foram gerados com sucesso!")

	