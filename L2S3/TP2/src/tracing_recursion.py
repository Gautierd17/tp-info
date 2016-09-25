#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`recursion_tracing`

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2016, september

Examples of recursion tracings.
"""


def fact(n, talkative=False, __depth=0):
    """
    Computes the factorial of natural number n. 
    Tracks recursive calls if optional parameter is set to True.

    :param n: natural number
    :param talkative: (optional boolean) defaults set to False. If True, 
                      prints, recursive calls during computation
    :return: factorial of n
    :UC: n >= 0

    :Examples:
    >>> fact(4)
    24
    >>> fact(4, talkative=True)
    ->fact(4)
    ...->fact(3)
    ......->fact(2)
    .........->fact(1)
    ............->fact(0)
    ............<-1
    .........<-1
    ......<-2
    ...<-6
    <-24
    24
    """
    assert isinstance(n, int) and n >= 0,\
        'parameter n must be a non negative integer'
    if talkative:
        dots = '...' * __depth
        print('{:s}->fact({:d})'.format(dots,n))
    if n == 0:
        res = 1
    else:
        res =  n * fact(n - 1, talkative=talkative, __depth=__depth + 1)

    if talkative:
        print('{:s}<-{:d}'.format(dots, res))
        
    return res

# function : sum
def somme(a, b, talkative=False, __depth=0):
    """
    Returns the sum of two numbers.
    This is recursive algorithm which takes two numbers a and b
    as parameter and returns their sum.

    :param a: real number
    :param b: real number
    :param talkative: (optional boolean) defaults set to False. If True, 
                      prints, recursive calls during computation
    :return: sum of a and b, a+b
    :UC: b>=0

    :Examples:
    >>> somme(-1,5)
    4
    >>> somme(-1,5, talkative=True)
    ->fact(-1,5)
    ...->fact(0,4)
    ......->fact(1,3)
    .........->fact(2,2)
    ............->fact(3,1)
    ...............->fact(4,0)
    ...............<-4
    ............<-4
    .........<-4
    ......<-4
    ...<-4
    <-4
    4
    """
    if talkative:
        dots = '...' * __depth
        print('{:s}->fact({:d},{:g})'.format(dots,a,b))
    if b == 0:
        res = a
    else:
        res = somme(a+1,b-1,talkative=talkative,__depth=__depth + 1)

    if talkative:
        print('{:s}<-{:d}'.format(dots, res))
        
    return res



# function : binomial
def binomial(n,p,talkative=False, __depth=0):
    """
    Calculates binomial coefficient xCy = x! / (y! (x-y)!).
    This is recursive algorithm which takes two numbers n and p
    as parameter and returns binomial coefficient.

    :parameter n: natural number or 0
    :parameter p: natural number or 0
    :parameter talkative:(optional boolean) defaults set to False. If True, 
                          prints, recursive calls during computation
    :return: binomial coefficient of two given natural(or 0) numbers
    :UC: 0<=p<=n

    :Examples:
    >>> binomial(6,4)
    15
    >>> binomial(6,4, talkative=True)
    ->binomial(6,4)
    ...->binomial(5,3)
    ......->binomial(4,2)
    .........->binomial(3,1)
    ............->binomial(2,0)
    ............<-1
    ............->binomial(2,1)
    ...............->binomial(1,0)
    ...............<-1
    ...............->binomial(1,1)
    ...............<-1
    ............<-2
    .........<-3
    .........->binomial(3,2)
    ............->binomial(2,1)
    ...............->binomial(1,0)
    ...............<-1
    ...............->binomial(1,1)
    ...............<-1
    ............<-2
    ............->binomial(2,2)
    ............<-1
    .........<-3
    ......<-6
    ......->binomial(4,3)
    .........->binomial(3,2)
    ............->binomial(2,1)
    ...............->binomial(1,0)
    ...............<-1
    ...............->binomial(1,1)
    ...............<-1
    ............<-2
    ............->binomial(2,2)
    ............<-1
    .........<-3
    .........->binomial(3,3)
    .........<-1
    ......<-4
    ...<-10
    ...->binomial(5,4)
    ......->binomial(4,3)
    .........->binomial(3,2)
    ............->binomial(2,1)
    ...............->binomial(1,0)
    ...............<-1
    ...............->binomial(1,1)
    ...............<-1
    ............<-2
    ............->binomial(2,2)
    ............<-1
    .........<-3
    .........->binomial(3,3)
    .........<-1
    ......<-4
    ......->binomial(4,4)
    ......<-1
    ...<-5
    <-15
    15
    """
    assert 0<=p<=n
    if talkative:
        dots = '...' * __depth
        print('{:s}->binomial({:d},{:g})'.format(dots,n,p))
    if p==n or p==0:
        res = 1
    else:
        res = binomial(n-1,p-1, talkative=talkative,__depth=__depth + 1)+binomial(n-1,p, talkative=talkative,__depth=__depth + 1)
        
    if talkative:
        print('{:s}<-{:d}'.format(dots, res))
    return res



# binomial v.2 using factorials
from math import factorial as fac

def binomial2(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom



# function : is_palindromic
def is_palindromic(s, talkative=False, __depth=0):
    """
    Returns True if the word(s) is a palindrome or False in the opposite case.
    This is recursive predicate which tests if the string used as
    parameter is the palindrome.
    :parameter s: a string
    :parameter talkative:(optional boolean) defaults set to False. If True, 
                          prints, recursive calls during computation
    :return: True or False
    :UC: none

    :Examples:
    >>> is_palindromic('radar')
    True
    >>> is_palindromic('radar', talkative=True)
    ->is_palindromic(radar)
    ...->is_palindromic(ada)
    ......->is_palindromic(d)
    ...<-1
    <-1
    True  
    """
    n = len(s)
    if talkative:
        dots = '...' * __depth
        print('{:s}->is_palindromic({:s})'.format(dots,s)) 
        
    if n <= 1:
        return True
    else:
        s[0]==s[-1]
        res = is_palindromic(s[1:n-1],talkative=talkative,__depth=__depth + 1) 
        
    if talkative:
        print('{:s}<-{:d}'.format(dots, res))
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    


