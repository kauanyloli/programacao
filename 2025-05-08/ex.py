#programa para calcular a media de uma diciplina

#as notas devem ser inteiras e entre 0 e 100 (inclusive).

#caso a media seja igual  ou superior a 60 o aluno estara aprovado ; caso a media seja igual ou superior a 20 0 aluno estara em prova final e os demais casos o aluno estara reprovado

import sys

etapa1 = int(input('insira o valor da sua primeiro semestre'))
if etapa1 < 0 or etapa1 > 100:
    sys.exit(' nota invalisa!')
etapa2 = int(input('insira o valor da sua segundo semestre'))
if etapa2 < 0 or etapa2 > 100:
    sys.exit(' nota invalisa!')  
# round ele arredonda o valor
media=round((etapa1*2 + etapa2*3)/5 ) 
print(f'media do aluno{media}')    
# print(f'media do aluno{media:.0f}') 
