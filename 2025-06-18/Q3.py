'''Na definição da Wikipédia, números triangulares são aqueles que representam o total 
de pontos que formam triângulos equiláteros em um plano (veja a definição detalhada em https://pt.wikipedia.org/wiki/Número_triangular).

Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não) triangular, de acordo com a definição.'''

try:
    num = int(input("Digite um número inteiro positivo: "))
    if num <= 0:
        print("Por favor, insira um número positivo.")
    else:
        n = 1
        triangular = False

        while n * (n + 1) // 2 <= num:
            if n * (n + 1) // 2 == num:
                triangular = True
                break
            n += 1

        if triangular:
            print(f"O número {num} é triangular.")
        else:
            print(f"O número {num} não é triangular.")
except:
    print("Entrada inválida. Por favor, digite um número inteiro.")