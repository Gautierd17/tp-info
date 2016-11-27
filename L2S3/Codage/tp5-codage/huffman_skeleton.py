'''
Implantation de l'algorithme de Huffman

@author FIL - IEEA - Univ. Lille (août 2015)
'''

import doctest
import operator
from huffman_tree import HuffmanTree
import coding
import struct
from tpcodings import write_bits, read_bits, flush_binary_string
from collections import Counter

def symbol_occurrences(stream):
    '''
    Read the stream and count the occurrences of each symbol in the stream
    
    :param stream: a stream opened (in read mode and (possibly) in binary mode)
    :return: A dictionary whose keys are symbols and the associated values are\
    the corresponding number of occurrences
    :rtype: dict
    :Examples:
    
    >>> from io import StringIO # StringIO is used to have stream examples based on strings.
    >>> from io import BytesIO # BytesIO is used to have stream examples based on bytes.
    >>> symbol_occurrences(StringIO("ababcaba")) == {'c': 1, 'b': 3, 'a': 4}
    True
    >>> symbol_occurrences(BytesIO(b"ababcaba")) == {b'c': 1, b'b': 3, b'a': 4}
    True
    >>> symbol_occurrences(StringIO('aaaa')) == {'a': 4}
    True
    >>> symbol_occurrences(StringIO(''))
    {}
    >>> symbol_occurrences(StringIO('abcd')) == {'a': 1, 'b': 1, 'c': 1, 'd': 1}
    True
    >>> symbol_occurrences(BytesIO(b'abcd')) == {b'a': 1, b'b': 1, b'c': 1, b'd': 1}
    True
    '''
    l=[]
    byte=stream.read(1)
    for line in stream:
        for byte in line:
            l.append(byte)
    return dict(Counter(l))    
            
    
def create_forest(occurrences):
    '''
    Create the initial list of Huffman trees based on the dictionary of
    symbols given in parameter.
    
    :param occurrences: Number of occurrences of each symbol.
    :type occurrences: dict
    :return: A list sorted in ascending order on the number of occurrences\
    and on the symbols of Huffman trees of all symbols provided in\
    `occurrences`.
    :Examples: 

    >>> create_forest({'a': 4, 'c': 2, 'b': 1})
    [|b:1|, |c:2|, |a:4|]
    >>> create_forest({'e': 1, 'f': 1, 'g': 1, 'h': 1, 'a':2})
    [|e:1|, |f:1|, |g:1|, |h:1|, |a:2|]
    '''
    sorted_occs = sorted(occurrences.items(), key=lambda item: (item[1], item[0]))
    forest = [HuffmanTree(leaf[0], leaf[1]) for leaf in sorted_occs]
    return forest

def pop_least_element(list1, list2):
    '''
    Get and remove the lowest element from two lists sorted in ascending order.

    :param list1: First list sorted in ascending order
    :type list1: list
    :param list2: Second list sorted in ascending order
    :type list2: list
    :return: The lowest element among the two lists
    :UC: The two lists are sorted in ascending order and there is at least\
    one element among the two lists.
    :Examples:

    >>> pop_least_element([1], [2])
    1
    >>> pop_least_element([2], [1])
    1
    >>> pop_least_element([], [1])
    1
    >>> pop_least_element( [1], [])
    1
    '''
    assert(len(list1) + len(list2) >= 1)
    if len(list1) == 0:
        return list2.pop(0)
    if len(list2) == 0:
        return list1.pop(0)
    if list2[0] < list1[0]:
        return list2.pop(0)
    return list1.pop(0)

def create_huffman_tree(occurrences):
    '''
    Return a Huffman tree of the symbols given in `occurrences`.
    
    :param occurrences: Number of occurrences of each symbol.
    :type occurrences: dict
    :return: Return a single Huffman tree (obtained with Huffman algorithm)\
    of the symbols in `occurrences`.
    :rtype: huffman_tree.HuffmanTre
    :Examples:
    
    >>> create_huffman_tree({'a': 4, 'b': 1, 'c': 2})
    |bca:7|_<|bc:3|_<|b:1|, |c:2|>, |a:4|>
    >>> create_huffman_tree({'a': 1, 'b': 1, 'c': 2})
    |cab:4|_<|c:2|, |ab:2|_<|a:1|, |b:1|>>
    '''
    symbol_list = create_forest(occurrences)
    tree_list = []

    while len(tree_list) + len(symbol_list) != 1:
        (elem1, elem2) = (pop_least_element(symbol_list, tree_list),\
                          pop_least_element(symbol_list, tree_list))
        new_tree = HuffmanTree(left = elem1, right=elem2)
        tree_list.append(new_tree)

    if len(tree_list) == 1:
        return tree_list[0]
    return symbol_list[0]

def get_coding_from_tree(tree, code=''):
    '''
    Get the codes associated to the symbols.

    :param tree: A HuffmanTree
    :type tree: huffman_tree.HuffmanTree
    :param code: (optional parameter) the path that was followed to access the\
    current root of the tree
    :return: a list of tuples. Each tuple is made of a symbol and a code.\
    The order of the tuples in the list does not matter
    :rtype: list
    :Examples:

    >>> c=get_coding_from_tree(create_huffman_tree({'a': 4, 'b': 1, 'c': 2}))
    >>> len(c)
    3
    >>> c.count(('a', '1')) == 1
    True
    >>> c.count(('b', '00')) == 1
    True
    >>> c.count(('c', '01')) == 1
    True
    '''
    if tree.isLeaf():
        return [(tree.symbol, code)]
    return get_coding_from_tree(tree.left, code + '0') \
        + get_coding_from_tree(tree.right, code + '1')
    
def huffman_coding(tree):
    '''
    Creates a Huffman coding from a Huffman tree.

    :param tree: A Huffman tree
    :type tree: huffman_tree.HuffmanTree
    :return: A Huffman coding based on the Huffman tree given in parameter
    :rtype: coding.Coding
    :Examples:

    >>> c = huffman_coding(create_huffman_tree({'a': 4, 'b': 1, 'c': 2}))
    >>> c.code('a') + ' ' + c.code('b') + ' ' + c.code('c')
    '1 00 01'
    >>> c = huffman_coding(create_huffman_tree({'a': 1, 'b': 2, 'c': 3, 'd': 5}))
    >>> c.code('a') + ' ' + c.code('b') + ' ' + c.code('c') + ' '\
    + c.code('d')
    '110 111 10 0'
    '''
    result = get_coding_from_tree(tree, '')
    alphabet = list(map(lambda i: i[0], result))
    codes = list(map(lambda i: i[1], result))
    return coding.create(alphabet, codes)

import pickle
def write_occurrences(occurrences, filename):
    '''
    Write the symbol occurrences in the given file
    
    :param occurrences: The dictionary of symbol occurrences
    :type occurrences: dict
    :param filename: The filename where the occurrences must be written.
    :type filename: str
    '''
    assert isinstance(occurrences, dict), 'The parameter occurences must be a dict'
    stream = open(filename, 'wb')
    values = list(occurrences.values()) # numbers
    keys = list(occurrences.keys()) # letters

    l=[]
    for i in keys:
        st = ''.join(format(ord(i), 'b'))
        l.append(st)
        l1=[]    
        for j in l:
            n = int(j,2)
            data=chr(n)
            byte = bytes([n])
            l1.append(byte) #l1 writable array of keys
    l2=[]
    for k in values:
        n = struct.pack('i',k)
        l2.append(n) #l2 writable array of values

    d = dict(zip(l2,l1))
    pickle.dump(occurrences, stream, pickle.HIGHEST_PROTOCOL)
    #return d
        
        

def read_occurrences(filename):
    '''
    Read the symbol occurrences from the given file.

    :param filename: The filename where the occurrences must be read.
    :type filename: str
    :return: A dictionary of the symbol occurrences
    :rtype: dict
    :Examples:

    >>> import tempfile; temp = tempfile.NamedTemporaryFile()
    >>> d = {b'c': 1, b'b': 3, b'a': 4}
    >>> write_occurrences(d, temp.name)
    >>> read_occurrences(temp.name) == d
    True
    >>> d = {b'e': 1, b'f': 1, b'g': 1, b'h': 1, b'a':2}
    >>> write_occurrences(d, temp.name)
    >>> read_occurrences(temp.name) == d
    True
    '''

    with open(filename, 'rb') as f:
        return pickle.load(f)


def huffman_encode(filename, out_filename):
    '''
    Encode a file using Huffman algorithm and writes the result to 
    an other file.
    
    Two files will be created. One called `out_filename` containing
    a Huffman encoding of the input file. Another one called
    `out_filename`+".code" which will contain the occurrences of each 
    symbol.

    :param filename: The filename of the file to be encoded.
    :type filename: str
    :param out_filename: The filename of the file where the resulting\
    encoding will be stored.
    :type out_filename: str
    '''
    stream = open(filename, 'rb')
    
    # Calcul du nombre d'occurrences
    d_occurrences = symbol_occurrences(stream)
    
    # Création du codage de Huffman
    codage = get_coding_from_tree(create_huffman_tree(d_occurrences))
    d_codage=dict(codage)
    
    # Ecriture du fichier stockant le dictionnaire d'occurrences
    with open(out_filename+'.dict', 'w') as d_file:
        for key, value in d_codage.items():
            d_file.write('%s:%s\n' % (key, value))
    
    # Mise de la tête de lecture au début du fichier pour le reparcourir
    stream.seek(0)
    
    # Parcours du fichier et encodage des symboles lus
    str_stream=stream.read()
    list_stream=list(str_stream)
    list_to_append=[]
    for item in list_stream:
        code_item=d_codage.get(item)
        list_to_append.append(code_item)
        
    encoded=''.join(list_to_append)
    bit_encoded=[encoded[i:i + 8] for i in range(0, len(encoded), 8)]
    byte_list = [int(b, 2) for b in bit_encoded]

    with open(out_filename, 'wb') as f:
        f.write(bytearray(byte_list))

def prefix_tree_decoding(bits, tree):
    '''
    Return the decoding of the binary string given in parameter
    using the Huffman tree `tree`.
    
    :param bits: a binary string (only made of 0s and 1s)
    :type bits: str
    :param tree: a Huffman tree
    :type tree: huffman_tree.HuffmanTree
    :return: Return the concatenation of symbols represented by the binary string.\
    The binary string is decoded using the Huffman tree.
    :rtype: bytes
    :UC: The binary string must end in a leaf.
    :Examples:

    >>> tree = create_huffman_tree({b'a': 1, b'b': 2, b'c': 3, b'd': 5})
    >>> prefix_tree_decoding('111110100111111110', tree)
    b'bacdbba'
    '''
    noeud = tree
    sortie = b''
    for bit in bits:
        if noeud.isLeaf():
            sortie += noeud.symbol
            noeud = tree
        if bit == '0':
            noeud = noeud.left
        else:
            noeud = noeud.right
    assert(noeud.isLeaf()), "La chaine devrait se terminer sur une feuille"
    sortie += noeud.symbol
    return sortie

from tp2 import byte_to_binary    
def huffman_decode(filename, out_filename):
    '''
    Decode a file encoded with a Huffman encoding.

    :param filename: the file name of the Huffman encoded file
    :type filename: str
    :param out_filename: the file name where the decoding will be stored
    :type out_filename: str
    '''

    with open(filename,'rb') as f:
        s=f.read()
        list_bytes = list(bytearray(s))
        l=[]
        for el in list_bytes:
            l.append(byte_to_binary(el))
    data = dict()
    
    with open(filename+'.dict','r') as raw_data:
        for item in raw_data:
            if ':' in item:
                key,value = item.split(':', 1)
                data[key]=value
            else:
                pass
    
    s = ''.join(l)
    tree= create_huffman_tree(data)
    out = prefix_tree_decoding(s, tree)
    d = open(out_filename,'w')
    d.write(out[2:])
         
            
