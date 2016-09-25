# TP 2 : Algorithmes et programmation

### 2. Algorithmes récursifs


[![Download Python](https://pp.vk.me/c836333/v836333766/10af/Uxs7hx8-fOU.jpg)](https://www.python.org/downloads/release/python-344/)
[![Documentation Python](https://pp.vk.me/c836333/v836333766/10b6/r1KTGitaPQA.jpg)](https://docs.python.org/3.4/)
[![Cours Fibonacci Algorithm](https://pp.vk.me/c626922/v626922766/2cf9a/1W8tLeh3E0o.jpg)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-19-dynamic-programming-i-fibonacci-shortest-paths/)
[![Sphinx](https://pp.vk.me/c836333/v836333766/10c4/1N2SYXB6bXg.jpg)](https://pypi.python.org/pypi/Sphinx)
[![Unix Commands](https://pp.vk.me/c836333/v836333766/10cb/mE9nIDqKWIo.jpg)](https://en.wikipedia.org/wiki/List_of_Unix_commands)

### 2.2. Tracer une fonction récursive

###### Talkative function example.
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
    ............<-1       # error : fact(0) != 0. Zero replaced by 1.
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
        print('{:s}->fact({:d})'.format(dots,1)) # n replaced by 1.
    if n == 0:
        res = 1
    else:
        res =  n * fact(n - 1, talkative=talkative, __depth=__depth + 1)

    if talkative:
        print('{:s}<-{:d}'.format(dots, res))
        
    return res
```
