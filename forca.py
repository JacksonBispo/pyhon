import random

def joga():

    imprime_mensagem()
    palavra_secreta = carrega_palavra_secreta()
    letra_acertada = init_letras_acertadas(palavra_secreta)
    print(letra_acertada)
    acertou = False
    enforcou = False
    erros = 0
   
    
    while(not enforcou and not acertou):
        
        chute = pede_chute()
    
        if (chute in palavra_secreta):
            marca_chute_certo(chute, letra_acertada, palavra_secreta)
        else:
            erros +=1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letra_acertada
        print(letra_acertada)

    if (acertou):
       imprime_mensagem_vencedor()
    else:
       imprime_mensagem_perdedor(palavra_secreta) 

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def imprime_mensagem():
    print('****************************')
    print('***********FORCA************')
    print('****************************')

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /     ____      \       ")
    print("  /                 \      ")
    print("//                   \     ")
    print("\|  XXXXX     XXXXX  |     ")
    print(" |  XXXXX     XXXXX  |     ")
    print(" |   XXX       XXX   |      ")
    print(" |         X         |      ")
    print(" \__       X       __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | [][][][][][]  |        ")
    print("   | [][][][][][]  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def carrega_palavra_secreta():
    enforcou = False
    acertou = False
    erros = 0 
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def init_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual a letra ? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_certo(chute, letra_acertada, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(letra == chute) :
            letra_acertada[index] = letra
        index +=1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__=="__main__"):
    joga()