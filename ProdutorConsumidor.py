#! /usr/bin/python
# coding:utf-8

from random import randint
from time import sleep
import sys
import os


sleep_Consumidor = False #Desativa ou Ativa o Consumidor
sleep_Produtor = False #Desativa ou Ativa o Produtor
#Tamanho_Max = 5 #tamanho max do Buffer
buffer = [] #Cria um buffer com o tamanho maximo informado


def Produtor(): 
 global buffer, Tamanho_Max, sleep_Consumidor, sleep_Produtor
 if not sleep_Produtor: # Se o Produtor estiver ativo ele insere numeros de 1 a 10 no buffer, até encher.
  while len(buffer) < Tamanho_Max: 
   buffer.append(randint(0, 10)) 
  else: #Se o buffer estiver cheio, o produtor informa, é desativado e chama consumidor
   print ("O buffer esta cheio:", buffer)
   sleep_Produtor = True 
   sleep_Consumidor = False
   Consumidor() 
    
def Consumidor():
 global buffer, Tamanho_Max, sleep_Consumidor, sleep_Produtor

 if not sleep_Consumidor: #verifica se processo está ativo
  if buffer: #verifica existem valores no buffer
    del buffer[0]  #remove sempre a primeira posição do buffer, ate sobrar nenhum valor.
  else:
   print ("O buffer esta vazio novamente:", buffer)
   sleep_Consumidor = True #
   sleep_Produtor = False 
   Produtor() #chama o produtor

Tamanho_Max= input("Qual o tamanho do buffer?")
Tamanho_Max = int(Tamanho_Max)

for i in range (50):
  Produtor()
  Consumidor()
