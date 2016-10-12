### BENZINA Amina
### SHCHERBAKOVA Iuliia

from conversions import *

### Codage d’un fichier en base 64
BASE64_SYMBOLS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                  'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                  'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                  'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                  'w', 'x', 'y', 'z', '0', '1', '2', '3',
                  '4', '5', '6', '7', '8', '9', '+', '/']

### Question 4
def bytes_to_symbols(l):
    """
    Takes (at most) three bytes of data in input and returns the corresponding bas64 symbols.
    :param l: list of at most three bytes
    :return: Four base64 symbols (or ‘=’) corresponding to the data given in input
    :type return: str
    :UC: len(data) <= 3
    :examples:
    >>> bytes_to_symbols([5])
    'BQ=='
    >>> bytes_to_symbols([4, 163])
    'BKM='
    """
    if len(l)==0:
        return t
    p=''
    for i in range(len(l)):
        assert type(l[i])== int and l[i]<(2**8)
        b = bin(l[i])
        s = b[2:]
        
    
        s= (8-len(s))*'0'+s
        p=p+s
    t=''
    k=0
    
    if len(l)==1:
        p=p+'0'*4
    elif len(l)==2:
        p=p+'0'*2
    #si la longueur est >0
    for i in range(6,len(p)+1,6):
            t=t+BASE64_SYMBOLS[binary_str_to_integer(p[k:i])]
            k=i
    return t+('='* (4-len(t)))
    
### Question 6
def base64_encode(source):
    '''
    Encode a file in base64 and outputs the result on standard output.

    :param source: the source filename
    :type source: str
    '''

    input = open(source, 'rb')
    data = input.read(3)
    nb = 0  
    while len(data) > 0:
        if nb==76:
            print (bytes_to_symbols(data), end='\n')
            data = input.read(3)
            nb=4          
        print (bytes_to_symbols(data), end='')
        nb+=4
        data = input.read(3)
        
    print()
    input.close();


### Décodage d’un fichier au format base 64
### Question 7
def decode_base64_symbol(s):
    """
    Convert a base64 symbol in integer.
    :param s: symbol(str)
    :return: the integer corresponding to base64 symbol
    :return type: int
    :CU: the symbol is part of the base64 symbols
    :examples:
    >>> decode_base64_symbol('A')
    0
    >>> decode_base64_symbol('Z')
    25
    """
    assert len(s)==1 and s in BASE64_SYMBOLS, 'the symbol is not part of base64'
    return BASE64_SYMBOLS.index(s)

### Question 7
def symbols_to_bytes(s):
    """
    Convert base64 symbols to bytes.
    :param s: a string of four base64 symbols (and maybe the = sign)
    :return: a list of one to 3 bytes whose values correspond to the base64 symbols
    :type return: list
    :UC: len(s) == 4
    :examples:
    >>> symbols_to_bytes('BQ==')
    [5]
    >>> symbols_to_bytes('BKM=')
    [4, 163]
    >>> symbols_to_bytes('HFll')
    [28, 89, 101]
    """
    assert len(s) == 4
    p=''
    i=0
    while i<len(s) and s[i]!='=':
        d= decode_base64_symbol(s[i])
        r= bin(d)[2:]
        r= (6-len(r))*'0' + r
        p=p+r
        i=i+1
    p= binary_str_to_integer(p)
    nb= s.count('=')
    p= p >> (nb*2)
    l=[]
    while p>0:
        l.insert(0, p%(2**8))
        p= p>>8
    return l

### Question 9
def process_base64_line(s):
    """
    Process a line from a base64 input and writes the conversion on the output
    :param line: line of a base64 output
    :UC: len(line) % 4 == 0 and the line only contains base64 symbols (or possibly = signs)
    :examples:
    >>> process_base64_line('eW91ciB0ZXh0')
    'your text'
    >>> process_base64_line('Q29kYWdl')
    Codage
    >>> process_base64_line('Q29kYWdlcw==')
    Codages
    >>> process_base64_line('Q29kYWdlcy4=')
    Codages.
    """
    assert len(s)%4==0
    for i in (s):
        assert i in BASE64_SYMBOLS or i=='=' or i== '\n'
    k=0
    for i in range(4,len(s)+1,4):
        for f in symbols_to_bytes(s[k:i]):
            print(chr(f), end='')   
        k=i
         

### Question 10            
def base64_decode(source):
    """
    Decode a source file encoded in base64 and output the result.
    :param source: source (str) – the filename of the base64 file to decode
    :UC: None
    :return: converted from the base64 file as string.
    """
    assert type(source)==str
    with open(source, 'r') as inp:
        
        s= inp.read(1)
        line=''
        while len(s)>0:
            line=line+s
            s= inp.read(1)
            if not s in BASE64_SYMBOLS:
                s=inp.read(1)
        process_base64_line(line)
            
