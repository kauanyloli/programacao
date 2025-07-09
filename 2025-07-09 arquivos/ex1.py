import os, sys
# obtendo o diretorio omde o programa esta salvo
strDir= os.path.dirname(__file__)

try:
 arqLeitura= open(f'{strDir}\\times.csv','r', encoding='utf-8') 
except FileNotFoundError:
    sys.exit('\nERRO: Arquivo não encontrado... ')
except Exception as erro:
      sys.exit('\nERRO: {erro}')
else:
    strTime =list()
    while True:
        #lendo a linha e armazendo na variavel
        strLinha= arqLeitura.readline().strip()
        #interrompe o laço quando nao a conteudo na linha(EQF)        
        if not strLinha: break
        #transforma a string em uma lista convertendo os valores
        