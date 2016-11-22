from coding import *
from tp2 import binary_to_bytes, byte_to_binary

### defining constants
source_alphabet = \
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',\
     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
code1 = \
[ "00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111",
  "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111",
  "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111",
  "11000", "11001", "11111" ]

code2 = \
[".-/", "-.../", "-.-./", "-../", "./", "..-./", "--./", "..../", "../",
 ".---/", "-.-/", ".-../", "--/", "-./", "---/", ".--./", "--.-/", ".-./",
 ".../", "-/", "..-/", "...-/", ".--/", "-..-/", "-.--/", "--../", "---./"]

code3 = \
["1010", "0010011", "01001", "01110", "110", "0111100", "0111110",
 "0010010", "1000", "011111110", "011111111001", "0001", "00101",
 "1001", "0000", "01000", "0111101", "0101", "1011", "0110", "0011",
 "001000", "011111111000", "01111110", "0111111111", "01111111101",
 "111"]

### question 6
### on déclare trois variables coding1,coding2,coding3
coding1=create(source_alphabet,code1)
coding2=create(source_alphabet,code2)
coding3=create(source_alphabet,code3)

### question 7
### fait

### question 8
def code_word(word,my_coding):
    """
    Code a word with the provided coding
    
    :param word: the word to be coded
    :type(word): str
    :param my_coding: the coding to use for coding the word
    :type(my_coding): Coding
    :return: coded word with my_coding
    :type return: str
    :UC: symbols in the word are in the source alphabet of the coding
    :examples:
    
    >>> code_word('', coding1)
    ''
    >>> code_word('ABCD', coding1)
    '00000000010001000011'
    >>> code_word(' ZA', coding1)
    '111111100100000'
    """
    assert isinstance(word,str), 'Not a string passed as parameter'
    word=list(word)
    l=[]
    for item in word:
        app_num = my_coding.code(item)
        l.append(app_num)
    return "".join(str(x) for x in l)  

### question 11
def decode_fixed_length_word(codeword, my_coding):
    if len(codeword)%5 != 0:
         raise Undecodable_word('decode_fixed_length_word: undecodable word')
    n=5
    num_list = [codeword[i:i+n] for i in range(0, len(codeword), n)]
    l=[]
    for item in num_list:
        app_lett = my_coding.decode(item)
        l.append(app_lett)
    return "".join(str(x) for x in l)

### question 15
def decode_comma_word(word, comma, my_coding):
    if not word[-1] == comma:
        raise Undecodable_word('decode_comma_word: comma not found, cannot decode the word')
    split_list = word.split(comma)
    l=[]
    for item in split_list:
        if item=='':
            res= ''
        else:
            res = item+comma
            l.append(res)
    list_items = [item for item in l]
    lst=[]
    for items in list_items:
        app_num = my_coding.decode(items)
        lst.append(app_num)
    return "".join(str(x) for x in lst)  
        

def decode_prefix_letter(word, my_coding):
    '''
    Decodes the first letter of the word, assuming a prefix coding was used.

    :param word: A word that was coded using `coding`
    :type word: str
    :param my_coding: The coding used for (de)coding
    :type my_coding: coding.Coding
    :return: a tuple whose elements are: 1) the symbol associated with the\
    first decodable prefix 2) the length of the first decodable prefix
    :rtype: tuple
    :CU: `word` was coded using `my_coding`
    :Examples:

    >>> decode_prefix_letter("0010010", coding3)
    ('H', 7)
    >>> decode_prefix_letter("00100101000", coding3)
    ('H', 7)
    >>> decode_prefix_letter("00", coding3)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_prefix_letter: no decodable prefix
    '''
    word_length = len(word)
    for i in range(1,word_length+1):
        try:
            prefix = my_coding.decode(word[:i])
            return (prefix, i)
        except:
            pass
    #raise Undecodable_word("decode_prefix_letter: no decodable prefix")

### question 18
def decode_prefix_word(word, my_coding):
    l=[]
    while len(word)>=2: #2 c'est la plus petite longueur d'un symbole parmi des listes code1,code2,code3.
        element = decode_prefix_letter(word,my_coding)[0]
        position = decode_prefix_letter(word,my_coding)[1]
        word = word[position:]
        decode_prefix_letter(word,my_coding)
        l.append(element)
        res = "".join(str(x) for x in l)
        if len(word)<2:
            break
    return res
import os
### question 20
def write_bits(stream, bits):
    r = len(bits) % 8
    
    if r:
        wrt = bits[:-r]
    else:
        wrt = bits
    
    if wrt:
        wrt = binary_to_bytes(wrt) #list
        not_list = bytes(wrt)
        stream.write(not_list)
 
    return bits[-r:] if r else ''
    
    

##def write_bits(stream,bits):
##    with open(stream,'a') as f: 
##        res = len(bits)%8
##        if res!=0:
##            chaine = bits[:-res]
##            list_bytes = binary_to_bytes(chaine)
##            string = "".join(str(x) for x in list_bytes)
##            t = bytes(string.encode())
##            f.write(" {} ".format(t))
##            return bits[-res:]
##        else:
##            list_byte = binary_to_bytes(bits)
##            s = "".join(str(x) for x in list_byte)
##            t = bytes(s.encode())
##            f.write(" {} ".format(t))
##            return ""
    
### question 21
def complete_byte(bits):
    assert len(bits)<=8,'please enter less than 8 characters'
    if len(bits)==8:
        raise AssertionError('I cannot coplete a completed byte!')
    else:
        to_complete=8-len(bits)
        byte = bits+'1'+'0'*(to_complete-1)
        return byte
    
### question 22
def read_bits(stream):
    chunk = stream.read(1)
    
    if chunk: 
        return bin(chunk[0])[2:].zfill(8)
    return ''

### question 23
def uncomplete_byte(bits):
    assert len(bits)==8, 'I can only uncomplete a byte(8chars)'
    if not '1' in bits:
        raise AssertionError('I can only uncomplete a byte')
    else:
        inv_bits=bits[::-1]
        idx=inv_bits.index('1')
        rm_inv_bits=inv_bits[idx+1:]
        byte = rm_inv_bits[::-1]
        return byte
    
### question 24
### cette fonction fait appel à la fonction uncoplete_byte
### donc elle retourne une erreur si le nombre de chiffres à la fin d'un nombre 'bits' est inf. à 8    
def remove_completion(bits):
    assert len(bits)>=8, 'Please enter at least 8 characters'
    if not '1' in bits:
        raise AssertionError('I can only uncomplete a byte')
    else:
        byte=bits[8:]
        madelast = uncomplete_byte(byte)
        res = bits[:-8]+madelast
        return res
    
### version 2
### cette fonction ne fait pas d'appel à la fonction uncomplete_byte
### donc elle marche même si le nombre de chiffres à la fin est inf. à 8    
def remove_completion2(bits):
    assert len(bits)>=8, 'Please enter at least 8 characters'
    if not '1' in bits:
        raise AssertionError('I can only uncomplete a byte')
    else:
        inv_bits=bits[::-1]
        idx=inv_bits.index('1')
        rm_inv_bits=inv_bits[idx+1:]
        byte = rm_inv_bits[::-1]
        return byte    
        
### question 25
def flush_binary_string(binary, stream):
    '''
    Flush a binary string by writing as many bytes as possible in the output
    stream.

    :param binary: A binary string
    :type binary: str
    :param stream: An output stream
    :return: the bits that could not be written in the output stream (the\
    length of the returned string is necessarily < 8).
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> flush_binary_string('01000001', r)
    ''
    >>> r.seek(0);
    0
    >>> r.read().decode()
    'A'
    '''
    while len(binary) >= 8:
        binary = write_bits(stream, binary)
    return binary

def write_binary_string_in_file(binary, file):
    '''
    Write the binary string in the file (the string is written 8 bits per 8
    bits in the file).
    As the binary string can have any length, the last byte will be completed
    so that all the content could be written to the file.

    :param binary: a binary string
    :type binary: str
    :param file: The filename of the file where the binary string will be\
    written
    :type file: str
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_binary_string_in_file('01000001010', r.name)
    >>> r.seek(0);
    0
    >>> r.read().decode()
    'AP'
    '''
    out_file = open(file, 'wb')
    binary = flush_binary_string(binary, out_file)
    write_bits(out_file, complete_byte(binary))
    out_file.close()

def read_file(file):
    '''
    Read the data in the file and returns a binary string corresponding to
    that data.

    :param file: the filanem of the file to read.
    :type file: str
    :return: The binary string of the data that was stored in the file. The\
    completion will be removed from the binary string.
    :rtype: str
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_binary_string_in_file('01000001010', r.name)
    >>> r.seek(0);
    0
    >>> read_file(r.name)
    '01000001010'
    '''
    in_file = open(file, 'rb')
    bits = ''
    binaire = read_bits(in_file)
    while binaire != '':
        bits += binaire
        binaire = read_bits(in_file)
    in_file.close
    if len(bits) > 0:
        bits = remove_completion(bits)
    return bits

          
        

    
            
    
    
    
