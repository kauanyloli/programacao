'''O Crivo de Eratóstenes é um algoritmo eficiente para encontrar todos os números primos menores ou
iguais a um determinado número n. O algoritmo funciona da seguinte maneira:

Crie uma lista de números de 2 até n, onde inicialmente todos os números são marcados como "potenciais primos";
Comece com o número 2. Marque todos os múltiplos de 2 (exceto o próprio 2) como não primos;
Vá para o próximo número não marcado e marque todos os seus múltiplos como não primos;
Repita esse processo até que tenha verificado todos os números até n.
TAREFA:

Implemente o algoritmo do Crivo de Eratóstenes em Python para encontrar todos os números primos
menores ou iguais a um número n. O número n será fornecido como entrada.


INSTRUÇÕES:

Utilize uma lista para marcar os números como primos ou não primos;
Implemente a marcação dos múltiplos como não primos de acordo com o Crivo de Eratóstenes
A entrada será um número inteiro n (2 ≤ n ≤ 10**6);
Ao final, imprima a lista com todos os números primos encontrados.'''