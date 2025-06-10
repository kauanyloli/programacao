'''
   Programa para verificar quantas vogais existem em uma string informada pelo usuário.
'''
strLetra = input('Digite um texto').upper()

intVogais='AEIOUÁÉÍÓÚÃÕÃÃÂÊÛÎÔ'

intVogais=0

for strLetra in strLetra:
   if strLetra == 'A' or strLetra =='E' or 