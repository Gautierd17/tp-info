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
        if talkative:
            print('{:s}<-{:d}'.format(dots,1))
        return 1
    else:
        res =  n * fact(n - 1, talkative=talkative, __depth=__depth + 1)
        if talkative:
            print('{:s}<-{:d}'.format(dots,res))
        return res

def is_palindromic(s, talkative=False, __depth=0):
    n = len(s)
    if talkative:
        dots = "..." * __depth
        print('{:s}->fact({:d})'.format(dots,n))
    if n <= 0:
        if talkative:
            print('{:s}<-{:d}'.format(dots,n))
        return True
    else:
        res = s[0] == s[-1] and is_palindromic(s[1:n-1])
        if talkative:
            print('{:s}<-{:d}'.format(dots,res))
        return res 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
