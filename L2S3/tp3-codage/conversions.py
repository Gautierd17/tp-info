import struct
import io

###Remarque:
##Je ne reecris pas les conditions d'utilistation d'un certain parametre tant que je l'ecris deja dans "la description du parametre".(comme en AP2)
def integer_to_digit(n):
    """
    Convert an integer in a hexadecimal digit.

    :param n: natural number included in [0..15]
    :type n: int
    :return: the hexadecimal number of n
    :rtype: str
    :UC: None

    :Examples:
     >>> integer_to_digit(15)
     'F'
     >>> integer_to_digit(0)
     '0'

     """
    assert isinstance(n, int) and 0<= n<= 15, 'parameter n is a natural number included in [0..15]'

    if 0<= n<= 9:
        return chr(ord('0') + n)
    else:
        return chr(ord('7') + n)

def integer_to_string(n, b):
    """
    Gives the representation in base base of the integer integer.

    :param n: the integer we want to represent
    :type n: int
    :param b: natural number representing the base (2, 8, 16, 10)
    :type: int
    :return: the writing of the integer n in base b
    :rtype: string
    :UC: None

    :Examples:
    >>> integer_to_string(1331,16)
    '533'
    >>> integer_to_string(31415,16)
    '7AB7'
    >>> integer_to_string(12,8)
    '14'
    >>> integer_to_string(12,2)
    '1100'

    """
    assert isinstance(n,int) and n>=0, 'parameter n is a natural number'
    assert isinstance(b, int) and b in [2,8,16,10], 'parameter b is a natural number and it represents a base'

    if b==2:
        return bin(n)[2:]
    elif b==8:
        return oct(n)[2:]
    elif b==10:
        return n
    else:
        return hex(n)[2:].upper()

def tableau():
    for n in range(21):
        print('{:2d} : {:5s} {:2s} {:2s}'.format(n, integer_to_string(n,2), integer_to_string(n,8), integer_to_string(n, 16)))


def power_two(n):
    """
    Compute 2^n
    
    :param n: a natural number_ the power of two
    :type n: int
    :return: The value of 2^n
    :rtype: int
    :UC: None

    :Examples:
    >>> power_two(0)
    1
    >>> power_two(10)
    1024
    """
    assert isinstance(n,int) and n>=0, ' parameter n is a natural number'

    if n==0:
        p=1
    else:
        p = power_two(n-1) << 1
    return p
    


def integer_to_binary_str(n):
    """
    Get a binary representation of an integer.

    :param n: a natural number – the integer to be converted in binary
    :type n: int
    :return: the binary representation (as a string) of n
    :rtype:str
    :UC: None

    :Examples:
    >>> integer_to_binary_str(0)
    '0'
    >>> integer_to_binary_str(4)
    '100'
    >>> integer_to_binary_str(15)
    '1111'
    """

    assert isinstance(n, int) and n>=0, 'parameter n is a natural number'
    
    b=n
    s=''
    if b==0:
        return str(b)
    while b!=0:
        s=str(b%2)+s
        b=b//2
    return s

def binary_str_to_integer(s):
    """
    Inverse function of conversions.integer_to_binary_str().

    :param s: string composed only of 0s or 1s _ the input binary string
    :type n: str
    :return: The integer whose binary representation is s
    :rtype:int
    :UC: None

    :Examples:
    >>> binary_str_to_integer('0')
    0
    >>> binary_str_to_integer('10')
    2
    >>> binary_str_to_integer('1111')
    15
    """
    assert isinstance(s, str), 'parameter s is a string'
    p=0
    for i in range (len(s)):
        assert s[i] in ['0','1'], 'parameter s represents a binary number'
        p=p+(int(s[i])*2**(len(s)-i-1))
    return p
        
    
def byte_to_binary(byte):
    """
    Get the binary representation of a byte.

    :param byte: a whole numbre < 256 – The byte to be conerted to binary
    :type byte: int
    :return: The binary representation, as a string of length 8, of byte.
    :rtype: str
    :UC: None

    :Examples:	
    >>> byte_to_binary(1)
    '00000001'
    >>> byte_to_binary(255)
    '11111111'
    """
    assert isinstance(byte,int) and byte >= 0 and byte < 256, 'parameter byte must be in range of [0,255]'

    s= integer_to_binary_str(byte)
    return '0'*(8-len(s))+s
    



def float_to_bin(f):
    """
    Get the binary representation of a float (the struct.pack() method should be used).

    :param f: The float to be converted
    :type f: float
    :return: The binary representation according to the IEEE-754 32-bit encoding
    :rtype: str
    CU:	None

    :Examples:
    >>> float_to_bin(3.5)
    '01000000011000000000000000000000'
    """
    assert isinstance(f,float),'parameter f must be a float'
    
    s=''
    bytes_stored = struct.pack('>f', f)

    for i in range(len(bytes_stored)):
        s=s+byte_to_binary(bytes_stored[i])
    return s


def change_a_bit(s, x):
    """
    Changes a bit in a binary string.

    
    :param s: a binary string
    :type s: str
    :param x: The position at which the bit must be changed in binary.
    :type x: int
    :return: The modified binary string where the bit at position position has bee changed
    :rtype: str
    :UC: 0 <= x < len(s)
    
    :Examples:	
    >>> change_a_bit('0110', 0)
    '1110'
    >>> change_a_bit('0110', 1)
    '0010'
    """
    assert isinstance(s, str), 'parameter s must be a string'
    for i in range(len(s)):
        assert s[i] in ['0','1'], 'parameter s must be a binary'
    assert isinstance(x, int) and 0 <= x < len(s)

    l= list(s)
    if l[x]=='0':
        l[x]='1'
    else:
        l[x]='0'
    return ''.join(l)

def binary_to_bytes(s):
    """
    Get a list of bytes corresponding to a binary string.

    :param s: a binary string representing one or several bytes
    :type s: str
    :return: a list of  bytes. We assume that the binary string is encoded in big endian
    :rtype: list
    :UC: None

    :Examples:
    >>> binary_to_bytes('11010110')
    [214]
    >>> binary_to_bytes('110101101101011111011000')
    [214, 215, 216]
    """
    assert isinstance(s, str), 'parameter s must be a string'
    for i in range(len(s)):
         assert s[i] in ['0','1'], 'parameter s must be a binary'  #optimiser dans une fonction
    
    if len(s)%8!=0:
        p=('0'*(8-(len(s)%8)))+s
    else:
        p=s
    l=[]
    k=0
    for i in range(8,len(p)+1,8):
        l=l+[binary_str_to_integer(p[k:i])]
        k=i
    return l

def change_a_bit_in_float(f, x):
    """
    Changes a bit in the IEEE-754 32-bit float representation. Uses the struct.unpack() method.
    :param f: the float we want to modify
    :type f: float
    :param x: a whole number < 32 -the position (in the binary IEE-754 representation) where the bit will be modifie
    :type x: int
    :return: the value of f where the bit at position x in its IEE-754 binary representation has been changed
    :type r: float
    :UC: None

    :Examples:
    >>> '%.2f' % change_a_bit_in_float(3.14, 0)
    '-3.14'
    """
    d= struct.pack('>f',f)
    l=list(d)
    p=x//8
    l[p]=binary_str_to_integer(change_a_bit(byte_to_binary(l[p]), x % 8))
    return struct.unpack('>f', bytes(l))
    

##with open('data.txt', 'r') as stream_text:
##    content_text= stream_text.read()
##with open('data.txt', 'rb') as stream_bin:
##    content_bin= stream_bin.read()
##with open('data.out', 'wb') as output:
##    output.write(bytes([195, 137]))

def isolatin_to_utf8(flux):
    """
    Converts the first ISO-8859-1 character from the input stream to a UTF-8 character.

    :param flux: The input flux opened in binary mode for reading
    :type flux: io.BufferedReader
    :Return: A tuple containing one or two bytes representing the UTF-8 character which corresponds to the ISO-8859-1 read in the input stream. If the end of file is reached, None will be returned.
    :rtype: tuple
    :UC: None

    """
    assert type(flux) == io.BufferedReader
    
    try:
        byte= flux.read(1)[0]
        bit_poid_ford= byte>>7
        if bit_poid_ford==0:
            return (byte,)
        else:
            return ((0b11000000 | (byte>>6)) , int(0b10111111) & byte)
    except IndexError:
        flux.close()
        return None


def convert_file(source, dest, conversion):
    '''
    Convert `source` file using the `conversion` function and writes the
    output in the `dest` file.

    :param source: The name of the source file
    :type source: str
    :param dest: The name of the destination file
    :type dest: str
    :param conversion: A function which takes in parameter a stream (opened\
    in read and binary modes) and which returns a tuple of bytes.
    :type conversion: function
    '''
    entree = open(source, 'rb')
    sortie = open(dest, 'wb')

    octets_sortie = conversion(entree)
    while octets_sortie != None:
        sortie.write(bytes(octets_sortie))
        octets_sortie = conversion(entree)
    sortie.close()

def convert_file_isolatin_utf8(source, dest):
    '''
    Converts `source` file from ISO-8859-1 encoding to UTF-8.
    The output is written in the `dest` file.

    examples:
    >>> convert_file_isolatin_utf8('cigale-ISO-8859-1.txt', 'cigale-iso-utf.txt')
    '''
    convert_file(source, dest, isolatin_to_utf8)
    
def utf8_to_isolatin(flux):
    """
    Converts the first UTF-8 character from the input stream to a ISO-8859-1 character.

    :param flux: The input stream opened in binary mode for reading
    :type flux: io.BufferedReader
    :return: A tuple containing a single value: the byte representing the ISO-88591-1 character which corresponds to the UTF-8 character read in the input. If the end of the file is reached, None will be returned.
    :rtype: tuple
    :UC: None
    """
    assert type(flux) == io.BufferedReader

    try:
        byte1= flux.read(1)[0]
        if byte1 >> 7==0:
            return (byte1,)
        elif byte1 >> 5== 0b110:
            byte2= flux.read(1)[0]
            s= (byte1 & 0b11)<<6 | (byte2 & (0b00111111))
            return (s,)
        
    except IndexError:
        flux.close()
        return None
    

def conversion_file_utf8_isolatin(source, dest):
    '''
    Converts `source` file from UTF-8 encoding to ISO-8859-1.
    The output is written in the `dest` file.

    :Examples:
    conversion_file_utf8_isolatin('cigale-UTF-8.txt', 'cigale-utf-iso.txt')
    '''
    convert_file(source, dest, utf8_to_isolatin)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
