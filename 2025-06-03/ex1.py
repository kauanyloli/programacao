'''
   Dados dois números inteiros positivos, determinar o Máximo Divisor 
   Comum (MDC) entre eles usando o Algoritmo de Euclides.
'''
import sys
try:
    n1=int(input('Digite o primeiro numero inteiro:'))
    n2=int(input('Digite o segundo numero inteiro:'))
    if n1<=0 or n2<=0: 
    
        print('este numero nao é ')
except ValueError:
    sys.exit('ERRO...Digite um numero inteiro possitivo') 
      
except Exception as exc:
    sys.exit(f'ERRO:{exc}')   

for _ in range(n1 + n2):  # Laço temporário para garantir execução suficiente
    if n1 < n2:
        n1, n2 = n2, n1
    
    r1 = n1 % n2
    if r1 == 0:
        break
        
    n1, n2 = n2, r1

print(f'O MDC de ({n1},{n2}) é: {n2}')