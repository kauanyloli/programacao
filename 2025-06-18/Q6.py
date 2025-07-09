'''
Tomando por base a definição de Constante de Kaprekar (https://pt.wikipedia.org/wiki/Constante_de_Kaprekar)
faça um programa que receba um inteiro positivo de no máximo 4 dígitos e exiba em quantas iterações esse
número converge para a Constante de Kaprekar. Exiba as iterações também.

Para que um número de 4 dígitos não convirja para 6174, a restrição a ser considerada é a seguinte: 
número tiver todos os seus dígitos iguais, como 1111, 2222, 3333, etc., o processo de Kaprekar não 
funcionará, porque a diferença entre o número maior (formado pelos dígitos em ordem decrescente) 
e o menor (formado pelos dígitos em ordem crescente) será sempre zero.

Por exemplo:

para n = 3524, o programa deverá exibir a seguinte saída:

Iterações:
5432 – 2345 = 3087
8730 – 0378 = 8352
8532 – 2358 = 6174

Nº de Iterações: 3'''

n = int(input("Digite um inteiro positivo de no máximo 4 dígitos: "))

if not (0 < n < 10000):
    print("Número fora do intervalo permitido (1-9999).")
else:
    # Converte para string e preenche manualmente com zeros à esquerda
    s_n = str(n)
    while len(s_n) < 4:
        s_n = "0" + s_n
    
    # Verifica se todos os dígitos são iguais
    if len(set(s_n)) == 1:
        print("O processo de Kaprekar não funciona para números com todos os dígitos iguais.")
    else:
        
        count = 0
        current_number = n

        print("\nIterações:")
        while current_number != 6174:
            # Converte para string e preenche manualmente com zeros à esquerda para o número atual
            s_current_number = str(current_number)
            while len(s_current_number) < 4:
                s_current_number = "0" + s_current_number

            # Converte a string de dígitos para uma lista de inteiros para facilitar a ordenação
            digitos_list = [int(d) for d in s_current_number]

            # Cria uma cópia para ordenar em ordem decrescente
            digitos_desc_list = list(digitos_list) 
            tamanho = len(digitos_desc_list)
            for i in range(tamanho - 1):
                for j in range(tamanho - 1 - i):
                    if digitos_desc_list[j] < digitos_desc_list[j+1]:
                        # Troca os elementos se estiverem fora de ordem
                        temp = digitos_desc_list[j]
                        digitos_desc_list[j] = digitos_desc_list[j+1]
                        digitos_desc_list[j+1] = temp
            
            # Converte a lista de volta para string
            digits_desc = "".join([str(d) for d in digitos_desc_list])
            # Cria uma cópia para ordenar em ordem crescente
            digitos_asc_list = list(digitos_list) 
            tamanho = len(digitos_asc_list)
            for i in range(tamanho - 1):
                for j in range(tamanho - 1 - i):
                    if digitos_asc_list[j] > digitos_asc_list[j+1]:
                        # Troca os elementos se estiverem fora de ordem
                        temp = digitos_asc_list[j]
                        digitos_asc_list[j] = digitos_asc_list[j+1]
                        digitos_asc_list[j+1] = temp
            
            # Converte a lista de volta para string
            digits_asc = "".join([str(d) for d in digitos_asc_list])

            num_desc = int(digits_desc)
            num_asc = int(digits_asc)

            result = num_desc - num_asc
            
            iteration_str = f"{num_desc} – {num_asc} = {result}"
            print(iteration_str)

            current_number = result
            count += 1

            # Proteção contra loops infinitos (improvável para Kaprekar, mas boa prática)
            if count > 10: 
                print("Mais de 10 iterações, algo pode estar errado.")
                break 

        if current_number == 6174: 
            print(f"Nº de Iterações: {count}")