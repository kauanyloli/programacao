'''
A cifra de Vigenère é uma técnica clássica de cifra de substituição que utiliza uma palavra-chave para embaralhar a mensagem original.
Para criptografar uma mensagem, cada caractere do texto claro é deslocado por uma quantidade
determinada pela letra correspondente da chave (veja a definição detalhada em Wikipedia: Cifra de Vigenère).


Nesta questão, você implementará uma versão da cifra de Vigenère que utiliza todos os caracteres 
imprimíveis do teclado, incluindo letras maiúsculas e minúsculas, letras acentuadas, números, símbolos, e espaços em branco. Todos os caracteres, incluindo espaços e letras acentuadas, serão criptografados de acordo com a chave fornecida.


A chave de criptografia será formada pelos últimos 9 caracteres do texto de entrada (strTexto),mas
esses últimos 9 caracteres também devem ser criptografados utilizando a cifra de Vigenère antes de serem
usados como chave. Ou seja, você deve criptografar o texto, gerar a chave a partir dos 9 últimos caracteres do 
texto criptografado, e então aplicar essa chave na cifra do texto completo.


Entrada:

A variável strTexto conterá uma string que representa o texto a ser criptografado. Este texto pode
conter letras maiúsculas, minúsculas, letras acentuadas, números, espaços, símbolos e outros caracteres
especiais. A seguir segue a sugestão que você pode utilizar no seu código:

strTexto = """O sol se ergue sobre o campo da Gália, e com ele as hostes gaulesas de Vercingetórix
se preparam para enfrentar-nos. Contudo, a vitória será nossa não pela força bruta, mas pela
astúcia e pela disciplina das legiões romanas. Como é de nosso costume, a mente hábil será
mais poderosa que a lâmina afiada. O inimigo, embora numeroso e bem posicionado, comete o erro
de subestimar a flexibilidade de nossas formações. Ele acredita que o flanco esquerdo de seu
exército é seguro. E é exatamente aí que vejo a oportunidade de esmagá-lo. Ordeno, portanto, que
tu, Marco Antônio, tomes o comando das nossas tropas e as posicione ao longo do flanco esquerdo
de Vercingetórix. Sei que o terreno é difícil, coberto de arbustos e com diversas elevações, mas
é essa falsa confiança do inimigo que nos dará a vantagem. Ele acreditará que aquela região está
fora de alcance, e, por isso, não dará a devida atenção à sua proteção. Esse erro será nossa
armadilha. O movimento que desejo que faças não é de ataque direto, mas uma manobra que o engane.
Quando o inimigo perceber a movimentação, ele se verá forçado a reagir, provavelmente desviando
parte de suas forças para aquele flanco, o que causará a desorganização de suas linhas. Nossa
vantagem, então, será dar-lhe a falsa sensação de que estamos atacando um ponto crucial, enquanto
preparamos o golpe real. Com a reorganização do inimigo, será o momento de agir. Nossas legiões,
disciplinadas e ávidas pela vitória, devem então se lançar com toda a força, aproveitando a brecha
que criamos. Vercingetórix não terá tempo de reagir adequadamente, e sua confiança será sua própria
ruína. Não te esqueças, Marco Antônio, que a guerra não é vencida apenas com espada e escudo, mas
com mente e vontade. A verdadeira força está em manter a ordem e a estratégia firmes diante do caos.
Confio em ti, como sempre, para executar este movimento com precisão e destreza. Que as legiões
romanas, com sua disciplina e coragem, avancem para a vitória. Que tu estejas em posição para
realizar a tarefa, pois o momento da ação se aproxima Ave César"""
Os últimos 9 caracteres do texto (ou mais, caso o texto tenha menos de 9 caracteres)
formarão a chave da cifra, mas esses últimos 9 caracteres devem ser criptografados antes de
serem usados como chave. Ou seja, a chave será gerada a partir de uma versão criptografada dos últimos 9 caracteres do texto.

Saída:

O programa deve retornar uma string representando o texto criptografado usando a cifra de Vigenère 
com um conjunto expandido de caracteres, incluindo letras acentuadas, espaços e símbolos, considerando 
que os últimos 9 caracteres do texto também foram criptografados para formar a chave

O programa deverá também fazwer a operação reversa, ou seja decriptografar o texto criptografado.

Regras:

Alfabeto Expandido: O conjunto de caracteres considerado para a cifra inclui todos os caracteres 
imprimíveis ASCII, como letras (maiúsculas e minúsculas), letras acentuadas, números, símbolos e espaços.
O alfabeto a ser usado pode ser representado pela sequência:
strCaracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáàâãäåçéèêíìîóòôõöúùûüÁÀÂÃÄÅÇÉÈÊÍÌÎÓÒÔÕÖÚÙÛÜ0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~'
Repetição da Chave: A chave será formada pelos últimos 9 caracteres do texto strTexto, mas 
esses últimos 9 caracteres devem ser criptografados primeiro, utilizando a cifra de Vigenère.
A partir dessa chave criptografada, a cifra será aplicada ao texto completo;

Cálculo do Deslocamento: O deslocamento de cada caractere será calculado com base no índice do 
caractere correspondente na chave. O cálculo deve ser feito usando a posição do caractere no alfabeto expandido.
Caso o deslocamento ultrapasse o final do alfabeto, ele deve "voltar" ao início;

Texto e Chave Sensíveis a Maiúsculas e Minúsculas: A cifra deve ser sensível a maiúsculas, minúsculas, letras acentuadas, 
símbolos e espaços. O comportamento da cifra deve ser consistente para todos os caracteres, sem exceção.'''

import math

strTexto = """O sol se ergue sobre o campo da Gália, e com ele as hostes gaulesas de Vercingetórix
se preparam para enfrentar-nos. Contudo, a vitória será nossa não pela força bruta, mas pela
astúcia e pela disciplina das legiões romanas. Como é de nosso costume, a mente hábil será
mais poderosa que a lâmina afiada. O inimigo, embora numeroso e bem posicionado, comete o erro
de subestimar a flexibilidade de nossas formações. Ele acredita que o flanco esquerdo de seu
exército é seguro. E é exatamente aí que vejo a oportunidade de esmagá-lo. Ordeno, portanto, que
tu, Marco Antônio, tomes o comando das nossas tropas e as posicione ao longo do flanco esquerdo
de Vercingetórix. Sei que o terreno é difícil, coberto de arbustos e com diversas elevações, mas
é essa falsa confiança do inimigo que nos dará a vantagem. Ele acreditará que aquela região está
fora de alcance, e, por isso, não dará a devida atenção à sua proteção. Esse erro será nossa
armadilha. O movimento que desejo que faças não é de ataque direto, mas uma manobra que o engane.
Quando o inimigo perceber a movimentação, ele se verá forçado a reagir, provavelmente desviando
parte de suas forças para aquele flanco, o que causará a desorganização de suas linhas. Nossa
vantagem, então, será dar-lhe a falsa sensação de que estamos atacando um ponto crucial, enquanto
preparamos o golpe real. Com a reorganização do inimigo, será o momento de agir. Nossas legiões,
disciplinadas e ávidas pela vitória, devem então se lançar com toda a força, aproveitando a brecha
que criamos. Vercingetórix não terá tempo de reagir adequadamente, e sua confiança será sua própria
ruína. Não te esqueças, Marco Antônio, que a guerra não é vencida apenas com espada e escudo, mas
com mente e vontade. A verdadeira força está em manter a ordem e a estratégia firmes diante do caos.
Confio em ti, como sempre, para executar este movimento com precisão e destreza. Que as legiões
romanas, com sua disciplina e coragem, avancem para a vitória. Que tu estejas em posição para
realizar a tarefa, pois o momento da ação se aproxima Ave César"""

str_caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáàâãäåçéèêíìîóòôõöúùûüÁÀÂÃÄÅÇÉÈÊÍÌÎÓÒÔÕÖÚÙÛÜ0123456789 !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
tamanho_alfabeto = len(str_caracteres)
tamanho_chave_base = 9

base_chave_raw = strTexto[-tamanho_chave_base:] if len(strTexto) >= tamanho_chave_base else strTexto

chave_final = ''
chave_para_chave_repetida = base_chave_raw * math.ceil(len(base_chave_raw) / len(base_chave_raw)) if base_chave_raw else ""

for i_chave_gen, char_base in enumerate(base_chave_raw):
    if char_base in str_caracteres and chave_para_chave_repetida and chave_para_chave_repetida[i_chave_gen % len(chave_para_chave_repetida)] in str_caracteres:
        indice_base = str_caracteres.index(char_base)
        indice_chave_para_chave = str_caracteres.index(chave_para_chave_repetida[i_chave_gen % len(chave_para_chave_repetida)])
        novo_indice_chave = (indice_base + indice_chave_para_chave) % tamanho_alfabeto
        chave_final += str_caracteres[novo_indice_chave]
    else:
        chave_final += char_base

if not chave_final:
    chave_final = 'Padrao'
    print(f'Atenção: A chave final calculada está vazia ou inválida. Usando a chave padrão: "{chave_final}"')

texto_criptografado_lista = []
modo_criptografia = 'criptografar'

chave_final_repetida_cripto = chave_final * math.ceil(len(strTexto) / len(chave_final))

for i_cripto, char_texto_cripto in enumerate(strTexto):
    if char_texto_cripto in str_caracteres:
        indice_texto_cripto = str_caracteres.index(char_texto_cripto)
        char_chave_cripto = chave_final_repetida_cripto[i_cripto % len(chave_final)]
        
        if char_chave_cripto in str_caracteres:
            indice_chave_cripto = str_caracteres.index(char_chave_cripto)
            
            if modo_criptografia == 'criptografar':
                novo_indice_cripto = (indice_texto_cripto + indice_chave_cripto) % tamanho_alfabeto
            
            
            texto_criptografado_lista.append(str_caracteres[novo_indice_cripto])
        else:
            texto_criptografado_lista.append(char_texto_cripto)
    else:
        texto_criptografado_lista.append(char_texto_cripto)

texto_criptografado = ''.join(texto_criptografado_lista)

texto_descriptografado_lista = []
modo_descriptografia = 'descriptografar'

chave_final_repetida_decripto = chave_final * math.ceil(len(texto_criptografado) / len(chave_final))

for i_decripto, char_texto_decripto in enumerate(texto_criptografado):
    if char_texto_decripto in str_caracteres:
        indice_texto_decripto = str_caracteres.index(char_texto_decripto)
        char_chave_decripto = chave_final_repetida_decripto[i_decripto % len(chave_final)]
        
        if char_chave_decripto in str_caracteres:
            indice_chave_decripto = str_caracteres.index(char_chave_decripto)
            
            if modo_descriptografia == 'descriptografar':
                novo_indice_decripto = (indice_texto_decripto - indice_chave_decripto + tamanho_alfabeto) % tamanho_alfabeto
            
            texto_descriptografado_lista.append(str_caracteres[novo_indice_decripto])
        else:
            texto_descriptografado_lista.append(char_texto_decripto)
    else:
        texto_descriptografado_lista.append(char_texto_decripto)

texto_descriptografado = ''.join(texto_descriptografado_lista)

print('-----')
print('Texto Original:'
)
print(strTexto)
print('\n-----')
print(f'Chave Gerada e Usada: "{chave_final}"')
print("\n-----")
print('Texto Criptografado:')
print(texto_criptografado)
print('\n-----')
print('Texto Descriptografado:')
print(texto_descriptografado)
print('\n-----')

if texto_descriptografado == strTexto:
    print('Verificação: O texto descriptografado é idêntico ao texto original. A cifra funcionou corretamente!')
else:
    print('Verificação: ATENÇÃO! O texto descriptografado NÃO é idêntico ao texto original. Há um erro na cifra.')