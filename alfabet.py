a = list('abcdefghijklmnopqrstuvwxyz \'')
b = input('give your string(all lower)\n: ')
c = []
e = ''
for d in b:
    try:
        c.append(a.index(d))
    except:
        pass
print(c)
for d in c:
    e += a[d]
print(e)
