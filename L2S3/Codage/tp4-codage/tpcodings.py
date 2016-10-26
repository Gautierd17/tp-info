from coding import *

### constants
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
    for i in word  #///////////////////////
