def mult(x, num=2):
    return x, x*num

a,b = mult(2)
print(a,b)

a,b = mult(2, num=10)
print(a,b)

a,b = mult(3, 5)
print(a,b)