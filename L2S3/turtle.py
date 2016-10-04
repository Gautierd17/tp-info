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

import turtle
def draw_sierpinski(length,depth):
    if depth==0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length/2,depth-1)
        t.fd(length/2)
        draw_sierpinski(length/2,depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw_sierpinski(length/2,depth-1)


window = turtle.Screen()
t = turtle.Turtle()
draw_sierpinski(500,1)
window.exitonclick()
