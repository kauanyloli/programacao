'''Na definição da Wikipédia, números triangulares são aqueles que representam o total 
de pontos que formam triângulos equiláteros em um plano (veja a definição detalhada em https://pt.wikipedia.org/wiki/Número_triangular).

Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não) triangular, de acordo com a definição.'''

import math

def eh_triangulo(n):
    if n < 0:
        return False
    
    # Resolvendo a equação n*(n+1)/2 = numero
    discriminante = 1 + 8*n
    raiz = (-1 + math.sqrt(discriminante)) / 2
    
    # Verifica se a raiz é um número natural
    return raiz.is_integer() and raiz > 0

# Entrada do usuário
numero = int(input("Digite um número inteiro positivo: "))
print(f"O número {numero} {'é' if eh_triangulo(numero) else 'não é'} triangular.")