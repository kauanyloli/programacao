'''
   Dada a lista lstNomes (no início do código), faça um programa que:
   
      1) Gere mais duas listas (lstNotas_1 e lstNotas_2), cada uma com N notas aleatórias
         entre 0 e 100 (inclsuive). Cada uma dessas listas deverá ter exatamente notas
         para cada um dos nomes em lstNomes;

      2) Gere uma lista (lstBoletins), onde cada posição será uma sub-lista contendo um dos
         dos nomes de lstNomes e suas respectivas notas (lstNotas_1 e lstNotas_2);

      3) Após lstBoletins ser gerada, adicione em cada posição mais duas informações:

         a) A média das notas (utilize como referência o cálculo de média do IFRN);

         b) A situação do aluno (Aprovado, Prova Final ou Reprovado) seguindo os 
            critérios do IFRN;

         c) Liste todos os boletins.

      4) Ordene os Boletins (lstBoletins) em ordem decrescente de média e em seguida liste-os;

      5) Filtre e liste apenas os alunos aprovados;
'''

lstNomes = ['Scooby-Doo'       , 'Fred Flintstone', 'Zé Colmeia' , 'Dom Pixote'     , 
            'Muttley'          , 'Bionicão'       , 'Tutubarão'  , 'Capitão Caverna', 
            'Formiga Atômica'  , 'Jonny Quest'    , 'Space Ghost', 'Manda-Chuva'    , 
            'Barney Rubble'    , 'Salsicha'       , 'Falcão Azul', 'Batatinha'      , 
            'Penélope Charmosa', 'Pepe Legal'     , 'Catatau'    , 'Dick Vigarista' ]

import sys, random

try:
   intN = int(input('Informe o valor de N: '))
except ValueError:
   sys.exit('\nERRO: Informe um valor inteiro válido...\n')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}...\n')
else:
   if intN <= 0 or intN > 100:
      sys.exit('\nERRO: Informe um valor entre 1 e 100...\n')
