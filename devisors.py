max = 100000
def get(arg):
    b = []
    for a in range(max):
        a+=1
        c = float(arg/a)
        if '.0 ' in str(c)+' ' and c != 0 and c != 1 and a != arg and c != arg:
            b.append(int(arg/a))
    return b
print(get(int(input('->'))))