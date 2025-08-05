''' Utilizando os arquivos GABARITO.TXT e PROVAS.CSV faça o que se pede:

.
O programa deverá ler o arquivo GABARITO.TXT e armazenar o seu conteúdo em uma lista;
O programa deverá ler o arquivo PROVAS.CSV e montar uma lista com os dados contidos nesse arquivo. Observe que cada 
linha tem o nome do aluno e as suas opções marcadas em cada questão;
O programa deverá adicionar no final de cada sub-lista do item (ii) a quantidade de acertos do aluno;
Em seguida o programa deverá ordenar a lista modificada no item (iii)
pela quantidade de acertos de cada aluno, começando pela maior pontuação até a menor pontuação obtida ;
O programa deverá salvar a lista do item (iv) no mesmo formato do arquivo 
PROVAS.TXT (cada aluno em uma linha, juntamebnte com suas opções marcadas e sua pontuação. 
Os dados dever ser separados por ;). O arquivo deverá ser salvo com o nome RESULTADOS.CSV.'''

import os, sys
diretorio = os.path.dirname(__file__)
try:
    gabLeitura = open(f'{diretorio}\\gabarito.txt', 'r', encoding='utf-8')
    provasLeitura = open(f'{diretorio}\\provas.csv', 'r', encoding='utf-8')
    arqEscrita = open(f'{diretorio}\\RESULTADOS.csv', 'w', encoding='utf-8')
except FileNotFoundError:
    sys.exit('\nERRO: Arquivo não encontrado...')
except Exception as erro:
    sys.exit(f'\nERRO: {erro}')
else:
    lstGabarito = list(gabLeitura.readline().split())
    lstProvas = list()
    while True:
        strProva = provasLeitura.readline().strip()
        if not strProva: break
        lstAux = [linha for linha in strProva.split(';')]
        lstProvas.append(lstAux)

    provasLeitura.close()
    gabLeitura.close()

    # Add notas!
    for prova in lstProvas:
        acertos = 0
        for nota in range(1, len(prova)):
            if prova[nota] == lstGabarito[nota - 1]: acertos += 1
            else: continue
        prova.append(acertos)
    lstProvas.sort(key=lambda prova: prova[11], reverse=True)
    for prova in lstProvas:
        linha = '; '.join(str(i) for i in prova)
        arqEscrita.write(f'{linha}\n')
    arqEscrita.close()
    for prova in lstProvas: print(prova)