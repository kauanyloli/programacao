'''
   Dados dois números inteiros positivos, determinar o Máximo Divisor 
   Comum (MDC) entre eles usando o Algoritmo de Euclides.
'''
import sys
try:
    n1=int(input('Digite o primeiro numero inteiro:'))
    if n1<=0:
        print('este numero nao é primo')
except ValueError:
    sys.exit('ERRO...Digite um numero inteiro possitivo') 
    
except Exception as exc:
    sys.exit(f'ERRO:{exc}')

n1=int(input('digite o primeiro numero inteiro'))