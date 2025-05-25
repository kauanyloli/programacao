'''Faça um programa que solicite ao usuário um número de até 
4 dígitos inteiro positivo e exiba a soma dos seus algarismos.

Exemplo: 2456 = 17 (2 + 4 + 5 + 6)
'''
#fiz
import sys

Num=int(input('Informe um número de até 4 dígitos inteiro positivo'))

if Num < 0 or Num > 9999:
        sys.exit('ERRO... Digite um numero valido')
if Num > 0 or  Num < 9999:
 mil = Num//1000
 Num %= 1000  

 cent = Num//100
 Num %= 100  

 dec = Num//10
 Num %= 10   

soma= mil+cent+dec+Num
print(f'O valor da soma é:',soma)

