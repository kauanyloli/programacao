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
    
 #-----------------------------------------------------------------
 
try:
    import random
    palavras = ("ABACATE","LIMA","ABACAXI","LIMAO","PERA","graviola","caja","caQUI","BaNaNa","PeSSego","acai",
                "maracuja","uva","manga","tomate")
    # Escolhendo uma palavra aleatória!
    segredo = palavras[random.randint(0,len(palavras)-1)]
    # Convertendo todas as letras em MAIÚSCULAS!
    segredo = segredo.upper()
    # Contando quantidade de letras na palavra sorteada!
    visivel = "_"*len(segredo)
    # Limite de tentativas!
    tentativas = 6

    # Loop que permane até acertar todas as letras ou acabarem as tentativas!
    while visivel != segredo and tentativas > 0 :
        print(visivel)
        print("Lhe restam: ",tentativas,"tentativas!")
        # Lê uma letra e a converte em MAIÚSCULA!
        letra = input("Digite uma letra: ")
        letra = letra.upper()

        # Não aceita mais de uma letra nem letras já em 'visivel'!
        # Não altera 'segredo' e não reduz 'tentativas'!
        if len(letra) != 1 or visivel.count(letra) !=0 :
            print(letra,"Já foi digitado ou é mais que uma letra!") # Opcional
        
        else:
            # Reduz uma tentativa caso erre a letra!
            if segredo.count(letra) == 0:
                tentativas = tentativas - 1
        # Caixinha de comparação!
        #######################################################
            novavisivel = ""
            for pos in range (len(segredo)):
                # Caso de acerto de letra, troca "_" pela "letra" na visivel!
                if letra == segredo[pos]:
                    novavisivel += segredo[pos]
                # Caso de erro de letra, mantem "visivel[pos]" na visivel!
                else:
                    novavisivel += visivel[pos]
                    
            # Sai do laço com uma nova visivel
            visivel = novavisivel
        #######################################################

    # Exibe sucesso ou falha e exibe segredo!
    if visivel == segredo:
        print("Parabéns, você acertou!, a palavra era:",segredo)
    else:
        print("Esgotaram-se suas tentativas!, a palavra era:",segredo)

    print("FIM") # Opcional
except:
    print("Em algum lugar, de alguma forma, algo deu errado e a culpa provavelmente foi sua!")   