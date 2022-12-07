import random
inp = input('-> ')
leninp = len(inp)
rand = random.randint(leninp-10,leninp)
for a in range(len(inp)):
    if a <= rand:
        inp[a] = '#'
print(inp)