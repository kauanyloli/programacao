'''Considerando uma equação do 2º grau na forma:

image


Onde a, b e c são coeficientes reais, e x representa a variável que queremos encontrar.



Considerando que as raízes dessa equação são encontradas através da fórmula de Bhaskara.


image


E que o valor de delta é dado por:


image


Com base no valor de delta temos as seguintes condições:

delta maior que zero, a equação tem duas raízes reais distintas;
delta igual a zero, a equação tem uma raiz real (ou duas iguais);
delta menor que zero, a equação não tem raízes reais.

Elabore um programa que solicite ao usuário os coeficientes da equação
 (a, b e c) e exiba as raízes reais da equação (quando houver).'''
# acho que terminei 
# refazer sem import math
#terminei

import sys

a=int(input(' informe o valor de A'))
if a==0:
    sys.exit(f'Nao existe')
b=int(input(' informe o valor de B'))
c=int(input(' informe o valor de C'))
delta=b*b-4*a*c


if delta>0:
  x1= (-b+ (delta**0.5))/(2*a) 
  x2= (-b- (delta**0.5))/(2*a) 
  print(f' As raizes sao :',x1,x2)  
if delta==0:
    x=-b/(2*a)
    print(f' A raiz é:',x)    
    
if delta<0:
 print('Nao tem raizes')
        
    