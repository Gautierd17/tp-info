#SHCHERBAKOVA Iuliia --- SESI 53 --- 2015/16
#TP 8 http://www.fil.univ-lille1.fr/~L1S1Info/Doc/HTML/tp_numeration_shadok.html
#TP 8 : L’alphabet shadok

GA = chr(0x004F)
BU = chr(0x2212)
ZO = chr(0x2A3C)
MEU = chr(0x25FF)

ALPHABET_SHADOK = [GA,BU,ZO,MEU]

def entier_en_shadok(d):
    assert(type(d) is int and d >= 0), "d doit  Ãªtre entre entier positif ou nul"

    if d == 0:
        return GA
    else:
        D = d
        r = ''
        while D >= 1:
            r = ALPHABET_SHADOK[D % 4] + r
            D = D // 4
        return r

def shadok_en_entier_1(s):
    if s == GA:
        return 0
    elif s == BU:
        return 1
    elif s == ZO:
        return 2
    elif s == MEU:
        return 3
    else:
        assert(False)

def shadok_en_entier(s):
    S = s
    d = 0
    if len(S) > 0:
        for i in range(-1, -len(S) - 1, -1):
            d += shadok_en_entier_1(S[i]) * 4 ** (-i - 1)
    return d

def octet_en_shadok(o):
    assert(type(o) is int and o < 256)
    s = entier_en_shadok(o)
    while len(s) < 4:
        s = GA + s
    return s

def code_car_en_shadok(c):
    assert(type(c) is str and len(c) == 1)
    return octet_en_shadok(ord(c))

def code_en_shadok(s):
    assert(type(s) is str)
    r = ''
    for i in s:
        r += code_car_en_shadok(i)
    return r

def decode_car_du_shadok(s):
    assert(type(s) is str and len(s) == 4)
    d = shadok_en_entier(s)
    assert(d < 128)
    return chr(d)

def decode_du_shadok(s):
    assert(type(s) is str and len(s)%4 == 0)
    r = ''
    
    for i in range(0, len(s), 4):
        r += decode_car_du_shadok(s[i:i+4])
    return r    
