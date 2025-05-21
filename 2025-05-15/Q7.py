'''Com base nas novas regras da Previdência Social estabelecidas pela Emenda Constitucional nº 103/2019, desenvolva um programa 
em Python que solicite oa usuário as seguintes informações de uma pessoa::

Sexo da pessoa (masculino/feminino);
Data de nascimento da pessoa (no formato DD/MM/AAAA);
Data de início da contribuição previdenciária da pessoa (no formato DD/MM/AAAA).

O programa deve então calcular e exibir a data em que a pessoa poderá se aposentar, considerando as seguintes regras de 
transição, com os pedágios aplicáveis para cada caso:


Aposentadoria por Idade:
Homens: podem se aposentar aos 65 anos, desde que tenham pelo menos 15 anos de contribuição.;
Mulheres: podem se aposentar aos 62 anos, desde que tenham pelo menos 15 anos de contribuição;
Para a aposentadoria por idade, não há pedágio adicional.

Explicação: A aposentadoria por idade é a forma mais simples de se aposentar, onde a pessoa precisa atingir uma certa idade
e ter um tempo mínimo de contribuição para o INSS (Instituto Nacional do Seguro Social). No caso da reforma, os homens precisam
atingir 65 anos e as mulheres 62 anos para se aposentarem por idade. Não existe pedágio aqui, ou seja, se a pessoa atingir esses
requisitos, pode se aposentar sem precisar contribuir por mais tempo do que o exigido.


Aposentadoria por Tempo de Contribuição (com Pedágio):
Homens: podem se aposentar após 35 anos de contribuição, com a inclusão de um pedágio de 50% do tempo que faltava para atingir 
os 35 anos de contribuição no momento da reforma;
Mulheres: podem se aposentar após 30 anos de contribuição, com a inclusão de um pedágio de 50% do tempo que faltava para atingir
os 30 anos de contribuição no momento da reforma.

Explicação: A aposentadoria por tempo de contribuição exige que a pessoa tenha contribuído com o INSS por um número mínimo de anos.
No caso da reforma, homens precisam ter 35 anos de contribuição e mulheres 30 anos de contribuição. Porém, quem já estava perto de 
se aposentar quando a reforma foi feita (em 2019) tem um pedágio. Esse pedágio é um "tempo extra" de contribuição que a pessoa precisa
cumprir para poder se aposentar. Esse pedágio corresponde a 50% do tempo que faltava para atingir a meta de contribuição quando a reforma entrou em vigor.


Exemplo de Pedágio:

Homens: Se um homem tinha 33 anos de contribuição em 2019 e, para se aposentar, precisaria de 35 anos, ele faltava 2 anos para atingir 
os 35 anos. Com o pedágio de 50%, ele teria que contribuir por mais 2 anos e meio (o tempo restante + metade desse tempo como pedágio);
Mulheres: Se uma mulher tinha 28 anos de contribuição em 2019 e, para se aposentar, precisava de 30 anos, ela faltava 2 anos para atingir
os 30 anos. Com o pedágio de 50%, ela teria que contribuir por mais 2 anos e meio também.
Considerações para o Programa:

O programa deve considerar que a pessoa iniciou sua contribuição antes da reforma e calcular a aposentadoria levando em conta as regras de
transição, ou seja, os anos de contribuição já alcançados e o pedágio;
O cálculo do tempo de contribuição restante deve ser feito com base na diferença entre a data atual e o ano de início da contribuição;
O programa deve calcular a data de aposentadoria para ambos os tipos de aposentadoria (por idade e por tempo de contribuição), levando em conta 
o pedágio e o tempo de contribuição restante;
Exibição dos resultados: O programa deve mostrar as duas possibilidades de aposentadoria (por idade e por tempo de contribuição) e as respectivas
datas em que a pessoa poderá se aposentar;
Poderá ser utilizada a biblioteca DATETIME (Documentação da bilioteca DATETIME). Caberá ao aluno fazer a pesquisa de quais funções deverão ser
utilizadas;
Poderá ser utilizada a biblioteca DATEUTIL (Documentação da bilioteca DATEUTIL). Caberá ao aluno fazer a pesquisa de quais funções deverão ser
utilizadas;'''


