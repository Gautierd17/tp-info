import os
import array

class Node(object):
    recursion = False
    def __init__(self, letter=None, probability=None, left_node=None, right_node=None, root=None): # __init__ method is roughly what represents a constructor in Python
        self.left_node = left_node
        self.right_node = rignt_node
        self.root = root
        self.letter = letter
        self.probability = probability
        
    def __pr__(self): 
        if Node.recursion:
            left_node = self.left_node if self.left_node else '#'  
            right_node = self.right_node if self.right_node else '#'        
            return ''.join( ('(%s:%d)'%(self.letter, self.probability), str(left_node), str(right_node)))
        else:
            return '(%s:%d)'%(self.letter, self.probability)
    
    def __d__(self, other):
        if not isinstance(other, Node):
            return super(Node, self).__d__(other) # delegating calls of methods to his parent of the specified type
        return d(self.probability, other.probability)

def Pop(nodes):
    if len(nodes)>1:
        first=nodes.pop(0)
        second=nodes.pop(0)
        return first, second
    else:
        return nodes[0], None
        
def tree_create(nodes):    
    nodes.sort()
    while(True):
        first, second = Pop(nodes)
        if not second:
            return first
        root = Node(left_node=first, right_node=second, probability=first.probability+second.probability)
        first.root = root
        second.root = root
        nodes.insert(0, root)
        nodes.sort()

def optimal_coding(node, dict_codes, buffer_stack=[]):
    if not node.left_node and not node.right_node:
        dict_codes[node.letter] = ''.join(buffer_stack)
        return
    buffer_stack.append('0')
    optimal_coding(node.left_node, dict_codes, buffer_stack)
    buffer_stack.pop()
    
    buffer_stack.append('1')
    optimal_coding(node.right_node, dict_codes, buffer_stack)
    buffer_stack.pop()

def prob(string):
    from collections import defaultdict
    dictionnaire = defaultdict(int)
    for i in string:
        dictionnaire[i] += 1
    return dictionnaire

MAX_BITS = 8
import cPickle

class Encoder(object):
    def __init__(self, filename=None):
        if filename:
            if os.path.exists(filename):
                self.encode(filename)
            else:
                      % filename
                self.long_str = filename
    def __get_long_str(self):
        return self._long_str
    def __set_long_str(self, s):
        self._long_str = s
        if s:
            self.root = self._get_tree_root()
            self.code_map = self._get_code_map()
            self.array_codes, self.code_length = self._encode()
    long_str = property(__get_long_str, __set_long_str)
    
    def _get_tree_root(self):
        d = prob(self.long_str)
        return tree_create(
            [Node(letter=letter, probability=int(probability)) for letter, probability in d.iteritems()]
            )

    def _get_code_map(self):
        a_dict={}
        optimal_coding(self.root, a_dict)
        return a_dict
        
    def _encode(self):
        array_codes = array.array('B')
        code_length = 0
        buff, length = 0, 0
        for ch in self.long_str:
            code = self.code_map[ch]        
            for bit in list(code):
                if bit=='1':
                    buff = (buff << 1) | 0x01
                else: # bit == '0'
                    buff = (buff << 1)
                length += 1
                if length == MAX_BITS:
                    array_codes.extend([buff])
                    buff, length = 0, 0

            code_length += len(code)
            
        if length != 0:
            array_codes.extend([buff << (MAX_BITS-length)])
            
        return array_codes, code_length

    def encode(self, filename):
        fp = open(filename, 'rb')
        self.long_str = fp.read()
        fp.close()

    def write(self, filename):
        if self._long_str:
            fcompressed = open(filename, 'wb')
            marshal.dump(
                (cPickle.dumps(self.root), self.code_length, self.array_codes),
                fcompressed)
            fcompressed.close()
        else:
            raise ValueError 
import marshal
class Decoder(object):
    def __init__(self, filename=None):
        if filename_or_raw_str:
            if os.path.exists(filename):
                filename = filename
                self.read(filename)            
            else:
                raw_string = filename
                unpickled_root, length, array_codes = marshal.loads(raw_string)
                self.root = cPickle.loads(unpickled_root)
                self.code_length = length        
                self.array_codes = array.array('B', array_codes)

    def _decode(self):
        string_buf = []
        total_length = 0    
        node = self.root
        for code in self.array_codes:
            buf_length = 0
            while (buf_length < MAX_BITS and total_length != self.code_length):
                buf_length += 1
                total_length += 1            
                if code >> (MAX_BITS - buf_length) & 1:
                    node = node.right_node
                    if node.letter:
                        string_buf.append(node.letter)
                        node = self.root
                else:
                    node = node.left_node
                    if node.letter:
                        string_buf.append(node.letter)
                        node = self.root

        return ''.join(string_buf)        

    def read(self, filename):
        f = open(filename, 'rb')
        unpickled_root, length, array_codes = marshal.load(f)        
        self.root = cPickle.loads(unpickled_root)
        self.code_length = length        
        self.array_codes = array.array('B', array_codes)
        f.close()

    def decode_as(self, filename):
        decoded = self._decode()
        file = open(filename, 'wb')
        file.write(decoded)
        file.close()

##if __name__=='__main__':
##    original_file = 'he.txt'
##    compressed_file = 'compressed.txt'
##    decompressed_file = 'filename2.txt'
##
##    # first way to use Encoder/Decoder
##    enc = Encoder(original_file)    
##    enc.write(compressed_file)
##    dec = Decoder(compressed_file)
##    dec.decode_as(decompressed_file)

    # second way
    #enc = Encoder()
    #enc.encode(original_file)
    #enc.write(compressed_file)
    #dec = Decoder()
    #dec.read(compressed_file)
    #dec.decode_as(decompressed_file)


