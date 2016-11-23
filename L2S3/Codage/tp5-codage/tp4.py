def compare(a, b):
    """
    :param a: 
    :type a: any type 
    :param b:
    :type b: same as a
    :return:
       - -1 if a < b
       -  1 if a > b
       -  0 if a = b
    :UC: a and b must be comparable with <
    :Examples:

    >>> compare(0, 1)
    -1
    >>> compare('a', 'a')
    0
    >>> compare((2, 1), (1, 2))
    1
    """
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

### verif if sorted
    ### verif if param is used

def sort(l,p):
    if l==[]:
        return True
    if p == 'prog':
        for item in l:
            if compare(l[item], l[item+1])==-1:    
                return True
            return False
    if p == 'rev':
        for items in l:
            if compare(l[-items], l[-items+1])==1:
                return True
            return False
    return False
    

