def conv(n):
    """
    Converts a digit to binary.
    :param n: int
    :return: converted number
    """
    assert type(n) == int, 'enter a number'
    if type(n) is not int:
        raise AssertionError
    return bin(n)

def integer_to_digit(n):
    """
    Converts integer to digit number.
    :param n: int, number to convert between 0 and 15.
    :return: new number of letter
    :examples:
    >>> integer_to_digit(15)
    'F'
    >>> integer_to_digit(0)
    '0'
    """
    assert 0 <= n <= 15, 'enter numbers between 0 and 15 incl.'
    if 0 <= n <= 9:
        res = chr(ord('0') + n)
    elif n > 9:
        res = chr(ord('7') + n)
    else:
        raise AssertionError
    return res

def integer_to_string(n,b):
    """
    Converts a number to bin, oct or hex system.
    :param n: int, number to convert
    :param b: int, 2/8/16
    :return: converted number
    """
    assert b == 2 or b == 8 or b == 16, 'enter 2, 8 or 16'
    if b == 2:
        return bin(n)
    elif b == 8:
        return oct(n)
    elif b == 16:
        return hex(n)
    else:
        return AssertionError

def deux_puissance(n):
    """
    Returns 2**n.
    """
    return 1 << n

def pair(number):
    assert isinstance(number, int), 'use numbers'
    if number & 1:
        print('impair')
    elif (number & 1) == 0:
        print('pair')
    else:
        raise AssertionError
    

def integer_to_binary_str(s):
    return str(s) if s<=1 else integer_to_binary_str(s>>1) + str(s&1)

def binary_str_to_integer(b):
    return int(b,2)

def byte_to_binary(n):
    b = 2147483648;
    str=''
    while b > 0:
        z = n & b;
        if z == 0:
             str=str+'0'
        else:
             str=str+'1'
        b = b >> 1;
    print (str)

import struct
def float_to_bin(num):
    return bin(struct.unpack('!I', struct.pack('!f', num))[0])[2:].zfill(32)

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, 'big')

s = "110101101101011111011000"
print(bitstring_to_bytes(s))    
