'''Faça um programa que receba duas strings compostas por 0 e 1 apenas. essas
strings correspondem a uma sequência binária e devem ter o mesmo comprimento.

Pede-se que após a leitura e a validação das duas strings, o programa apresente 
o resultado das operações lógicas AND, OR e XOR entre essas duas variáveis.
'''
try:
    # Variável que serve com TRUE!
    Valido = 1

    # Lê a primeira string!
    #string_1 = "1010" # Para testes! ##################################
    string_1 = input("Digite a primeira string: ")
    # Vê se há algo de diferente de 0 ou 1 na primeira string!
    for num in string_1:
            if int(num) != 0 and int(num) !=1:
                print("Há caracteres diferentes de 1 e 0 na 1ª string!",num)
                Valido = 0

    # Lê a segunda string!
    #string_2 = "1100" # Para testes! ##################################
    string_2 = input("Digite a segunda string: ")

    # Vê se há algo de diferente de 0 ou 1 na segunda string!
    for num2 in string_2:
            if int(num2) != 0 and int(num2) !=1:
                print("Há caracteres diferentes de 1 e 0 na 2ª string!",num2)
                Valido = 0

    # Checa se as duas strings tem o mesmo comprimento!
    if len(string_1) != len(string_2):
        print("AS DUAS STRINGS NÃO TEM O MESMO COMPRIMENTO")
    else:
        # Inicio de operações boleanas!
        if Valido == 1:
                #print("OK de falhas iniciais") ##################################
                # Criação de variáveis a serem útilizadas!
                variavel_AND = 0
                variavel_OR = 0
                variavel_XOR = 0
                variavel_AND_temp = int()
                variavel_OR_temp = int()
                variavel_XOR_temp = int()
                # Calculando AND, OR e XOR!
                for pos in range (len(string_1)):
                    #print(string_1[pos],string_2[pos]) # Para testes! ##################################

                    # Calculando AND!
                    if string_1[pos] == "1" and string_2[pos] == "1":
                        variavel_AND_temp = (variavel_AND_temp * 10) + 1
                    else:
                        variavel_AND_temp = (variavel_AND_temp * 10) + 0
                    variavel_AND = variavel_AND_temp

                    # Calculando OR!
                    if string_1[pos] == "1" or string_2[pos] == "1":
                        variavel_OR_temp = (variavel_OR_temp * 10) + 1
                    else:
                        variavel_OR_temp = (variavel_OR_temp * 10) + 0
                    variavel_OR = variavel_OR_temp

                    # Calculando XOR!
                    if string_1[pos] == string_2[pos]:
                        variavel_XOR_temp = (variavel_XOR_temp * 10) + 0
                    else:
                        variavel_XOR_temp = (variavel_XOR_temp * 10) + 1
                    variavel_XOR = variavel_XOR_temp


                # Exibe o resultado de todas as operações!
                print("O resultado das operações lógicas AND, OR e XOR são: ")
                print(f"O AND entre {string_1} e {string_2} é {variavel_AND}.")
                print(f"O OR entre {string_1} e {string_2} é {variavel_OR}.")
                print(f"O XOR entre {string_1} e {string_2} é {variavel_XOR}.")

# except para apresentação de erros, potencialmente causados por entradas de letras!
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa provavelmente foi sua!, " +
           "tente digitar apenas numeros inteiros!")