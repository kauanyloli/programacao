
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

def obter_posicao_inicial():
    while True:
        try:
            x = int(input("Digite a coordenada X inicial: "))
            y = int(input("Digite a coordenada Y inicial: "))
            return x, y
        except ValueError:
            print("Por favor, digite números válidos!")

def determinar_quadrante(x, y):
    if x > 0 and y > 0:
        return "Primeiro quadrante"
    elif x < 0 and y > 0:
        return "Segundo quadrante"
    elif x < 0 and y < 0:
        return "Terceiro quadrante"
    elif x > 0 and y < 0:
        return "Quarto quadrante"
    elif x == 0 and y > 0:
        return "Eixo Y positivo"
    elif x == 0 and y < 0:
        return "Eixo Y negativo"
    elif x > 0 and y == 0:
        return "Eixo X positivo"
    elif x < 0 and y == 0:
        return "Eixo X negativo"
    else:
        return "Origem (0,0)"

def processar_movimentos(x, y):
    movimentos = input("Digite a sequência de movimentos: ").upper()
    movimentos_validos = []
    direcoes = {
        'U': (0, 1),  # cima
        'D': (0, -1), # baixo
        'R': (1, 0),  # direita
        'L': (-1, 0), # esquerda
        'N': (1, 1),  # nordeste
        'E': (1, -1), # sudeste
        'W': (-1, -1),# sudoeste
        'O': (-1, 1)  # noroeste
    }
    
    for movimento in movimentos:
        if movimento in direcoes:
            dx, dy = direcoes[movimento]
            x += dx
            y += dy
            movimentos_validos.append(movimento)
    
    return x, y, movimentos_validos

def main():
    print("=== Simulador de Movimento do Robô ===")
    
    # Obter posição inicial
    x, y = obter_posicao_inicial()
    quadrante_inicial = determinar_quadrante(x, y)
    
    # Processar movimentos
    x_final, y_final, movimentos_validos = processar_movimentos(x, y)
    quadrante_final = determinar_quadrante(x_final, y_final)
    
    # Exibir resultados
    print("\n=== Resultados ===")
    print(f"Posição inicial: ({x}, {y})")
    print(f"Quadrante inicial: {quadrante_inicial}")
    print(f"Posição final: ({x_final}, {y_final})")
    print(f"Quadrante final: {quadrante_final}")
    print(f"Quantidade de movimentos válidos: {len(movimentos_validos)}")
    print(f"Movimentos válidos: {', '.join(movimentos_validos)}")

if __name__ == "__main__":
    main()
