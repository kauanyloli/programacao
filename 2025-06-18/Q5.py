'''Faça um programa que receba duas strings compostas por 0 e 1 apenas. essas
strings correspondem a uma sequência binária e devem ter o mesmo comprimento.

Pede-se que após a leitura e a validação das duas strings, o programa apresente 
o resultado das operações lógicas AND, OR e XOR entre essas duas variáveis.
'''
def validar_string_binaria(s):
    return all(bit in '01' for bit in s)

def operacoes_logicas(s1, s2):
    if len(s1) != len(s2):
        return "As strings devem ter o mesmo comprimento"
    if not (validar_string_binaria(s1) and validar_string_binaria(s2)):
        return "As strings devem conter apenas 0s e 1s"
    
    and_result = ''
    or_result = ''
    xor_result = ''
    
    for i in range(len(s1)):
        and_result += '1' if s1[i] == '1' and s2[i] == '1' else '0'
        or_result += '1' if s1[i] == '1' or s2[i] == '1' else '0'
        xor_result += '1' if s1[i] != s2[i] else '0'
    
    return f"""
Resultados:
AND (&):  {and_result}
OR (|):   {or_result}
XOR (^):  {xor_result}
"""

# Exemplo de uso
s1 = "1010"
s2 = "1100"
print(f"String 1: {s1}")
print(f"String 2: {s2}")
print(operacoes_logicas(s1, s2))