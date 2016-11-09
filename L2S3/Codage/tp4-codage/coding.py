'''
Coding module.

@author FIL - IEEA - Univ. Lille1 (oct 2010, août 2015)
'''

class Not_coding(Exception):
    '''
    Exception raised by `coding.create`.
    '''
    pass

class Not_codable_symbol(Exception):
    '''
    Exception raised by `coding.Coding.code`.
    '''
    pass

class Undecodable_word(Exception):
    '''
    Exception raised by `coding.Coding.decode`.
    '''
    pass


def create(alphabet, code):
    '''
    Creates a coding for the given alphabet and code.

    :param alphabet: a list of symbols
    :type alphabet: list
    :param code: a list of codewords
    :type list:
    :return: a Coding object, which represents a coding
    :rtype: Coding
    :CU: len(alphabet) == len(code) and alphabet and code don't contain twice\
    the same element. Raises exception `coding.Not_coding`.
    :Examples:

    >>> create(['a', 'b'], ['00', '1']).code('a')
    '00'
    >>> create([], ['00'])
    Traceback (most recent call last):
    ...
    Not_coding: The number of symbols in the alphabet differs from the number of codewords 
    >>> create(['a'], [''])
    Traceback (most recent call last):
    ...
    Not_coding: Empty word not allowed
    >>> create(['a', 'a'], ['0', '1'])
    Traceback (most recent call last):
    ...
    Not_coding: Symbol a appears twice in the alphabet
    >>> create(['a', 'b'], ['0', '0'])
    Traceback (most recent call last):
    ...
    Not_coding: Codeword 0 appears twice in the code
    '''
    taille_alphabet = len(alphabet)
    codage = {}
    decodage = {}
    if taille_alphabet != len(code):
        raise Not_coding('The number of symbols in the alphabet differs from the number of codewords')
    else:
        for i in range(taille_alphabet):
            symbole = alphabet[i]
            mot = code[i]
            if mot == "":
                raise Not_coding('Empty word not allowed')
            elif symbole in codage:
                raise Not_coding('Symbol %s appears twice in the alphabet' % symbole)
            elif mot in decodage:
                raise Not_coding('Codeword %s appears twice in the code' % mot)
            else:
                codage[symbole] = mot
                decodage[mot] = symbole
        return Coding(codage, decodage)

class Coding:
    '''
    The `Coding` type allows to code symbols with specified codewords (or to
    decode them).
    '''
    _table_codage={}
    _table_decodage={}

    def __init__(self, table_codage = {}, table_decodage = {}):
        self._table_codage = table_codage
        self._table_decodage = table_decodage

    def alphabet(self):
        '''
        Get the source alphabet

        :return: the alphabet associated with the coding
        :rtype: list
        :Examples:

        >>> coding1 = create(['a', 'b'], ['00', '01'])
        >>> coding1.alphabet()
        ['a', 'b']
        '''
        return sorted(list(self._table_codage.keys()))

    def code(self, symbol):
        '''
        Codes the provided symbol

        :param symbol: the symbol to be coded
        :type symbol: str
        :return: The corresponding codeword
        :rtype: str
        :CU: symbol belongs to the alphabet, otherwise Not_codable_symbol
        exception is raised

        :Examples:
        >>> coding1 = create(['a', 'b'], ['00', '01'])
        >>> coding1.code('a')
        '00'
        >>> coding1.code('c')
        Traceback (most recent call last):
        ...
        Not_codable_symbol
        '''
        if symbol not in self._table_codage:
            raise Not_codable_symbol()
      
        return self._table_codage[symbol]

    def decode(self, word):
        '''
        Decodes a codeword.

        :param word: The word is a codeword from the code.
        :type word: str
        :return: the corresponding symbol from the alphabet
        :rtype: str
        :CU: The word must belongs to the code, otherwise Undecodable_word
        exception is raised.
        :Examples:

        >>> coding1 = create(['a', 'b'], ['00', '01'])
        >>> coding1.decode('01')
        'b'
        >>> coding1.decode('11')
        Traceback (most recent call last):
        ...
        Undecodable_word
        '''
        if word not in self._table_decodage:
            raise Undecodable_word()
        return self._table_decodage[word]
