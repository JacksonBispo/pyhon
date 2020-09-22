import forca
import advinhacao

def selecioan():
    print('****************************')
    print('******ESCOLHA O SEU JOGO****')
    print('****************************')

    jogo = int(input("1 para forca 2 para advinhacão 3 sair "))

    if(jogo==2):
        advinhacao.joga()
    elif(jogo==1):
        forca.joga()
    

if(__name__=="__main__"):
    selecioan()


