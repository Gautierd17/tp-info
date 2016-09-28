=================
Fibonacci numbers
=================

What are Fibonacci numbers?
===========================

Fibonacci numbers are a sequence of numbers defined by the two first terms :

.. math::

   f_0 &= 0\\
   f_1 &= 1\\

and for all :math:`n\geq 0` by the following recursion relation :

.. math::

   f_{n+1} &= f_{n+1} + f_{n}.

Here are the Fibonacci numbers for :math:`0\leq n \leq 10` :

.. table:: Table of the first Fibonacci numbers
 

   ===========  ============
   :math:`n`     :math:`f_n`  
   ===========  ============
   0            0
   1            1             
   2            1           
   3            2
   4            3
   5            5
   6            8
   7            13
   8            21
   9            34
   10           55
   ===========  ============


A recursive function
====================   

A recursive function
====================   
A function:

.. literalinclude:: ../src/fibonacci.py
   :language: python
   :pyobject: fibonacci
   :linenos:

It takes more time to find the value of f(40) than value of f(10) or less.
I've used the module time of python to find exact values of time spent on calculations.
Example f(10)...f(0):
>>> import time

>>> start = time.time()
>>> fibonacci(10)
>>> end = time.time()
>>> print(end - start)

>>> 0.0 #seconds

Example f(40):
>>> import time

>>> start = time.time()
>>> fibonacci(40)
>>> end = time.time()
>>> print(end - start)

>>> 83.16859483718872 #seconds

Quel rapport existe-t-il entre le nombre de lignes imprimées et le nombre d’appels à la fonction ?

`(nbre_lignes-1)/2 = nbre_appels`

Nombre d’appels pour n compris entre 0 et 10:

   ===========  ============
   `n`          `nbre_appels` 
   ===========  ============
   0            0
   1            1
   2            3
   3            5
   4            9
   5            15
   6            25
   7            41
   8            67
   9            109
   10           177
   40           662320563
   ===========  ============

It takes more than 10 mins to execute a command `python3 fibonacci.py 40 | wc -l`.
For details : https://github.com/tonythedealer/TP-info/tree/master/L2S3/TP2
