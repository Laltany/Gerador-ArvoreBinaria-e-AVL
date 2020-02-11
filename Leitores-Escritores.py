# -*- coding: ISO-8859-1 -*-
import _thread
import time, random
import threading

class Documento:
   contador_Leitor = 0 #Contador de leitores, começa sem leitores.
   documento = threading.Semaphore(1)
   mutex = threading.Semaphore(1) #Evita que duas threads tenham acesso simultaneo ao recurso compartilhado. O contador inicial do semaphore  começa no 1
  

   def faz_leitura(self): #faz a ação de leitura
      global contador_Leitor
      self.mutex.acquire()
      self.contador_Leitor += 1

      
      if self.contador_Leitor == 1: # Se for o primeiro leitor, o documento recebe semáforo
         self.documento.acquire()

      self.mutex.release() #libera o sinal/semaforo

   def libera_leitura (self): #Desbloqueia a leitura/ libera o documento para outras ações.
      global contador_Leitor
      self.mutex.acquire()
      self.contador_Leitor -= 1

      if self.contador_Leitor == 0: #Se for o ultimo leitor, libera o sinal/semaforo do documento. 
         self.documento.release()

      self.mutex.release()

   def faz_escrita(self):
      self.documento.acquire() #O documentor recebe um sinal/semaforo

   def libera_escrita(self):
      self.documento.release() #libera o sinal/semaforo do documento, permitindo outras a interação de outros escritos/leitores.

documento = Documento()

def escritor(escritor):
   while True:
      time.sleep(random.randint(1, 5)) #espera um numero randomico entre 1 e 5
      documento.faz_escrita() #ninguem mais pode escrever ou ler, pois a ação de escrita esta sendo realizada no documento
      print ("O escritor ", escritor, " esta escrevendo.")
      time.sleep(random.randint(1, 5)) #O escritor fica escrevendo durante n instantes. (N eh um valor aleatorio entre 1 e 10)
      documento.libera_escrita() #A acao de escrita eh desbloqueada e agora outro escritor pode escrever ou os leitores podem ler.
      print ("O escritor ", escritor, " parou de escrever.") 

def leitor(leitor):
   while True:
      time.sleep(random.randint(1, 5)) #oleitor espera n instantes (N eh um número randomico entre 1 e 10)
      documento.faz_leitura() # o dados recebe o sinal/semaforo
      print (leitor, "esta lendo.")
      time.sleep(random.randint(1, 5)) # A leitura eh realizada por N instantes
      documento.libera_leitura() # o dados libera o sinal/semaforo
      print(leitor,"acabou de ler.")

for i in range(2):
   print ("Escritor ", i)
   _thread.start_new_thread(escritor, tuple([i]))
for i in range(3):
   print ("Leitor ", i)
   _thread.start_new_thread(leitor, tuple([i]))


while 1: pass