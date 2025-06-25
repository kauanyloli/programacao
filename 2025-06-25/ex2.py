'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);
   
      2) Gere uma lista com N valores inteiros aleatórios entre 0 e 1.000 (inclusive)
         sem repetições;

      3) A partir da lista gerada, gere uma segunda uma lista com as raízes quadradas 
         dos valores da lista anterior;
'''

import sys, random

try:
    intnum = int(input('informe o valor de num: '))

    if intnum > 0 or intnum > 1000:
        print('ERRO: Nota inválida. Informe entre 0 e +1000...')
    #elif intnum < 0:
    #    print('ERRO: Nota inválida. Informe entre -100 e 0 ...')

except ValueError:
    sys.exit('/nERRO: informe um valor inteiro válido.../n')
except Exception as erro:
    sys.exit(f'/nERRO: {erro}.../n')
else:
#intnum = 0

    lista = list()

    for num in range(intnum):
        lista.append(random.randint(1000))
        #if intnum [0 , +100]:
        #   print('')
    print(lista)