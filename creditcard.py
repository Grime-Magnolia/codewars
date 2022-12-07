import random
inp = list(input('-> '))
leninp = len(inp)
b = ''
rand = leninp-4
for a in range(leninp):
    if a <= rand:
        inp[a] = '#'
for a in inp:
    b += a
print(b)