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
![alt text][logo]
[logo]: https://wikimedia.org/api/rest_v1/media/math/render/svg/7a75ee6c0491af552e7af42d90f1d3b4245d7484 "Binomial"

**Recursive formula:**
![alt text][logo]
[logo]: https://wikimedia.org/api/rest_v1/media/math/render/svg/c1736571dc6d640fd320aff4806cd92769862f2d "Recursive"

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
>>> from math import factorial as fact
