import random
import jogos
def joga():
    print('****************************')
    print('*********ADVINHAÇÃO*********')
    print('****************************')

    numero_secreto = random.randrange(1,101)
    quantidade_chutes = 0; 
    pontos = 1000

    nivel = int(input("defina um nível 1 - iniciante, 2 - medio, 3 - dificíl " ))
    if(nivel==1):
        quantidade_chutes = 20
    elif(nivel==2):
        quantidade_chutes = 10
    elif(nivel ==3):
        quantidade_chutes = 5
    else:
        jogos.selecioan()
    chute = int(input("Digite o numero: "))
    for rodada in range(1, quantidade_chutes+1):
        acertou = numero_secreto == chute
        menor   =  chute < numero_secreto
        maior   =  chute > numero_secreto

        if(acertou):
            print("acertou em {} de {}".format(rodada,quantidade_chutes))
            break
        else:
            if(maior):
                print("você errou! o numero é maior que o número, tentativas ", rodada)
            if(menor):
                print("você errou! o numero é menor que o número, tentativas", rodada)
                pontos_prdidos = numero_secreto - chute
                pontos = pontos - pontos_prdidos
            chute = int(input("Digite o numero: "))
    print("Fim de jogo! pontos: ",pontos)

if(__name__=="__main__"):
    joga()
