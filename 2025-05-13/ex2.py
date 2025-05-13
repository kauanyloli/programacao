import sys
try:
   intDividendo= int(input('digite o dividendo:'))
   intDivisor= int(input('digite Divisor:'))
   intResultado= intDividendo/ intDivisor
except ValueError:
    print(f'ERRO:nInforme um Valor que possa ser convertido em inteiro')   
except ZeroDivisionError:
    print('ERRO: Nao existe divisao por zero.')    
except Exception as tipoExcecao:# nao capitura o erro expecifico
    print(f'ERRO:{tipoExcecao}')
    print(f'ERRO:{sys.exc_info()}')#mostra especificamente o erro
else:
        
  print(intResultado)