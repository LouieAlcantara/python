w = 3
while w < 13:
    print(w)
    w = w + 1
print('fim')

n = 1
while n != 0:
    n = int(input('digite um valor'))
print ('fim')

r = 'S'
while r == 'S':
    n = int(input('digite um valor'))
    r = str(input('quer continuar? [S/N] ')).upper()
print('fim')

j = 1
par = impar = 0
while j != 0:
    j = int(input('digite um numero '))
    if j % 2 == 0:
        par +=1
    else:
        impar += 1
print('voce digitou {} numeros pares e {} numeros impares'.format(par, impar))