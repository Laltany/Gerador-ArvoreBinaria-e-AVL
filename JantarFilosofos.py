import sys
import _thread
import threading
import time, random


N = input ("Qual a quantidade de filosofos sentados na mesa?")
N = int(N)

class Desocupado:
  desocupado = True #todos os garfos começam como desocupados
  def estado_garfo(self,desocupado): #Muda o estado do garfo para ocupado ou desocupado
    self.desocupado = desocupado
 
  def verifica_garfo(self):  #Verifica se o garfo está desocupado. Se estiver desocupado retorna True, se não, False.
    return self.desocupado

Garfos = list() #Lista de Garfos
for i in range(N): #Adiciona  garfos na lista
   Garfos.append(Desocupado()) #Coloca estado atual em cada garfo

def Filosofo(f):
   filosofo = int(f) #Pega a posição do filosofo
   #While infinito para processo de comer ou pensar
   while True:
    #Verifica se o garfo a direita e a esquerda tá livre
    if Garfos[filosofo].verifica_garfo() ==True and Garfos[(filosofo + 1) % N].verifica_garfo() == True : #verifica se os garfos estão desocupados   
      Garfos[filosofo].estado_garfo(False) #Coloca o garfo da esquerda como ocupado
      Garfos[(filosofo+1)%N].estado_garfo(False) #Coloca o garfo da direita como ocupado
      print ("O filósofo ", filosofo, " está comendo")
      time.sleep(random.randint(1, 5)) #Os garfos ficam ocupados por N instante (N pode ser qualquer valor entre 1 e 5)
      Garfos[filosofo].estado_garfo(True) #Desocupa o garfo da direita
      Garfos[(filosofo + 1) % N].estado_garfo(True) #Desocupa o garfo da esquerda     
      print ("O filósofo ", filosofo ," desocupou as talheres e esta pensando em comer mais.")
      time.sleep(random.randint(1, 10)) #O filosofo deve esperar para poder comer novamente


for i in range (N): #Cria os filosofos
  print ("Filósofo ", i)
  _thread.start_new_thread(Filosofo, tuple([i]))

while 1: pass
