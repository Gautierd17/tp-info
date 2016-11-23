'''
Binary tree implementation that can be used as a Huffman tree.

@author FIL - IEEA - Univ. Lille (août 2015)
'''

class HuffmanTree:
    '''
    Manages Huffman trees
    '''
    
    left = None
    right = None
    occurrences = 0
    symbol = None

    def __init__(self, symbol=None, occurrences=None, left=None, right=None):
        """
        Creates a Huffman tree consisting of either:
        - one leaf (in that case `symbol` and `occurrences` must be provided)
        - a node with two subtrees.

        :param symbol: The symbol to store in the leaf
        :type symbol: str
        :param occurrences: The number of occurrences of the given symbol
        :type occurrences: int
        :param left: The left subtree
        :type left: huffman_tree.HuffmanTree
        :param right: The right subtree
        :type right: huffman_tree.HuffmanTree
        :UC: Either symbol and occurrences are given, or left and right.
        The number of occurrences must be positive.
        
        Example:
        >>> HuffmanTree('a', 1)
        |a:1|
        >>> HuffmanTree(left = HuffmanTree('a', 1), right = HuffmanTree('b', 1))
        |ab:2|_<|a:1|, |b:1|>
        """
        if symbol is None:
            assert (occurrences is None), "The symbol is missing"
            assert (left is not None and right is not None), "Both subtrees must be provided"
            self.left = left
            self.right = right
            self.occurrences = left.occurrences + right.occurrences
            self.symbol = left.symbol + right.symbol
        else:
            assert (occurrences is not None), "The symbol's number of occurrences must be given"
            assert (left is None and right is None), "The subtrees must not be given with the symbol"
            self.symbol = symbol
            self.occurrences = occurrences

    def children(self, left, right):
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None

    def __repr__(self):
        repr = '|'
        if self.symbol is not None:
            repr += self.symbol
        if self.occurrences is not None:
            repr += ':%d' % self.occurrences
        repr += '|'
        if not self.isLeaf():
            repr += '_<%s, %s>' % (self.left, self.right)
        return repr

    def __lt__(self, other):
        return self.occurrences < other.occurrences

    def __eq__(self, other):
        return self.occurrences == other.occurrences
    
