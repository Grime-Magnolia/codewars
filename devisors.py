max = 10000
def get(arg):
    b = []
    for a in range(1,max):
        a+=1
        c = arg/a
        if type(c) == int and c != 0 and c != 1 and a != arg:
            b.append(arg/a)
    return b
print(get(int(input('->'))))