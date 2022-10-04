from codecs import oem_decode
from mailbox import NotEmptyError
from string import octdigits


dicio={
    'nome':input('qual o seu nome'),
    'endereço':input('qual o seu endereço'),
    'data':input('qual o seu aniversario'),
    'cpf':input('qual o seu cpf'),
    'rg':input('qual o seu rg')
}
print(dicio.items())