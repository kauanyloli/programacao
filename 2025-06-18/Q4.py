'''Na definição da Wikipédia, número de Armstrong é aquele número cuja soma de cada digito
dele elevado a potência n (onde n é a quantidade de dígitos) é igual ao número informado
(veja a definição detalhada em https://en.wikipedia.org/wiki/Narcissistic_number).

Faça um programa que solicite ao usuário um número inteiro positivo e informe se
ele é (ou não) um número de Armstrong, de acordo com a definição. NÃO usar a função LEN().'''

status_entrada = 0 
numero_str = ""

while status_entrada == 0:
    numero_str = input("Digite um número inteiro positivo: ")
    
    entrada_eh_digito = 1 # Assume que é dígito até provar o contrário
    
    if not numero_str: 
        entrada_eh_digito = 0
    else:
        for char in numero_str:
        
            if char < '0' or char > '9':
                entrada_eh_digito = 0
                break # Sai do loop assim que encontrar um caractere não dígito
    
    if entrada_eh_digito == 1:
        # Se a string for composta apenas por dígitos, tenta converter para inteiro
        numero_original = int(numero_str)
        if numero_original > 0: # Garante que o número é positivo
            status_entrada = 1 # Define status_entrada para 1 para sair do loop
        else:
            print("O número deve ser positivo. Tente novamente.")
    else:
        print("Entrada inválida. Digite um número inteiro positivo.")

soma_potencias = 0


quantidade_digitos = 0
temp_numero_para_contar = numero_original
if temp_numero_para_contar == 0: # Caso especial para o número 0
    quantidade_digitos = 1
else:
    while temp_numero_para_contar > 0:
        temp_numero_para_contar //= 10
        quantidade_digitos += 1


temp_numero_para_somar = numero_original
while temp_numero_para_somar > 0:
    digito = temp_numero_para_somar % 10
    soma_potencias += digito ** quantidade_digitos
    temp_numero_para_somar //= 10

if soma_potencias == numero_original:
    print(f"O número {numero_original} É um número de Armstrong.")
else:
    print(f"O número {numero_original} NÃO é um número de Armstrong.")