#faça um programa que solicite os valores de v0,a e t. o programa deve calcular e exibir a distancia pecorrida pelo objeto

V0 = float(input('difite o valor de V0'))
t = float(input('difite o valor de t'))
A = float(input('difite o valor de A'))

deltaS=  (V0 * t + ((A * (t*t))/2))
print(f'o valor da distancia pecorrida é {deltaS}')