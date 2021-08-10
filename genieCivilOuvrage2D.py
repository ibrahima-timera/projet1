"""Module permettant d'implementer des figures geometriques"""

from turtle import *
 

#Fonction pour tracer un rectangle
#Entree: longueur,largeur,couleur
#Sortie: rectangle
#Methode: boucle for
#Connu: les angles droit
def rectangle(longueur,largeur,couleur):
    fillcolor(couleur)
    begin_fill()
    for i in range(2):
        pensize(2)
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)
    end_fill()
#Fonction pour tracer un carre
#Entree: cote,couleur
#Sortie: carre
#Methode: boucle for
#Connu:   angle droit
def carre(cote,couleur):
    fillcolor(couleur)
    begin_fill()
    for i in range(4):
        pensize(2)
        forward(cote)
        left(90)
    end_fill()

#Fonction pour tracer un triangle
#Entree: coteA,coteB,A1(angle du cote coteA),couleur)
#Sortie: triangle
#Methode: affectation
#Connu:
def triangle(coteA,coteB,A1,couleur):
    fillcolor(couleur)
    begin_fill()
    a=position()
    fd(coteA)
    b=position()
    up()
    goto(a)
    down()
    left(A1)
    fd(coteB)
    goto(b)
    end_fill()

#Fonction pour tracer un triangle equilateral
#Entree: cote,couleur
#Sortie: triangle equilateral
#Methode: boucle
#Connu: angle 60 degre
def triangleEqui(cote,couleur):
    fillcolor(couleur)
    begin_fill()
    for i in range(3):
        pensize(2)
        forward(cote)
        left(120)
    end_fill()
    
#Fonction pour tracer un polygone
#Entree: longueur,nombre de cote,couleur
#Sortie: cercle
#Methode: 
#Connu: fonction circle
def polygone(longueur,nbr_cote,couleur):
    fillcolor(couleur)
    begin_fill()
    circle(longueur,steps=nbr_cote)
    end_fill()
    
#Foncrion pour tracer un cercle
#Entree: rayon
#Sortie: cercle
#Methode: fonction circle
#Connu:
def cercle(rayon):
    circle(rayon)
    
#Foncrion pour tracer un demi cercle
#Entree: rayon
#Sortie: demi cercle
#Methode: utilisaton fonction circle
#Connu: 
def demi_cercle(rayon):
    left(90)
    circle(rayon, 180)
    
#Fonction pour tracer un losange
#Entree:cote,couleur
#Sortie: losange
#Methode: 
#Connu: 
def losange(cote,couleur):
    fillcolor(couleur)
    begin_fill()
    left(25)
    forward(cote)
    left(130)
    forward(cote)
    left(50)
    forward(cote)
    left(130)
    forward(cote)
    end_fill()

#Fonction pour tracer un trapeze
#Entree:couleur,angle,liste(base,faceBase,Hauteur)
#Sortie: trapeze
#Methode: utilisation de la liste et du boucle while 
#Connu:
def  trapeze(couleur,angle,cote=list()):
    fillcolor(couleur)
    begin_fill()
    pointDeDepart = position()
    i=0
    while(i<=2):
        fd(cote[i])
        if(i==1):
            lt(angle)
        if(i==0):
            lt(180-angle)
        i+=1
    goto(pointDeDepart[0],pointDeDepart[1])
    end_fill()

#Fonction pour tracer une ellipse
#Entree:rayon
#Sortie: elipse
#Methode: utilisation fonction circle() et seth()
#Connu:
def ellipse(rayon):
    seth(-45)
    for i in range(2):
        circle(rayon,90)
        circle(rayon/3,90)



    
    

    