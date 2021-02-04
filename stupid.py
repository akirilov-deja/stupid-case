import sys
import random

normal = ' '.join(sys.argv[1:])
stupid = ''
coin = False
dup = False

for i in range(len(normal)):
    if normal[i].isalpha():
        if dup:
            coin = not coin
            dup = False
        else:
            oldcoin = coin
            coin = random.randrange(2) == 0
            dup = (coin == oldcoin)
        if coin:
            stupid += normal[i].upper()
        else:
            stupid += normal[i].lower()
    else:
        stupid += normal[i]

print(stupid)
