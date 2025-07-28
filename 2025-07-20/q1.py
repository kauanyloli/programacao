'''Desenvolva um programa que solicite ao usuário dois valores inteiros: o primeiro representando
a quantidade de sub-listas da lista principal e o segundo indicando a quantidade de elementos em 
cada sub-lista. Com base nesses valores, o programa deverá gerar aleatoriamente
os elementos de cada sub-lista da lista principal (utilizar LIST COMPREHENSIONS),
exibir a lista gerada e, em seguida, calcular e apresentar a lista transposta.'''

import sys, random

try:
    elementos = int(input('Digite a quantidade de elementos de cada Sub-lista: '))
    subListas = int(input('Digite a quantidade de Sub-listas: '))

except ValueError:
    sys.exit("\nERRO: informe um valor inteiro válido.")

except Exception as excecao:
    sys.exit(f"\nERRO: {excecao}")

else:
    lstPrincipal = list()
    lstTransposta = list()
    lstAux = list()

    for _ in range(subListas):
        lstSub = [random.randint(0,100) for _ in range(elementos)]
        lstPrincipal.append(lstSub)

    for sub in range(elementos):
        lstAux = [lstPrincipal[elemento][sub] for elemento in range(subListas)]
        lstTransposta.append(lstAux) 

    print("\nLista Normal:")
    for sub in lstPrincipal: print(sub)
    print("\nLista Transposta:")
    for transposta in lstTransposta: print(transposta)