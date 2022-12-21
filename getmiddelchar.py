def get(arg):
    arg = list(arg)
    lenarg = len(arg)
    #TYGO JE KUNT EEN VARIABLE NIET GEWOON 'A' OF 'B  NOEMEN!!!!!!!!!!!!!!!!!!!!'
    a = float(lenarg/2)
    if '.0 ' in str(a)+' ':
        return [arg[int(a-0.5)],arg[int(a+0.5)]]
    else:
        return [arg[int(a)]]
print(get(input('~>')))
