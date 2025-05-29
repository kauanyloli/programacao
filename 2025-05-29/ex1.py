''' dado que um numero que so possuis dois divisores(1 e ele mesmo),
faça um programa que solicite ao usuario
um numero inteiro e informe se ele é primo ou nao.'''
import sys

try:
    n=int(input('Digite um numero para saber se é primo :'))
    if n<=0:
        print('este numero nao é primo')
except ValueError:
    sys.exit('ERRO...Digite um numero inteiro possitivo') 
    
except Exception as exc:
    sys.exit(f'ERRO:{exc}')
    
else:
    divisores = 1
    contDivisor= 0
    while divisores <=n:
        if (n % divisores)==0:
             contDivisor +=1 
        divisores+=1         
    if contDivisor == 2:
        print(f'{n} é primo.')
    else:
        print(f'{n} não é primo.')
