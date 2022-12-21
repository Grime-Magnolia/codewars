import random
class encode():
    def __init__(self):
        self.alfabet = '6]ú0nfæ+»gFVK;yáéx!lT#^U{«q[%,G}Q4R&m27Aa%dpäðßzDe(ü-1þµí/8¥þS=>Lö¶¿btohJ×H®_.\"OCB<?NñwµIMå9)ç|ZiX3PWusvø$:Y5óc\'*¬Ejr@k'
        self.allkeys = {}
        for self.num,loop in enumerate(self.alfabet):
            self.allkeys[loop] = self.num
    def make(self,string1,yourkey):
        returnman = ''
        for abc in string1:
            count = list(self.allkeys).index(abc) + yourkey
            if count > len(list(self.allkeys)):
                count-=len(list(self.allkeys))
            returnman+=self.allkeys[list(self.allkeys)[count]]
key = random.randint(1,99999)
encode.make(input('your encoded string->'),)