import def_ppt
import random
import time

r ='S'
while( True):
    def_ppt.bem_vindo('OLÁ, XD, Vamos jogar pedra, papel e tesoura?')
    r = str(input('Deseja continuar ? [S/N] ')).upper()
    if (r == 'S'):
        print('Vamos continuar')
    elif(r != 'N'):
        break
    else:
        break
    escolha = int(input('Escolha [1] para pedra, [2] para papel e [3] para tesoura '))
    if(escolha > 3):
        print('ERROR')
        break
    elif(escolha <= -1):
        print('ERROR')
        break


    print ('')
    time.sleep(1)
    def_ppt.bem_vindo('Pedra')
    print('')
    time.sleep(1)
    def_ppt.bem_vindo('Papel')
    print ('')
    time.sleep(1)
    def_ppt.bem_vindo('tesoura')
    print('')

    computador = random.randrange(1,3)
    time.sleep(1)
    if (computador == 1):
        print('O computador escolheu : PEDRA ') 
        if (escolha == 1):
            print('Houve empate')
        elif (escolha == 2):
            print('Você ganhou')
        elif (escolha == 3):
            print('Você perdeu')
        
    elif (computador == 2):
        print('O computador escolheu : PAPEL')
        if (escolha == 2):
            print('Houve empate')
        elif (escolha == 3):
            print('Você ganhou')
        elif (escolha == 1):
            print('Você perdeu') 

    elif (computador == 3):
        print('O computador escolheu : TESOURA')
        if (escolha == 3):
            print('Houve empate')
        elif (escolha == 1):
            print('Você ganhou')
        elif (escolha == 2):
            print('Você perdeu')
    else:
        break