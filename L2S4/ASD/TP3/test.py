# -*- coding: utf-8 -*-

import listiterator as list

def print_with_iterator (l):
    """
    Print elements of a list using an iterator.
    
    :param l: The list to be printed
    :type l: dict
    """
    create_iter=list.get_listiterator(l) 
    while list.hasNext(create_iter)==True:
        print(list.next(create_iter))
        

def print_with_iterator_reverse (l):
    """
    Print elements of a list using an iterator in reverse order.
    
    :param l: The list to be printed
    :type l: dict
    """
    lst=l["tail"]
    it=list.get_listiterator(l)
    while list.hasNext(it)==True:
        list.next(it)
    while list.hasPrevious(it):
        print(list.previous(it))
        
        
def print_with_iterator_reverse_bis (l):
    """
    Print elements of a list using an iterator in reverse order.
    
    :param l: The list to be printed
    :type l: dict
    """
    it=list.get_listiterator(l,True)
    while list.hasPrevious(it):
        print(list.previous(it))

def ordering_insert (l, v):
    """
    Add *v* to list *l* such that *l* is kept ordered.
    
    :param l: An ordered list.
    :type l: dict
    :param v: The value to be inserted.
    :type v: same as elements of *l*
    """
    it=list.get_listiterator(l)
    while list.hasNext(it) and it["next"]["value"] < v:
        list.next(it)
    return list.add(it,v)
        
if __name__ == "__main__":
    l = list.empty_list ()
    for i in reversed(range(1,5)):
        list.cons(l,i)

##
##    # test 0 : impression renversee
##    list.print_list(l,reverse=True)
##    # test 1 : impression avec iterateurs
##    print_with_iterator(l)
##    print_with_iterator_reverse(l)
##    print_with_iterator_reverse_bis (l)

##    # test 2 : insertion avant le 3eme element
##    it = list.get_listiterator (l)
##    list.next(it)
##    list.next(it)
##    list.add(it,23)
##    print_with_iterator(l)
##    print_with_iterator_reverse(l)
##
##    # test 3 : insertion apres le dernier element
##    it = list.get_listiterator (l)
##    while (list.hasNext(it)):
##        list.next(it)
##    list.add(it,45)
##    print_with_iterator(l)
##    print_with_iterator_reverse(l)

##    # test 4 : insertion avant le premier element
##    it = list.get_listiterator (l)
##    list.add(it,0)
##    print_with_iterator(l)
##    print_with_iterator_reverse(l)
##
##    # test 5 : insertion avant le dernier element avec l'iterateur placé en fin
##    it = list.get_listiterator (l,True)
##    list.previous(it)
##    list.add(it,445)
##    print_with_iterator(l)
##    print_with_iterator_reverse(l)
##
    # test 6 : affichage à l'envers avec l'itérateur placé en fin
##    print_with_iterator_reverse_bis(l)

    # test 7 : ajout après le dernier élément
##    it = list.get_listiterator (l,True)
##    list.add(it,5)
##    print_with_iterator(l)
##    print_with_iterator_reverse(l)
        
    # test 8 : inserer trié, à vous d'écrire ce test
##    ordering_insert (l, 70)
##    print_with_iterator(l)
    # test 9 : suppression en tete
##    it = list.get_listiterator(l)
##    list.remove(it)
##    print_with_iterator(l)

    # test 10 : suppression en queue
##    it=list.get_listiterator(l,True)
##    list.remove(it)
##    print_with_iterator(l)
