def get(arg):
    count = {}
    a = ''
    for b in arg:
        if b in count:
            count.update({b:count[b]+1})
        else:
            count.update({b:1})
    for b in arg:
        if count[b] > 1:
            a += ')'
        else:
            a += '('
    return a
print(get('abcdefggfedcb'))