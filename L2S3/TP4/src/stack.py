#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`stack1` module

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2015, september
:last revision: 2016, october

A module for stack data structure.

:Provides:

* `create`
* `push`
* `pop`
* `top`
* `is_empty`

.. seealso::
           :mod:`stack2`

:Examples:

>>> stak = create()
>>> is_empty(stak)
True
>>> push(1, stak)
>>> is_empty(stak)
False
>>> push(2, stak)
>>> top(stak)
2
>>> pop(stak)
2
>>> top(stak)
1
>>> pop(stak)
1
>>> is_empty(stak)
True
"""

class StackEmptyError(Exception):
    """
    Exception for empty stacks
    """
    def __init__(self, msg):
        self.message = msg


def create():
    """
    :return: a new stack
    :rtype: stack
    :UC: none
    """
    return []

def push(x, s):
    """

    :param x: a value
    :type x: any
    :param s: a stack
    :type s: stack
    :return: None
    :rtype: Nonetype
    :Side effect: stack s contains a new value : x
    :UC: none
    """
    s.append(x)

def pop(s):
    """
    :param s: stack to pop
    :type s: stack
    :return: element on top of s
    :Side effect: s contains an element less
    :UC: s must be non empty
    """
    try:
        return s.pop()
    except IndexError:
        raise StackEmptyError('empty stack, nothing to pop')

def top(s):
    """
    :param s: stack to pop
    :type s: stack
    :return: element on top of s without removing it
    :UC: s must be non empty
    """
    try:
        return s[-1]
    except IndexError:
        raise StackEmptyError('empty stack, nothing on the top')

def is_empty(s):
    """
    :param s:
    :type s: stack
    :return:
        * ``True`` if s is empty
        * ``False`` otherwise
    :rtype: bool
    :UC: none
    """
    return s == []

if __name__ == '__main__':
    import doctest
    doctest.testmod()
