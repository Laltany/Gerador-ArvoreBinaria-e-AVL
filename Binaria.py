from os import listdir
import sys
import os
import time
from random import randint
import statistics

diretorio = str(sys.argv[1])
dir= './'+ diretorio +"/"

class No:
	def __init__(self, matricula, nome, curso, email, telefone, direita, esquerda): #Estrutura dos nodos
		self.matricula = matricula
		self.nome = nome 
		self.curso=curso
		self.email=email
		self.telefone = telefone
		self.direita = direita
		self.esquerda =esquerda

lista_arqs = [arq for arq in listdir(dir)]
arquivoBusca =  open('buscas.txt', 'r')


class tree:
	def __init__(self): #inicia arvore
		self.root = No(None, None, None, None, None, None, None)
		self.root = None

	def inserir(self, identifica, nome): #insere os alunos na arvore
		diretorio = dir + nome + ".txt"
		arquivo =  open(diretorio, 'r')
		linhas = arquivo.readlines()				
		novo = No(identifica,linhas[1],linhas[2],linhas[3],linhas[4], None, None) #Cria novo nodo
		if self.root == None:
			self.root = novo			
		else:
			atual = self.root			
			while True:				
				anterior = atual
				if identifica <= atual.matricula:
					atual = atual.esquerda
					
					if atual == None:
						anterior.esquerda = novo
						return
				else:
					atual = atual.direita
					if atual == None:
						anterior.direita = novo
						return
		
	def busca (self): #Busca normal através do arquivo de busca
		temp=[]
		matriculas= []	
		linhasBusca = arquivoBusca.readlines()
		for i in range(len(linhasBusca)): # passando pra memória
			mat = int(linhasBusca[i])
			matriculas.append(mat)
		for j in range(len(matriculas)):			
			Matricula_Aluno = matriculas[j]		
			atual = self.root
			while atual.matricula != Matricula_Aluno:
				if Matricula_Aluno< atual.matricula:
					atual=atual.esquerda
				else:
					atual = atual.direita
				if atual == None:
					return None			
			print ("----------- Aluno encontrado --------------")
			print ("Matricula:", atual.matricula)
			print ("Nome:", atual.nome)
			print ("curso:", atual.curso)
			print ("email:", atual.email)
			print ("Telefone:", atual.telefone)
			print ("-------------------------------------------")

 	

	def buscaDesempenho (self, quantidade): #Busca com desempenho
		arquivo = open ('MetricasBinaria.txt', 'w')
		numero = lista_arqs[0].split(".")
		primeiro = int(numero[0])
		total = primeiro + quantidade
		listaMatricula=[]
		for i in range(quantidade):
			Matricula_Aluno = randint(primeiro, total)
			listaMatricula.append(Matricula_Aluno)
		for c in range(len(listaMatricula)):
			start_time = time.time()
			mat = listaMatricula[c]							
			atual = self.root
			while atual.matricula != mat:
				if mat< atual.matricula:
					atual=atual.esquerda
				else:
					atual = atual.direita
				if atual == None:
					return None
			end_time= time.time()
			print ("----------- Aluno encontrado --------------")
			print ("Matricula:", atual.matricula)
			print ("Nome:", atual.nome)
			print ("curso:", atual.curso)
			print ("email:", atual.email)
			print ("Telefone:", atual.telefone)
			print ("-------------------------------------------")

			print("Desvio padrão:" , statistics.pstdev(listaMatricula))
			print("Variancia:", statistics.variance(listaMatricula))
			print("Tempo Médio da Busca:",  end_time - start_time )
			DP = ("Desvio padrão: %i \n" % statistics.pstdev(listaMatricula))
			var = ("Variancia: %i \n " % statistics.variance(listaMatricula))
			tempMedio = ("Tempo: %i \n" % (end_time - start_time) )
		print ("tempo total:", end_time - start_time)
		total = ("tempo total:%i \n" % (end_time - start_time))
		arquivo.write(total)
		arquivo.close()
	

	def busca2 (self, quantidade): #Busca semi aleatória
		numero = lista_arqs[0].split(".")
		primeiro = int(numero[0])
		total = primeiro + quantidade
		for i in range(quantidade):
			Matricula_Aluno = randint(primeiro, total)
		
			atual = self.root
			while atual.matricula != Matricula_Aluno:
				if Matricula_Aluno< atual.matricula:
					atual=atual.esquerda
				else:
					atual = atual.direita
				if atual == None:
					return None

			print ("----------- Aluno encontrado --------------")
			print ("Matricula:", atual.matricula)
			print ("Nome:", atual.nome)
			print ("curso:", atual.curso)
			print ("email:", atual.email)
			print ("Telefone:", atual.telefone)
			print ("-------------------------------------------")
			

	def inOrder(self, atual): ## teste
		if atual != None:
			self.inOrder(atual.esquerda)
			print(atual.matricula,end=" ")
			self.inOrder(atual.direita)


	def caminhar(self): ## teste
		print(" Exibindo em ordem: ",end="")
		self.inOrder(self.root)
	
def main():
	print("Rodando!")
	arv = tree()
	opcao = 0
	while opcao != 6:
		print("***********************************")
		print("Entre com a opcao:")
		print(" --- 1: Inserir")
		print(" --- 2: Pesquisar")
		print(" --- 3: mostrar arvore")
		print(" --- 4: Buscas PseudoAleatorias")
		print(" --- 5: Vizualizar Desempenho da busca")
		opcao = int(input("-> "))
		if opcao == 1:
			for i in range(len(lista_arqs)):
				numero = lista_arqs[i].split(".")				
				nome = numero[0]				
				identifica = int(numero[0])	
				print(identifica)			
				arv.inserir(identifica, nome)
		elif opcao == 2:
			arv.busca()				
		elif opcao == 3:
			arv.caminhar()
		elif opcao == 4:
			print("quantidade de buscas:")
			quantidade = int(input("-> ")) 
			arv.busca2(quantidade)
		elif opcao == 5:
			print("quantidade de buscas:")
			quantidade = int(input("-> ")) 
			arv.buscaDesempenho(quantidade)

if __name__ == "__main__":
	main()

	


			


		
			