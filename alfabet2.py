a = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \'1234567890-=_+`~!@#$$%%^&*(){}[]|\\;:\"\'/?<>,.')
b = input('give your string\n: ')
c = []
for d in a:
    b.replace(d,(' ',str(a.index(d)),' '))
print(b)
