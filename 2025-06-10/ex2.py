'''
   Programa para ao digitar uma palavra ela seja escrita da seguinte forma 
   (como exemplo iremos usar a palavra PROGRAMAÇÃO).

   p
   PR
   PRO
   PROG
   ...
   PROGRAMAÇÃO  
'''
strTexto = input('Digite um texto')

intPosicao=0

while intPosicao < len(strTexto):
   print(strTexto[0:intPosicao +  1])
   intPosicao+=1