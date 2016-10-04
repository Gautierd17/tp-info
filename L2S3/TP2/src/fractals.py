from turtle import *
speed("fastest")

def zigzag(n):
    right(45)
    for i in range(n):
        left(((-1)**i)*90)
        forward(100)

def von_koch(l,n):
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
    for i in range(3):
        von_koch(l,n)
        right(120)
        
def cesaro(l,n):
    if n==0:
        forward(l)
    else:
        cesaro(l/4, n-1)
        left(85)
        cesaro(l/4, n-1)
        right(170)
        cesaro(l/4, n-1)
        left(85)
        cesaro(l/4, n-1)
    
def cesaro_carre(l, n):
    
    for i in range(4):
        cesaro(l,n)
        left(90)

def sierpinski(l,n):
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
