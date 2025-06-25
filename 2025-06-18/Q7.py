'''Faça um programa que simule o jogo da forca. O programa terá uma 
constante chamada PALAVRA_CHAVE que armazenara a palavra a ser descoberta
(o programador deverá atribuir uma string ao eu critério para essa constante).
O programa deverá solicitar ao usuário as letras e à medida que as letras forem
sendo digitadas o programa irá exibir se o usuário acertou ou não. 
O jogo deverá considerar maiúsculas e minúsculas iguais. O jogador poderá errar 6 vezes antes de ser enforcado.'''

def mostrar_palavra(palavra, letras_acertadas):
    return ' '.join(letra if letra in letras_acertadas else '_' for letra in palavra)

def jogo_forca():
    palavra = CHAVE.lower()
    letras_acertadas = set()
    tentativas_restantes = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    print(f"Você tem {tentativas_restantes} tentativas para acertar a palavra.")
    
    while tentativas_restantes > 0:
        print(f"\nPalavra atual: {mostrar_palavra(palavra, letras_acertadas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")
        
        letra = input("Digite uma letra: ").lower()
        
        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, digite apenas uma letra!")
            continue
            
        if letra in letras_acertadas:
            print("Você já tentou essa letra!")
            continue
            
        letras_acertadas.add(letra)
        
        if letra not in palavra:
            tentativas_restantes -= 1
            print("Errou! Letra não encontrada.")
        else:
            print("Acertou! Letra encontrada.")
            
        if all(letra in letras_acertadas for letra in palavra):
            print(f"\nParabéns! Você ganhou! A palavra era: {palavra}")
            return
            
    print(f"\nGame Over! A palavra era: {palavra}")

if __name__ == "__main__":
    jogo_forca()