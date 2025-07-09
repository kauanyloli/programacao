
'''Um robô pode se mover em oito sentidos em um plano cartesiano: U (cima);
D (baixo); R (direita); L (esquerda); O (noroeste/cima-esquerda); N (nordeste/cima-direita); E (sudeste/baixo-direita) e W (sudoeste/baixo-esquerda).

Faça um programa que:


Solicite ao usuário a posição inicial do robô (suas coordenadas X e Y);
Solicite ao usuário uma string. Letras maiúsculas e minúsculas são 
indistintas e aquelas informadas que estejam fora das estabelecidas (U, D, R, L, O, N, E e W) devem ser ignoradas;
Com base em cada letra válida (U, D, R, L, O, N, E e W), o robô deverá se deslocar 1 (uma) unidade em cada eixo (X e Y) por vez em função da direção;

Ao final, indique:


A posição inicial do robô (coordenadas X e Y);
A posição final do robô (coordenadas X e Y);
Quantos movimentos válidos ele executou;
Quais foram os movimentos válidos que ele executou;
Em que quadrante ele iniciou (posição inicial de X e Y) e;
Em que quadrante ele terminou (posição final de X e Y).'''
#posiçao inicial
import sys

print('Posição Inicial do Robô')
while True:
    try:
        x_in = int(input('Digite a coordenada X inicial do robô: '))
        y_in = int(input('Digite a coordenada Y inicial do robô: '))
        break
    except ValueError:
        sys.exit('Entrada inválida. Por favor, digite números inteiros para as coordenadas.')

posicao_x = x_in
posicao_y = y_in
movimentos_validos = []

print('\n--- Comandos de Movimento ---')
comandos = input('Digite a string de comandos de movimento (U, D, R, L, O, N, E, W): ').upper()

movimentos = {
    'U': (0, 1),   # Cima
    'D': (0, -1),  # Baixo
    'R': (1, 0),   # Direita
    'L': (-1, 0),  # Esquerda
    'O': (-1, 1),  # cima-esquerda
    'N': (1, 1),   # cima-direita
    'E': (1, -1),  # baixo-direita
    'W': (-1, -1)  # baixo-esquerda
}

for comando in comandos:
    if comando in movimentos:
        dx, dy = movimentos[comando]
        posicao_x += dx
        posicao_y += dy
        movimentos_validos.append(comando)

quadrante_inicial = ''
if x_in == 0 or y_in== 0:
    quadrante_inicial = 'Nenhum (sobre um eixo)'
elif x_in > 0 and y_in > 0:
    quadrante_inicial = 'Primeiro'
elif x_in < 0 and y_in> 0:
    quadrante_inicial = 'Segundo1'
elif x_in < 0 and y_in < 0:
    quadrante_inicial = 'Terceiro1'
else:
    quadrante_inicial = 'Quarto1'

quadrante_final = ''
if posicao_x == 0 or posicao_y == 0:
    quadrante_final = 'Nenhum (sobre um eixo)'
elif posicao_x > 0 and posicao_y > 0:
    quadrante_final = 'Primeiro'
elif posicao_x < 0 and posicao_y > 0:
    quadrante_final = 'Segundo'
elif posicao_x < 0 and posicao_y < 0:
    quadrante_final = 'Terceiro'
else:
    quadrante_final = 'Quarto'

print('\n--- Resultados da Simulação ---')
print(f'Posição inicial do robô: ({x_in}, {y_in})')
print(f'Posição final do robô: ({posicao_x}, {posicao_y})')
print(f'Total de movimentos válidos executados: {len(movimentos_validos)}')
print(f'Movimentos válidos executados: {",".join(movimentos_validos) if movimentos_validos else "Nenhum"}')
print(f'Quadrante inicial do robô: {quadrante_inicial}')
print(f'Quadrante final do robô: {quadrante_final}')