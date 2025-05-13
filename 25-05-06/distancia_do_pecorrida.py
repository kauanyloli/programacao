#vc esta viajando de carro de mossoro para natal e,no momento, esta passando por lajes. o carroesta em movimento com uma velocidade inicial v0, e acelera constantimente ate atingir 
#a velocidade final ao chegar em natal.A formula pra calcular o tempo de viagem t é dada por t= a.t2/2 + v0.t-d
#solicita ao ussuaria as informaçoes:
# Distancia (km)
# velocidade inicial(em km/h)
# aceleraçao do carro(em metros por segundo ao quadrado)
#o programa deve calcular e exibir o tempo necessario para o carro pecorrer essa distancia ate natal, formatado no padrão hh:mm:ss.

import sys

d= int(input('digite a distancia (Km)'))
if d<=0:
    sys.exit('informe um valor possitivo')
v0 = float(input('digite a velocidade inicial(Km/h)'))
if v0<=0:
    sys.exit('informe um valor possitivo')
    
A = int(input('digite o valor de A(m/s2)')) 
if A<=0:
    sys.exit('informe um valor possitivo')
    
d*=1000   
v0 /=3.6
delta= v0**2-4*A*d
#if delta<0:
 #   sys.exit('nao é possivel calcular o tempo')
t=(-v0+delta**0.5)/(2*A)    
hora=t//3600
t=t%3600
minutos=t//60
segundos=t%60
print(f'o tempo gasto foi{hora}{minutos}{segundos}')        
    