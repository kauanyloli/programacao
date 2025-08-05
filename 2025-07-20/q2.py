'''Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos
(n deverá ser solicitado ao usuário, positivo e entre 7 e 60, inclusive),
cada elemento dessa lista será um número aleatório entre 1 e 60 (inclusive) 
sem repetição. Após a lista ser gerada, as seguintes operações deverão ser implementadas:

Deverá ser criada uma segunda lista com todas as combinações possíveis de 6 dezenas.
Cada combinação deverá ser uma sub-lista. Cada combinação deverá estar ordenada do menor número para o maior;
A lista de números escolhidos deverá ser salva em um arquivo chamado NUMEROS_ESCOLHIDOS.
TXT (salvar no mesmo diretório/pasta em que o programa está salvo). Nesse arquivo os números
deverão estar em apenas 1 linha. Utilize espaço em branco para separar os valores na linha;
A lista de combinações deverá ser salva em um arquivo chamado COMBINACOES.CSV (salvar no mesmo
diretório/pasta em que o programa está salvo). Nesse arquivo cada combinação deverá estar em 1linha. 
Utilize ponto e vírgula para separar os valores na linha;
No final deverão ser exibidos na tela quantas combinações foram geradas, e 
quais as probabilidades de se acertar a sena, a quina e a quadra.'''

import sys, random, os; from math import factorial
diretorio = os.path.dirname(__file__)

try:
    escritaElem = open(f'{diretorio}\\NUMEROS_ESCOLHIDOS.txt', 'w', encoding='utf-8')
    escritaComb = open(f'{diretorio}\\COMBINACOES.csv', 'w', encoding='utf-8')
    elementos = int(input('Digite o valor de N elementos: '))

    while not (7 <= elementos <= 60):
        print('ERRO: digite um valor positivo entre 7 e 60.\n')
        elementos = int(input('Digite o valor de N elementos: '))

except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido.')

except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')
else:
    lstNumeros = list()
    lstCombinacoes = list()

    for _ in range(elementos):
        numTemp = random.randint(1,60)
        if numTemp not in lstNumeros: lstNumeros.append(numTemp)
        else: lstNumeros.append(numTemp + 1)

    linha = ' '.join(str(i) for i in lstNumeros)
    escritaElem.write(linha)
    escritaElem.close() 

    for num in range(len(lstNumeros)):
        for num2 in range(num + 1, len(lstNumeros)):
            for num3 in range(num2 + 1, len(lstNumeros)):
                for num4 in range(num3 + 1, len(lstNumeros)):
                    for num5 in range(num4 + 1, len(lstNumeros)):
                        for num6 in range(num5 + 1, len(lstNumeros)):
                            combinacao = [lstNumeros[num], lstNumeros[num2], lstNumeros[num3], 
                                        lstNumeros[num4], lstNumeros[num5], lstNumeros[num6]]
                            lstCombinacoes.append(combinacao)
                            lstCombinacoes[-1].sort()
    
    for comb in lstCombinacoes:
        linha = ';'.join(str(i) for i in comb)
        escritaComb.write(f'{linha}\n')
    escritaComb.close()

    combQuina = int((factorial(6) / factorial(5)) * (factorial(len(lstNumeros) - 6) / factorial((len(lstNumeros) - 6) - 1)))
    if elementos > 7: combQuadra = int((factorial(6) / (factorial(4) * 2)) * (factorial(len(lstNumeros) - 6) / (2 * factorial((len(lstNumeros) - 6) - 2))))
    else: combQuadra = 0
    

    print(f'\nQuantidade de Combinações')
    print(f'SENA: {len(lstCombinacoes)}')
    print(f'QUINA: {combQuina}')
    print(f'QUADRA: {combQuadra}')
    print(f'\nProbabilidades de Acertos\nSENA: 1/{len(lstCombinacoes)} = {(1 / len(lstCombinacoes))*100} %.')
    print(f'QUINA: {combQuina}/{len(lstCombinacoes)} = {(combQuina / len(lstCombinacoes))*100} %.')
    print(f'QUADRA: {combQuadra}/{len(lstCombinacoes)} = {(combQuadra / len(lstCombinacoes))*100} %.\n')