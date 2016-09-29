from turtle import *
speed("fastest")

def zigzag(n):
    right(45)
    for i in range(n):
        left(((-1)**i)*90)
        forward(100)

def vk(l,n):
    if n==0:
        forward(l)
    else:
        vk(l/3,n-1)
        left(60)
        vk(l/3,n-1)
        right(120)
        vk(l/3,n-1)
        left(60)
        vk(l/3,n-1)
   

def vk_fl(l,n):
    for i in range(3):
        vk(l,n)
        right(120)
