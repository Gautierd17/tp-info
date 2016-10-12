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
def  base64_encode(source):
    '''
    Encode a file in base64 and outputs the result on standard output.

    :param source: the source filename
    :type source: str
    '''
    input = open(source, 'rb')
    data = input.read(3)
    nb = 4   #4 car le programme lit 3 caracteres à chaque fois ce qui represente 4 code en base64
    while len(data) > 0:
        if nb==76:
            print (bytes_to_symbols(data), end='\n')
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
    assert s in BASE64_SYMBOLS, 'the symbol is not part of base64'
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
    nb= s.count('=')
    p= p[:len(s)-nb*2]
    return binary_to_bytes(p)
    
### Question 9,10
dictn = dict(zip(BASE64_SYMBOLS, range(len(BASE64_SYMBOLS))))        
def process_base64_line(line):
    """
    Process a line from a base64 input and writes the conversion on the output
    :param line: line of a base64 output
    :UC: len(line) % 4 == 0 and the line only contains base64 symbols (or possibly = signs)
    :example:
    >>> process_base64_line('eW91ciB0ZXh0')
    'your text'
    """
    assert len(line) % 4 == 0 and type(line) == str
    new_list = []
    for ch in line:
        if ch == "=":
            break
        try:
            new_list.append(dictn[ch])
        except:
            pass
        pass
    data = ""
    long_line = len(new_list) % 4 
    if long_line > 0:
        new_list += [0] * (4 - long_line)

    for i in range(0, len(new_list), 4):
        b3 = (new_list[i] << 18) | (new_list[i + 1] << 12) | (new_list[i + 2] << 6) | new_list[i + 3]
        data += chr(b3 >> 16) + chr((b3 >> 8) & 0xff) + chr(b3 & 0xff)
        pass
    return data[:-long_line] if long_line > 0 else data    


### Réalisation de l’utilitaire base64
### Question 11

'''
   Encoding and decoding utility for base64 files.
   Requires the codage64 module.

   @author FIL - UFR IEEA - Univ. Lille1 (oct 2010, sept. 2015)
'''

import codage64
import sys

def usage():
    '''
    prints how to use the program
    '''
    print("Usage : %s [-e|-d] <fichier>\n" % sys.argv[0], file=sys.stderr)
    print("\t -e pour encoder\n\t -d pour decoder\n", file = sys.stderr)
    exit(1)

def main():
  if len(sys.argv) != 3:
      usage()
  else:
      option = sys.argv[1]
      file = sys.argv[2]
      if option == "-e":
          codage64.base64_encode(file)
      elif option == "-d":
          codage64.base64_decode(file)
      else:
          usage()

if __name__ == '__main__':
    main()            

