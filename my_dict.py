from datetime import datetime 

hora_atual = datetime.now()
h = hora_atual.strftime('%H')

my_dict = {
    'manha':'bomdia',
    'tarde':'boatarde',
    'noite':'boanoite'
}

if int(h)>=1 and int(h)< 12:
    print(my_dict['manha'])
elif int(h) >=12 and int(h) < 18:
    print(my_dict['tarde'])
else:
    print(my_dict['noite'])

dicio ={
    'pt': 'dale lula',
    'patriota':'la vai o bolsonario',
    'outro':'la vai o ciro'
}
x = input('qual é sua opnião politica?[pt,patriota,outro]')
print (dicio[x])
