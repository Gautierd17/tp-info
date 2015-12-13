#SHCHERBAKOVA Iuliia --- SESI 53 --- 2015/16
#TP 5 : Dessiner avec la tortue
#http://www.fil.univ-lille1.fr/~L1S1Info/Doc/HTML/tp_itcond_tortue.html


from turtle import *

def carre(l):
    """ dessine un carre de longueur l """
    for i in range (4):
        forward(l)
        right(90)

def carre_ligne(l,nb):
    """ dessine une ligne de nb carres de longueur l """
    for i in range (nb):
        carre(50)
        penup()
        goto(xcor() + l + 5, ycor())
        pendown()

def carre_grille(l,nb):
    """ dessine une grille de nb * nb carre de longueur l """
    for i in range (nb):
        x = xcor()
        y = ycor()
        carre_ligne(l,nb)
        penup()
        goto(x, y - l - 5)
        pendown()

##carre_grille(50,4)

def carre_emboite():
    """ dessine 50 carres emboites avec un sommet commun
    et dont les longueurs des cotes varient de 10 en 10 """ 
    x = xcor()
    y = ycor()
    l = 10
    for i in range (50):
        carre(l)
        l += 10
        penup()
        goto(x,y)
        pendown()

##carre_emboite()

def carre_tournant(l,n):
    """ dessine n carres de cote l pivotant autour d'une sommet commun
    pour en faire un tour complet """
    a = 360.0 / n
    for i in range (n):
        carre(l)
        right(a)

##carre_tournant(50,20)

def polygone_convexe(l,n):
    """ dessine un polygone rÃ©gulier convexe Ã  n cotes de longueur l """
    a = 360.0 / n
    for i in range (n):
        forward(l)
        right(a)

##polygone_convexe(100,8)

def polygone_etoile(n,l,k):
    """ dessine un polygone rÃ©gulier Ã©toile Ã  n cotes de longueur l,
    le nombre k indiquant l'ordre de parcours des sommets """
    a = 360.0 / n
    for i in range (n):
        penup()
        oldx = xcor()
        oldy = ycor()
        for i in range (k):
            forward(l)
            right(a)
        pendown()
        goto(oldx,oldy)
        penup()
        left(k*a)
        forward(l)
        right(a)

##polygone_etoile(8,100,2)

def carre_centre(l):
    """ dessine un carre bleu centrÃ© Ã  l'origine """
    penup()
    goto(-l/2,l/2)
    pendown()
    pencolor("blue")
    carre(l)

##carre_centre(400)

def tortue_sortie(l):
    """ renvoie True si la tortue est en dehors d'un carre centre Ã  l'origine
    dont les cotes ont pour longueur l passe en parametre sinon False"""
    if(xcor() < -l/2 or xcor() > l/2 or ycor() < -l/2 or ycor() > l/2):
        return True
    else:
        return False

##goto(0,0)
##print(tortue_sortie(400))
##goto(210,0)
##print(tortue_sortie(400))
##goto(0,210)
##print(tortue_sortie(400))
##goto(-210,0)
##print(tortue_sortie(400))
##goto(0,-210)
##print(tortue_sortie(400))

from random import randint

def brownien(l):
    """ simulation du mouvement brownien avec l la longueur de l'environnement """
    carre_centre(l)
    penup()
    pencolor("green")
    goto(0,0)
    pendown()
    while(not tortue_sortie(l)):
        left(randint(0,359))
        forward(randint(10,30))

##brownien(400)

from math import *

def table(w,h):
    """ dessine la table de billard de longueur w et de largeur h """
    penup()
    goto(-w/2,h/2)
    pendown()
    begin_fill() ##debut de la zone Ã  remplir
    pencolor("red")
    fillcolor("green")
    for i in range (4):
        if(i%2 == 0):
            forward(w)
        else:
            forward(h)
        right(90)
    end_fill() ##fin de la zone Ã  remplir

def contact_bord(w,h):
    """ retourne True si la bille touche le bord de la table sinon False """
    if(xcor() <= -w/2 or xcor() >= w/2 or ycor() <= -h/2 or ycor() >= h/2):
        return True
    else:
        return False

def angle_reflexion(w,h,alpha):
    if(xcor() <= -w/2):
        if heading() > 90 and heading() < 270:
            left(180 + 2*(180 - heading()))
        else:
            right(180 - 2*(heading()-180))
    elif(xcor() >= w/2):
        if heading() < 90 or heading() > 270:
            left(180 - 2*heading())
        else:
            right(180 + 2*(360-heading()))
    elif(ycor() <= -h/2):
        if heading() > 90 and heading() < 270:
            left(180 - 2*(heading()-270))
        else:
            right(180 - 2*(270-heading()))
    else:
        if heading() < 90 or heading() > 270:                       
            left(180 + 2*(90-heading()))
        else:
            right(180 + 2*(heading()-90))

def parcours_trajectoire(width,height,x,y,alpha,bandes):
    table(width,height)
    penup()
    goto(x,y)
    pencolor("black")
    left(alpha)
    pendown()
    while(bandes > 0):
        if(contact_bord(width,height)):
            bandes -= 1
            angle_reflexion(width,height,alpha)
            forward(1)
        else:
            forward(1)

##speed(40)       
##parcours_trajectoire(100,50,0,0,10,30)
