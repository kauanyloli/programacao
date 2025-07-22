import os, sys, json

strDirApp= os.path.dirname(__file__)

strNomeArq= f'{strDirApp}//cartola_fc_2024.json'

try:
    arqInput= open(strNomeArq,'r',encoding='utf-8')
    strDados