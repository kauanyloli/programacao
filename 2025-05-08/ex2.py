''' programa paea classificar um triangulo quanto aos angulos
- o programa devera solicitar 3 angulos inteiros positivos;
- para ser um triangulo a somas dos angulos deve ser igual a180;

-retangulo: possui um angulo interno igual a 90
-obtusangulo: possui um angulo interno obtuso maior que 90. 
-acutangulo: possui todos os angulos internos agudos menores que 90

'''

import sys

angulo1= int(input('digite o valor do primeiro angulo'))
if angulo1 <0:
    sys.exit('angulo invalido')
angulo2=int(input('digite o valor do segundo angulo'))
if angulo2 <0:
    sys.exit('angulo invalido')
angulo3=int(input('digite o valor do terceiro angulo'))
if angulo3 <0:
    sys.exit('angulo invalido')

if angulo1+angulo2+angulo3 ==180:
     
else:
    sys.exit('nao é um triangulo')