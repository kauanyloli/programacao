'''Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Faça um programa que solicite a massa inicial (em gramas) e que calcule o tempo necessário para que essa massa se torne menor que 0,5 grama. Ao término, o programa deve exibir a massa inicial, a massa final e o tempo que levou para o decaimento (exiba o tempo informando horas, minutos e segundos).

Exemplo de saída:
Massa Inicial: 250 gramas
Massa Final: 0.48828125 gramas
Tempo de Decaimento: 0:07:30'''
import sys
mInicial= int(input('digite o valor da Massa:'))
mFinal=0
tempo=0
tempoF=0
if mInicial<=0:
    sys.exit('ERRO...valor invalido')
    
while mInicial>=1:
    
 mFinal= mInicial/50
 tempo=+50
tempoF=tempo/60 
print('a massa final sera de :{mFinal} o tempo de decaimento sera de :{tempoF}')
 
    