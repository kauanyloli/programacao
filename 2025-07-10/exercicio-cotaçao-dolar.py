'''
   Fazer um programa que faça as seguintes operações.

   1) A partir do conteúdo do arquivo cotacao_dolar.csv gerar uma lista onde cada item
      dessa lista será uma sub-lista com os valores de cada linha do arquivo.

      a) Os valores estão separados por ";";
      b) Os dois primeiros valores são valores do tipo FLOAT;
      c) O terceiro valor é do tipo DATE;
      

   2) Gerar arquivos para cada ano. Salvar o arquivo com o mesmo nome do arquivo que 
      foi aberto na questão 1, adionando no final do nome o sufixo "_nnnn" onde "nnnn" 
      corresponde ao ano das cotações;


   3) Gerar arquivos por ano com as médias das cotações mensais. Salve os arquivos com 
      o nome "media_cotacao_nnnn.csv" onde "nnnn" corresponde ao ano. Cada linha do arquivo
      deverá ter o nome do mês e em seguida o valor médio da cotação. Separe os valores da 
      linha por ";";
'''
import os, sys

strdir= os.path.dirname(__file__)

try:
    arqleitura= open(f'{dir}\\cotaçao-dolar.cvs','r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERRO: Arquivo não encontrado...')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}')
else:
    listcotaçao= list() 
    lstCabecalho = arqleitura.readline().strip().split(';')
    while True:
      # Lendo a linha e armazendo na variável
      strLinha = arqleitura.readline().strip()   
      # Interrompe o laço quando não há conteúdo na linha (EOF)
      if not strLinha: break
      # Transforma a string em uma lista convertendo os valores para inteiro
      lstAux = [int(i) if i.isdigit() else i for i in strLinha.split(';')]
      # Adicionando os dados na lista
      listcotaçao.append(lstAux)
    arqleitura.close()
for time in listcotaçao:
    time.insert(4, time[1]*3 + time[2])
    time.append(time[5] - time[6])    
