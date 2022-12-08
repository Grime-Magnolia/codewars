def get(arg):
    arg = list(arg)
    lenarg = len(arg)
    a = float(lenarg/2)
    if '.0 ' in str(a)+' ':
        return [arg[int(a-0.5)],arg[int(a+0.5)]]
    else:
        return [arg[int(a)]]
print(get(input('~>')))