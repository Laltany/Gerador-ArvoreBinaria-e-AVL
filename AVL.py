from os import listdir
import sys
import os
import time
from random import randint
import statistics

diretorio = str(sys.argv[1])
dir= './'+ diretorio +"/"
lista_arqs = [arq for arq in listdir(dir)]
arquivoBusca =  open('buscas.txt', 'r')

class No:
	def __init__(self, matricula, nome, curso, email, telefone):
		self.matricula = matricula
		self.nome = nome 
		self.curso=curso
		self.email=email
		self.telefone = telefone
		self.esquerda = None
		self.direita = None
		self.altura = 1

class tree:

	def inserir(self,root,identificador):
		nome= str(identificador)
		diretorio = dir + nome + ".txt"
		arquivo =  open(diretorio, 'r')
		linhas = arquivo.readlines()
		Novo = No(identificador,linhas[1],linhas[2],linhas[3],linhas[4])
		if not root:
			return Novo
		elif identificador < root.matricula:
			root.esquerda = self.inserir(root.esquerda,identificador)
		else:
			root.direita = self.inserir(root.direita,identificador)

		root.altura = max(self.altura(root.esquerda) , self.altura(root.direita)) + 1
		balance = self.Balance(root)

		if balance > 1 and identificador < root.esquerda.matricula:
			return self.GirarDireita(root) 
        
		if balance < -1 and identificador > root.direita.matricula:
			return self.GirarEsquerda(root)
        
		if balance > 1 and identificador > root.esquerda.matricula:            
			root.esquerda = self.leftRotate(root.esquerda)
			return self.GirarDireita(root) 
        
		if balance < -1 and identificador < root.direita.matricula:            
			root.direita = self.GirarDireita(root.direita)
			return self.GirarEsquerda(root)
		
		return root
        

        
	def busca(self, root):
		matriculas= []	
		linhasBusca = arquivoBusca.readlines()
		for i in range(len(linhasBusca)): #passando pra memória
			mat = int(linhasBusca[i])
			matriculas.append(mat)
		for j in range(len(matriculas)):

			Matricula_Aluno = matriculas[j]
			atual = root
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

	def busca2(self, root, quantidade):
		numero = lista_arqs[0].split(".")
		primeiro = int(numero[0])
		total = primeiro + quantidade
		for i in range(quantidade):
			Matricula_Aluno = randint(primeiro, total)
		
	#	for i in range(len(linhasBusca)):
			start_time = time.time()
	#		Matricula_Aluno = int(linhasBusca[i])
			atual = root
			while atual.matricula != Matricula_Aluno:
				if Matricula_Aluno< atual.matricula:
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
			

			print("Tempo Médio da Busca:",  end_time - start_time )

		print ("tempo total:", end_time - start_time) 


	def GirarEsquerda(self,z):
		y=z.direita
		t = y.esquerda
		y.esquerda=z
		z.direita=t
		z.altura= max(self.altura(z.esquerda),self.altura(z.direita)) + 1
		y.altura= max(self.altura(y.esquerda),self.altura(y.direita)) + 1
		return y
	def GirarDireita(self,z):
		y=z.esquerda
		t=y.direita
		y.direita=z
		z.esquerda=t
		z.altura= max(self.altura(z.esquerda),self.altura(z.direita)) + 1
		y.altura= max(self.altura(y.esquerda),self.altura(y.direita)) + 1
		return y
	def altura(self,root):
		if not root:
			return 0
		return root.altura
	def Balance(self,root):
		if not root:
			return 0
		return self.altura(root.esquerda) - self.altura(root.direita)
	def preorder(self,root):
		if not root:
			return
		print(root.matricula)
		self.preorder(root.esquerda)
		self.preorder(root.direita)

def main():
	print("Rodando!")
	arv = tree()
	root= None
	opcao = 0
	while opcao != 2:
		print("***********************************")
		print("Entre com a opcao:")
		print(" --- 1: Inserir")
		print(" --- 2: Pesquisar")
		print(" --- 3: mostrar arvore")
		print(" --- 4: Buscar Pseudoaleatorios")
		opcao = int(input("-> "))
		if opcao == 1:
			for i in range(len(lista_arqs)):
				numero = lista_arqs[i].split(".")						
				identifica = int(numero[0])	
				print(identifica)			
				root = arv.inserir(root, identifica)
		elif opcao == 2:
			arv.busca(root)				
		elif opcao == 3:
			arv.caminhar()
		elif opcao == 4:
			print("quantidade de buscas:")
			quantidade = int(input("-> ")) 
			arv.busca2(root, quantidade)

if __name__ == "__main__":
	main()