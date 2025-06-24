'''Existem somente quatro números, maiores do que um, que podem ser obtidos pela soma de potências de 4 dos seus dígitos:

1643 = 14 + 64 + 44 + 34
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44


Faça um programa que encontra e exibe os números menores de 1000000, que são múltiplos de 2 ou 5 e que podem ser escritos pela soma das potências de 5 de seus dígitos.
'''
def obter_digito(num, posicao):
    """Retorna o dígito na posição especificada."""
    return num // (10 ** posicao) % 10

def verificar_numero(numero):
    """Verifica se um número pode ser escrito como soma de potências de 5 dos seus dígitos."""
    temp = numero
    soma = 0
    
    while temp > 0:
        digito = temp % 10
        soma += digito ** 5
        temp //= 10
        
    return soma == numero

def encontrar_numeros(limite=1000000):
    """Encontra todos os números menores que limite que são múltiplos de 2 ou 5
    e podem ser escritos como soma de potências de 5 dos seus dígitos."""
    resultados = []
    
    # Verificamos apenas múltiplos de 2 ou 5
    for i in range(2, limite, 2):  # Começamos com 2 e pulamos de 2 em 2
        if i % 5 == 0:  # Se já é múltiplo de 5, não precisamos verificar mais
            if verificar_numero(i):
                resultados.append(i)
        elif verificar_numero(i):
            resultados.append(i)
            
    return resultados

# Exemplo de uso com limite menor para demonstração
limites_teste = [1000, 10000, 100000]
for limite in limites_teste:
    print(f"\nNúmeros encontrados até {limite}:")
    resultados = encontrar_numeros(limite)
    for num in resultados:
        print(num)