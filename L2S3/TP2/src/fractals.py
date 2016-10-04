from turtle import *
speed("fastest")

def zigzag(n):
    """
    Draws zig-zag of n angles.
    :param n: whole number(nbr of angles)
    :type n: int
    :UC: None
    """
    assert n>=0 and isinstance(n, int),'parameter n is a whole number'
    left(45)
    forward(100)
    for i in range(n):
        right(((-1)**i)*90)
        forward(100)
        

def von_koch(l,n):
    """
    Draws the Von koch's curve of length l and order n.
    :param l: the von koch's curve length
    :type l: int or float (a strictly positive number )
    :param n: the von koch's curve order (a whole number)
    :type n: int
    :UC:None
    """
    assert (isinstance(l, int) or isinstance(l, float)) and l>0, 'parameter l is a positive float or integer'
    assert isinstance(n, int) and n>=0, 'parameter n is a whole number'
    if n==0:
        forward(l)
    else:
        von_koch(l/3,n-1)
        left(60)
        von_koch(l/3,n-1)
        right(120)
        von_koch(l/3,n-1)
        left(60)
        von_koch(l/3,n-1)
   

def von_koch_flocon(l,n):
    """
    Draws a Von Koch's snowflake of length l and order n.
    :param l: the von koch's curve length
    :type l: int or float (a strictly positive number )
    :param n: the von koch's curve order (a whole number)
    :type n: int
    :UC:None    
    """
    assert (isinstance(l, int) or isinstance(l, float)) and l>0, 'parameter l is a positive float or integer'
    assert isinstance(n, int) and n>=0, 'parameter n is a whole number'      
       for i in range(3):
        von_koch(l,n)
        right(120)
        
def cesaro(l,n):
    """
    Draws Cesaro curve of length l and order n.
    :param l: the von koch's curve length
    :type l: int or float (a strictly positive number )
    :param n: the von koch's curve order (a whole number)
    :type n: int
    :UC:None     
    """
    assert (isinstance(l, int) or isinstance(l, float)) and l>0, 'parameter l is a positive float or integer'
    assert isinstance(n, int) and n>=0, 'parameter n is a whole number'        
    if n==0:
        forward(l)
    else:
        cesaro(l/2, n-1)
        left(85)
        cesaro(l/2, n-1)
        right(170)
        cesaro(l/2, n-1)
        left(85)
        cesaro(l/2, n-1)
    
def cesaro_carre(l, n):
    """
    Draws Cesaro square of length l and order n.
    :param l: the von koch's curve length
    :type l: int or float (a strictly positive number )
    :param n: the von koch's curve order (a whole number)
    :type n: int
    :UC:None        
    """
    assert (isinstance(l, int) or isinstance(l, float)) and l>0, 'parameter l is a positive float or integer'
    assert isinstance(n, int) and n>=0, 'parameter n is a whole number'      
    for i in range(4):
        cesaro(l,n)
        left(90)

def sierpinski(l,n):
    """
    Draws the Sierpinski triangle of length l and order n.
    :param l: the von koch's curve length
    :type l: int or float (a strictly positive number )
    :param n: the von koch's curve order (a whole number)
    :type n: int
    :UC:None
    """
    assert (isinstance(l, int) or isinstance(l, float)) and l>0, 'parameter l is a positive float or integer'
    assert isinstance(n, int) and n>=0, 'parameter n is a whole number'      
    if n==0:
        for i in range(0,3):
            fd(l)
            left(120)
    else:
        sierpinski(l/2,n-1)
        fd(l/2)
        sierpinski(l/2,n-1)
        bk(l/2)
        left(60)
        fd(l/2)
        right(60)
        sierpinski(l/2,n-1)
        left(60)
        bk(l/2)
        right(60)  
