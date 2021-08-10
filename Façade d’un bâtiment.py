from genieCivilOuvrage2D import *



def seDeplacer(x,y):
    up()
    goto(x,y)
    down()

def cadreFenetre(a,b):
    seDeplacer(a,b)
    rectangle(70,370,"DarkGray")

def fenetreDuBas(x,y):

    seDeplacer(x,y)
    rectangle(30,100,"white")
    goto(x+30,y)
    rectangle(30,100,"white")
    seDeplacer(x,y+100)
    rectangle(30,100,"white")
    goto(x+30,y+100)
    rectangle(30,100,"white")

def fenetreDuHaut(x,y):
    seDeplacer(x,y)
    carre(30,"white")
    goto(x+30,y)
    carre(30,"white")

    seDeplacer(x,y+30)
    carre(30,"white")
    goto(x+30,y+30)
    carre(30,"white")

def case(x,y):
    i=0
    a=0
    while(i <= 1):
        seDeplacer(x + a ,y)
        rectangle(10,30,"white")
        
        i= i + 1
        a=10


def principale():
    speed(400)
    setup(1000,700)

    seDeplacer(-400,-300)
    rectangle(800,400,"WhiteSmoke")
    seDeplacer(-400,-300)
    rectangle(800,10,"white")

    #Le premiere fenetres
        
    cadreFenetre(-380,-280)
    fenetreDuBas(-375,-270)
    fenetreDuHaut(-375,10)


    #2ieme fenetres

    cadreFenetre(-290,-280)
    fenetreDuBas(-285,-270)
    fenetreDuHaut(-285,10)
        

    #3ieme fenetres

    cadreFenetre(-200,-280)
    fenetreDuBas(-195,-270)
    fenetreDuHaut(-195,10)


    #4ieme fenetres

    cadreFenetre(120,-280)
    fenetreDuBas(125,-270)
    fenetreDuHaut(125,10)


    #5ieme fenetres

    cadreFenetre(210,-280)
    fenetreDuBas(215,-270)
    fenetreDuHaut(215,10)

    #6 fenetres

    cadreFenetre(300,-280)
    fenetreDuBas(305,-270)
    fenetreDuHaut(305,10)


    #Cadre de la porte
    seDeplacer(-100,-290)
    rectangle(190,390,"white")
    seDeplacer(-85,-290)
    rectangle(160,390,"white")
    seDeplacer(-70,-220)
    rectangle(130,320,"whiteSmoke")


    #escalliers
    seDeplacer(-85,-290)
    rectangle(160,10,"white")
    seDeplacer(-80,-280)
    rectangle(150,10,"white")
    seDeplacer(-75,-270)
    rectangle(140,10,"white")
    seDeplacer(-70,-260)
    rectangle(130,10,"white")
    seDeplacer(-65,-250)
    rectangle(120,10,"white")
    seDeplacer(-60,-240)
    rectangle(110,10,"white")
    seDeplacer(-55,-230)
    rectangle(100,10,"white")

        #Pied de  La porte
    seDeplacer(-100,-220)
    rectangle(190,10,"white")

    seDeplacer(-50,-220)
    rectangle(90,10,"white")

    #Porte
    pensize(3)
    seDeplacer(-50,-210)
    rectangle(45,70,"white")
    seDeplacer(-5,-210)
    rectangle(45,70,"white")

    seDeplacer(-50,-140)
    rectangle(45,70,"white")
    seDeplacer(-5,-140)
    rectangle(45,70,"white")

    #demi cercle
    seDeplacer(40,-70)
    demi_cercle(45)
    left(90)

    #le point noir
    seDeplacer(-5,-10)
    dot(20,"black")

    #la fenetre du haut
    seDeplacer(-35,20)
    rectangle(30,40,"white")
    seDeplacer(-5,20)
    rectangle(30,40,"white")

    #Trapeze du haut du batiment
    seDeplacer(-400,100)
    trapeze("white",150,[800,40,880])
    left(180)
    seDeplacer(-120,95)
    rectangle(230,25,"white")

    #les cases
        #les fenetres
    seDeplacer(-290,120)
    rectangle(125,40,"white")
    case(-270,120)
    case(-240,120)
    case(-210,120)


        #les fenetres
    seDeplacer(-165,120)
    rectangle(320,40,"white")
    case(-125,120)
    case(-75,120)
    case(-40,120)
    case(-10,120)
    case(20,120)
    case(50,120)
    case(115,120)

        #Les fenetres
    seDeplacer(155,120)
    rectangle(125,40,"white")
    case(175,120)
    case(205,120)
    case(235,120)


    #toiture

    seDeplacer(-165,160)
    trapeze("LightGreen",160,[320,50,450])

    #Les cases (les triangles)
    left(180)
    seDeplacer(-290,160)
    triangle(125,42,22,"LightGreen")

    rt(22)
    seDeplacer(155,160)
    triangle(125,54,18,"LightGreen")


    exitonclick()

if __name__ == "__main__":
    principale()
