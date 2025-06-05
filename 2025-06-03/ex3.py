
'''
   A sequência de Fibonacci é uma sequência numérica onde cada número 
   é a soma dos dois anteriores, com os dois primeiros números sendo 1 e 1. 

   Implemente um programa que receba um número inteiro n e retorne os n 
   primeiros termos da sequência de Fibonacci.
'''
import sys
try:
    intNum = int(input('Digite a quantidade de elementos da sequencia:')) 
except ValueError:
   sys.exit('ERRRO: Digite um numero inteiro valido...')
except Exception as e:
          sys.exit('ERRRO{e}')
else:
    if intNum < 2:
       sys.exit('ERRRO: a sequencia de ibonacci deve possuir pelo menos 2 numeros...')  

intAtualNum = 1
intProxNum = 1
print(f'{intAtualNum},{intProxNum},',end='')

if intNum ==2:
     sys.exit('n')

for i in range(3,intProxNum + 1):
                    