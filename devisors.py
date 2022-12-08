max = 10000
def get(arg):
    b = []
    for a in range(1,max):
        a+=1
        try:
            c = arg/a
            if is_integer(c) and c != 0 and c != 1 and a != arg:
                b.append(arg/a)
        except:
            pass
    return b
print(get(int(input('->'))))