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

if __name__ == "__main__":
   import doctest, sys
   doctest.testmod()

   #n = int(sys.argv[1]) #sys.argv[1] contains the first command line argument passed to the script.
   #print(fibonacci(n, talkative=True))
        
