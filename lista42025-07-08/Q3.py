'''O aluno deverá implementar um programa em Python para simular a movimentação de um robô em um plano cartesiano. O programa será composto por dois arquivos:

robo.py: Responsável pela interação com o usuário (entrada e saída de dados);
robo_funcoes: Contém as funções que realizam as ações necessárias.

Requisitos do sistema:

O programa deve solicitar ao usuário:
A posição inicial do robô, informando as coordenadas X e Y;
A sequência de movimentos que o robô deve executar;

O programa deve:
Calcular a posição final do robô após executar os movimentos válidos;
Determinar em qual quadrante (ou eixo/origem) o robô se encontra antes e depois da movimentação;
Exibir as seguintes informações:
Posição inicial e seu respectivo quadrante;
Lista de movimentos válidos realizados e a quantidade deles;
Posição final e seu respectivo quadrante.

A funções devem validar as entradas e tratar possíveis erros, como:
Coordenadas não numéricas (INT ou FLOAT);
Movimentos inválidos;
Tipos de dados incompatíveis para as funções.

Detalhes da implementação:

Os movimentos válidos são representados pelas seguintes letras:
U: Move uma unidade para cima (eixo Y positivo);
D: Move uma unidade para baixo (eixo Y negativo);
R: Move uma unidade para a direita (eixo X positivo);
L: Move uma unidade para a esquerda (eixo X negativo);
O: Move uma unidade para a esquerda e uma unidade para cima;
N: Move uma unidade para a esquerda e uma unidade para baixo;
E: Move uma unidade para a direita e uma unidade para baixo;
W: Move uma unidade para a direita e uma unidade para cima.

Qualquer caractere diferente desses deve ser ignorado;

As funções a serem implementadas em robo_funcoes.py são:
quadrante(posicaoXY: tuple) -> tuple: Retorna a posição (tuple) e uma string indicando em qual quadrante, eixo ou origem a coordenada se encontra;
movimenta(posicaoXY: tuple, movimentos: str) -> tuple: Recebe a posição inicial e a sequência de movimentos e retorna uma tupla contendo a posição inicial, a sequência de movimentos válidos e uma tupla contendo a posição final.

O arquivo robo.py deve importar essas funções e realizar toda a interação com o usuário, exibindo os resultados (a seguir tem os exemplos de como seria a entrada de dados e a exibição dos resultados.

Exemplo de entrada de dados:

Informe a coordenada X inicial..: 2
Informe a coordenada Y inicial..: -6
Digite os movimentos para o Robô: zxcvbnmjuygfdsaqwertgbhjkoplkjh
Exemplo de exibição dos resultados:

RESULTADO: 
Posição Inicial..........: (2.0, -6.0)
Quadrante Inicial........: Quadrante IV

Movimentos Realizados....: nudwerol
Qt. Movimentos Realizados: 8

Posição Final............: (2.0, -6.0)
Quadrante Final..........: Quadrante IV'''