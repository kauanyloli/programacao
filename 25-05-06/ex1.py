#faça um programa que solicite os valores de v0,a e t. o programa deve calcular e exibir a distancia pecorrida pelo objeto

import sys


V0 = int(input('difite o valor de V0'))
if V0 <=0: 
 sys.exit('informe uma velocidade positiva.')
    
A = int(input('difite o valor de A'))
if A<=0: 
 sys.exit('informe uma aceleraçao positiva.')
t = int(input('difite o valor de t'))

if t <=0: 
 sys.exit('informe uma tempo positiva.')


deltaS=  (V0 * t + ((A * (t*t))/2))
print(f'o valor da distancia pecorrida é {deltaS}')