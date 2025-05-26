'''Desenvolva um um programa que efetue as seguintes especificações:

Solicite ao usuário os comprimentos dos três lados do triângulo;
Verifique se os comprimentos fornecidos podem formar um triângulo. Caso contrário, informe que não é possível formar um triângulo com esses lados;
Se for possível formar um triângulo, calcule os três ângulos do triângulo;
Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno);
Classifique o triângulo quanto os ângulos (acutângulo, obtusângulo ou retângulo);


Atentem para as seguintes observações:


Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, é necessário verificar a seguinte condição: A soma de quaisquer dois lados de um triângulo deve ser sempre maior que o terceiro lado;
Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo;
Poderá ser utilizada a biblioteca MATH (Documentação da bilioteca MATH). Caberá ao aluno fazer a pesquisa de quais funções deverão ser utilizadas;
Para classificar quanto aos lados, verifique se os três lados são iguais (equilátero), se dois lados são iguais (isósceles) ou se todos os lados são diferentes (escaleno);
Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 90 graus (obtuso), se um dos ângulos é igual a 90 graus (retângulo) ou se todos os ângulos são menores que 90 graus (agudo);
Considere que os ângulos são expressos em graus.'''

import sys
import math

a = float(input('informeo comprimento de A:'))
b= float(input('informeo comprimento de B:'))
c= float(input('informeo comprimento de C:'))

if  a<=0 or b<=0 or c<=0:
    sys.exit('ERRO.... digite  valores validos ')
if a + b <=c or a + c<= b or b + c <=a:
    sys.exit('ERRO... Não é possivel formar um triangulo com esses lados')

cos_A = (b*b + c*c - a*a)/(2*a*c)
angulo_A = math.degrees(math.acos(cos_A))

cos_B = (a*a + c*c - b*b)/(2*a*c)
angulo_B= math.degrees(math.acos(cos_B))

cos_C = (b*b + a*a - c*c)/(2*a*c)
angulo_C = math.degrees(math.acos(cos_C))

if a == b and b == c:
    tipo_lado = 'Equilátero'
else:
 if a==b or a==c or b==c:
      tipo_lado='Isósceles'
 else:
      tipo_lado='Escaleno'

if angulo_A==90 or angulo_B==90 or angulo_C==90:
    tipo_angulo= 'Retangulo'  
else :
  if angulo_A > 90 or angulo_B >90 or angulo_C > 90:
    tipo_angulo= 'Obtuso' 
  else:
   tipo_angulo = 'Agudo'     

print("Ângulo A:", format(angulo_A, ".2f"), "graus")
print("Ângulo B:", format(angulo_B, ".2f"), "graus")
print("Ângulo C:", format(angulo_C, ".2f"), "graus")
print("Classificação quanto aos lados:", tipo_lado)
print("Classificação quanto aos ângulos:", tipo_angulo)      
