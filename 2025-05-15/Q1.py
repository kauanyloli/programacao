'''Faça um programa que solicite ao usuário um número de até 4 dígitos inteiro positivo e exiba a soma dos seus algarismos.

Exemplo: 2456 = 17 (2 + 4 + 5 + 6)
'''
import sys
Num=int(input('Informe um número de até 4 dígitos inteiro positivo'))
soma=0
if Num>0:
    resto = Num % 100
    Num = (Num - resto)/100
    soma = soma + resto
print(f'O valor da soma é:',Num)   
if Num<0:
    sys.exit('ERRO... Por favor infomerme um numero valido')
