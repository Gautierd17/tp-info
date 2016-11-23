f'''
   Compute the entropy on files.

   @author FIL - IEEA - Univ. Lille 1 (oct 2010, août 2015)
'''

import sys
import math
from collections import Counter

# IMPORTS A COMPLETER

def range_bytes():
    return range(256)
def range_printable():
    return (ord(c) for c in string.printable)

def entropy(filename, iterator=range_bytes): 
    '''
    Computes the entropy of the file called `filename`.

    :param filename: Input file name.
    :type filename: str
    :return: A tuple whose first element is an integer: the number of bytes read\
    and the second element is a float: the entropy of the file's content
    :rtype: tuple
    '''

    # 1) Read the file to count occurrences of each byte
    # Dictionary that will store the number of occurrences of each byte.    
    counters = {}
    nb_bytes = 0
    l=[]
    infile = open(filename, 'rb')
    byte = infile.read(1)
    # A COMPLETER
    for line in infile:
        for byte in line:
            l.append(byte)
        
        counters = dict(Counter(l)) # updated counters dict
        # podvinut' nazad
        
        total_sum=0
        occ_lst=list(counters.values())
        for el in occ_lst:
            if el>0:
                total_sum=total_sum+el*math.log(el,2)
        total_sum=-total_sum     
    #return total_sum
        # 2) Calcul de l'entropie à partir des effectifs des octets.
        ### optimal code entropy
    
        total=0
        prob=float(sum(occ_lst)) / max(len(occ_lst), 1)
        prob_lst = [prob]*len(occ_lst)
        for p in prob_lst:
            if p>0:
                total=total+p*math.log(p,2)
        total = -total
        x = (total*100)/total_sum
        eco = 100-x
        return total_sum, total, eco        
##    for x in iterator():
##        p_x=float(string).count(chr(x))/len(string)
##        if p_x>0:
##            entropy+=-p_x*math.log(p_x,2)
           
        
    
       

##def usage():
##    print("Usage: {:s} <filename>".format(sys.argv[0]))
##    print("\t<filename>: filename for which we want to compute the entropy.\n")
##    exit(1)
##
##def main():
##    if len(sys.argv) != 2:
##        usage()
##    (nb_bytes, entro) = entropy(sys.argv[1])
##    print("{:d} bytes read.".format(nb_bytes))
##    print("Entropy = {:f} bits per byte.".format(entro))
##    
##if __name__ == '__main__':
##    main()

