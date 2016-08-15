# SHCHERBAKOVA Iuliia
# GPE 45 Info/EEA
# liste_alea

import random
from random import shuffle

def liste_alea_():
    t = 1
    nmax = 101
    rev = list(range(t,nmax))
    random.shuffle(rev)
    print(rev)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("liste_alea_()", setup="from __main__ import liste_alea_", number=5000))    

