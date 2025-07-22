''' Você foi contratado para desenvolver um programa em Python que analisa uma lista de produto
s de informática de uma licitação. Cada produto é representado por uma sub-lista contendo as seguintes informações:

Nome: O nome do produto (string);
Categoria: A categoria à qual o produto pertence: "Permanente" ou "Consumo" (string);
Preço da Empresa A: O preço do produto na Empresa A (float);
Preço da Empresa B: O preço do produto na Empresa B (float);
Preço da Empresa C: O preço do produto na Empresa C (float);

A lista de produtos será alimentada a partir de um arquivo CSV (PRODUTOS_INFORMATICA.CSV), e
o programa deve realizar as seguintes tarefas utilizando as funções map(), filter() e funções lambda:


Aplicar um desconto nos preços de todos os produtos, para a empresa escolhida pelo usuário, baseado
em um valor percentual fornecido pelo usuário. Para isso, crie uma nova lista com os preços já com o desconto aplicado para a empresa escolhida;
Filtrar e listar os produtos. Para cada produto , a nova lista deverá conter:
O nome do produto
A categoria do produto;
O menor preço após a aplicação do desconto;
O nome da empresa com o menor preço.

CONSIDERAÇÕES:

O programa deve ler o arquivo CSV contendo os dados dos produtos e converter essas informações para uma lista de sub-listas;
Não utilize laços for explícitos para percorrer a lista;
Utilize as funções MAP() e FILTER() junto com funções LAMBDA para realizar as transformações e filtragens;
O programa deve permitir ao usuário escolher a empresa para a qual o desconto será aplicado e o percentual de desconto;
Os valores dos preços devem ser arredondados para duas casas decimais;
O arquivo de entrada será fornecido no mesmo diretório onde o programa será executado. O nome do arquivo deentrada será PRODUTOS_INFORMATICA.CSV;
Deverá ser gerado um arquivo com o resultado da licitação no mesmo diretório onde o programa será executado.
O nome do arquivo de saída será RESULTADO_LICITACAO.CSV.'''