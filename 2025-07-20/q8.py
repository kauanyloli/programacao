'''Você foi contratado para desenvolver um programa em Python que realiza consultas sobre a população dos municípios
do Brasil com base em um arquivo CSV contendo dados do último censo do IBGE. O programa deve oferecer duas opções de consulta para o usuário:

Consulta por região: O programa deverá listar as 10 cidades mais populosas de cada estado dentro de uma região específica 
do Brasil, apresentando as populações de cada cidade e o percentual que cada população representa do total do estado;

Consulta por estado: O programa deverá listar as 10 cidades mais populosas de um estado escolhido, apresentando as populações
de cada cidade e o percentual que cada população representa do total do estado.


INSTRUÇÕES:

O programa deve começar solicitando ao usuário uma das duas opções de consulta:
Consultar por estado;
Consultar por região.
Caso o usuário escolha consultar por região, o programa deverá:
Solicitar que o usuário informe a região do Brasil (Norte, Sul, Sudeste, Centro-Oeste, Nordeste);
Para cada estado da região, listar as 10 cidades mais populosas (nome e população);
As cidades devem ser listadas em ordem decrescente de população dentro de cada estado.
Caso o usuário escolha consultar por estado, o programa deverá:
Solicitar que o usuário informe a sigla de um estado;
Listar as 10 cidades mais populosas daquele estado (nome, população e percentual de cada cidade em relação à população total do estado);
As cidades devem ser listadas em ordem decrescente de população.

FORMATO DE ENTRADA:

O arquivo CSV a ser utilizado (CENSO_2022_POPULACAO_RESIDENTE_MUNICIPIOS.CSV)contém os seguintes campos:
Nome do município;
Código municipal;
UF;
População total.
Exemplos de linhas no CSV:
Natal;2408102;RN;751300
Mossoró;2408003;RN;264577
UF;
Parnamirim;2403251;RN;252716

FLUXO DO PROGRAMA:

O programa pergunta: "Deseja consultar por região ou estado?";
O programa solicita: "Informe o estado:" ou "Informe a região:";
O programa exibe os dados conforme as escolhas do usuário.

CONSIDERAÇÕES:

Deverão ser tratados possíveis informações passadas de maneira errada, tipo: informar a sigla de um estado que não existe;
O resultado deve ser formatado de maneira clara e legível;
Deve-se OBRIGATORIAMENTE utilizar LIST COMPREHENSION, FILTER(), SORT() juntamente com funções LAMBDA nessa questão.

OBSERVAÇÃO: os dados fornecidos no arquivo CSV foram obtidos em https://censo2022.ibge.gov.br/
'''