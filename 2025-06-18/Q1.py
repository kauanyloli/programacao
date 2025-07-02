'''Um determinado material radioativo perde metade de sua massa a cada 50 segundos. 
Faça um programa que solicite a massa inicial (em gramas) e que calcule o tempo necessário para que 
essa massa se torne menor que 0,5 grama. Ao término, o programa deve exibir a massa inicial, a massa
final e o tempo que levou para o decaimento (exiba o tempo informando horas, minutos e segundos).

Exemplo de saída:
Massa Inicial: 250 gramas
Massa Final: 0.48828125 gramas
Tempo de Decaimento: 0:07:30'''
import sys
#-feita----------------------------------------------------------------

# Lendo a massa inicial!
Minicial = float(input("Digite a massa inicial: "))
# Criando nova variável para guardar valor inicial!
Mdecaimento = Minicial
# Tempo inicial!
t = 0

# Loop para decaimento de massa!
while Mdecaimento > 0.5:
    Mdecaimento /= 2
    t += 50

# Separando o tempo decorrido em horas, minutos e segundos!
# Horas!
Horas = t // 3600
t = t % 3600
# Minutos!
Minutos = t // 60
t= t % 60
# Segundos!
Segundos= t

# Exibição de resultados seguindo modelo do enunciado!
print(f"Massa Inicial: {Minicial} gramas")
print(f"Massa Final: {Mdecaimento} gramas")
# {:02} ao final foramata para o valor ser exibido em duas casas!
print(f"Tempo de Decaimento: {Horas:02}:{Minutos:02}:{Segundos:02}") 
 
    