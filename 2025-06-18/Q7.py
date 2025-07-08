'''Faça um programa que simule o jogo da forca. O programa terá uma 
constante chamada PALAVRA_CHAVE que armazenara a palavra a ser descoberta
(o programador deverá atribuir uma string ao eu critério para essa constante).
O programa deverá solicitar ao usuário as letras e à medida que as letras forem
sendo digitadas o programa irá exibir se o usuário acertou ou não. 
O jogo deverá considerar maiúsculas e minúsculas iguais. O jogador poderá errar 6 vezes antes de ser enforcado.'''

try:
    import random
    palavras = ("Naruto ","Sasuke ","sakura","Gaara","itachi","deidara","kakashi","sasori","konan","pain","hidan",
                "kakuzu","tobi","neji","tobirima")
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