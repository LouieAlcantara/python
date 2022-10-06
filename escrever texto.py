#nao alinhado
def mensagem(pal):
    p= len(pal)
    print('-'*p)
    print(pal)
    print('-'*p)


mensagem('Menu principal')
mensagem('contato')
mensagem('saida')


#alinhado
def texto(txt):
    b= len(txt)+4
    print('-'*b)
    print(f'  {txt}')
    print('-'*b)

texto('eu sou batman')
texto('parabens')