# TP 2 : Algorithmes et programmation

### 2. Algorithmes récursifs


[![Download Python](https://pp.vk.me/c836333/v836333766/10af/Uxs7hx8-fOU.jpg)](https://www.python.org/downloads/release/python-344/)
[![Documentation Python](https://pp.vk.me/c836333/v836333766/10b6/r1KTGitaPQA.jpg)](https://docs.python.org/3.4/)
[![Cours Fibonacci Algorithm](https://pp.vk.me/c626922/v626922766/2cf9a/1W8tLeh3E0o.jpg)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-19-dynamic-programming-i-fibonacci-shortest-paths/)
[![Sphinx](https://pp.vk.me/c836333/v836333766/10c4/1N2SYXB6bXg.jpg)](https://pypi.python.org/pypi/Sphinx)
[![Unix Commands](https://pp.vk.me/c836333/v836333766/10cb/mE9nIDqKWIo.jpg)](https://en.wikipedia.org/wiki/List_of_Unix_commands)

### 2.2. Tracer une fonction récursive

####  What is recursion? 

> Recursion in computer science is a method where the solution to a problem depends on solutions to smaller instances of the same  problem (as opposed to iteration). The approach can be applied to many types of problems, and recursion is one of the central ideas of computer science.

![alt text](http://i.stack.imgur.com/HAEZW.gif "Recursion")

#### Talkative and recursive function example : fact 

*By default, talkative (optional) parameter is set to False and the function fact calculates the factorial of the number passed as parameter and returns the value. But when this parameter is assigned to True, the function then traces the different recursive calls by printing them on the standard output. (The optional parameter __depth only useful if the talkative parameter is True, this parameter manages the indentation of recursive calls.)*


```python
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
        print('{:s}->fact({:d})'.format(dots,n)) .
    if n == 0:
        res = 1
    else:
        res =  n * fact(n - 1, talkative=talkative, __depth=__depth + 1)

    if talkative:
        print('{:s}<-{:d}'.format(dots, res))
        
    return res
```

####  Talkative and recursive function example : binomial 

> In mathematics, a **binomial coefficient** is any of the positive integers that occur as coefficients in the binomial theorem.

**Binomial formula:**
![alt text][https://wikimedia.org/api/rest_v1/media/math/render/svg/7a75ee6c0491af552e7af42d90f1d3b4245d7484 "Binomial"]

**Recursive formula:**
![alt text][https://wikimedia.org/api/rest_v1/media/math/render/svg/c1736571dc6d640fd320aff4806cd92769862f2d "Recursive"]

```python
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
```

Also, this function can be created using python module `math`.
```python
>>> from math import factorial as fact
```
```python
def binomial2(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom
``` 

####  Talkative and recursive function example : is_palindromic

> A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.

```python
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
```

####  Talkative and recursive function example : somme

> Sum of two real numbers.
```python
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
```

### 2.3. Nombres de Fibonacci

> n mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence, and characterized by the fact that every number in it is the sum of the two preceding ones:
> *0 1 1 2 3 5 8 13 21 34 55*

Formula: 
![alt text][https://wikimedia.org/api/rest_v1/media/math/render/svg/f00c4321176b6522fe148a11a80a8e5fca9e88da "Fibonacci"]
![alt text][http://images-mediawiki-sites.thefullwiki.org/02/1/3/9/99174101582843431.png "Fibonacci"]
![alt text][http://40.media.tumblr.com/0a1c0913f2ac24ce8838e85ced735e37/tumblr_mno79kgNkV1sszkooo1_1280.png "Fibonacci"]

#### Talkative Fibonacci Function

```python
def fibonacci(n, talkative=False, __depth=0):
    """
    Returns the value of n-element in fibonacci sequence.
    This is recursive function which takes n as parameter and return
    the value of this n-element in sequence.
    :parameter n: int, natural number and 0
    :parameter talkative:(optional boolean) defaults set to False. If True, 
                          prints, recursive calls during computation
    :return: int >= 0
    :UC: n >= 0

    :Examples:
    >>> fibonacci(4)
    3
    >>> fibonacci(4, talkative=True)
    ->fibonacci(4)
    ...->fibonacci(3)
    ......->fibonacci(2)
    .........->fibonacci(1)
    .........<-1
    .........->fibonacci(0)
    .........<-0
    ......<-1
    ......->fibonacci(1)
    ......<-1
    ...<-2
    ...->fibonacci(2)
    ......->fibonacci(1)
    ......<-1
    ......->fibonacci(0)
    ......<-0
    ...<-1
    <-3
    3
    """
    if talkative:
        dots = '...' * __depth
        print('{:s}->fibonacci({:d})'.format(dots,n)) 
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
        
    else:
        res = fibonacci(n-1, talkative=talkative,__depth=__depth + 1)+fibonacci(n-2, talkative=talkative,__depth=__depth + 1)
  
    if talkative:
        print('{:s}<-{:n}'.format(dots, res))
    return res
```

As illustrated at document `sourcedoc\fibonacci.rst`, the calculations of this function takes alot of time(for numbers bigger than 10) because of huge number of calls to the function `fibonacci`.
Here's a table from this document:

| n - parameter   | number of calls to the function | 
| :-------------: |:-------------:| 
| 1        | 1 | 
| 2       | 3      |  
| 3 | 5      |  
| 4 |9|
| 5 |15|
| 6 |25|
| 7 |41|
| 8 |67|
| 9 |109|
| 10 |177|
| 40 |331160281|


