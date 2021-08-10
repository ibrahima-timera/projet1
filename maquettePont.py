import turtle
import genieCivilOuvrage2D

def arc(rayon, angle, debut):
    turtle.up()
    turtle.setposition(debut, rayon)
    turtle.setheading(0)
    turtle.down()
    turtle.circle(-rayon, angle)
    turtle.up()
    turtle.setposition(debut, rayon)
    turtle.setheading(0)
    turtle.down()
    turtle.circle(-rayon, -angle)
    turtle.setheading(0)


def tracer(distance):
    turtle.forward(distance)

def tracerPuisRetour(angle , distance):
    turtle.left(angle)
    turtle.forward(distance)
    turtle.up()
    turtle.back(distance)
    turtle.down()
    turtle.setheading(0)

def grandTriangle(cote1, cote2):
   #tracer le petit triangle gauche
    pointDeDepart = turtle.position()
    turtle.forward(cote1)
    turtle.left(90)
    turtle.forward(cote2)
    turtle.goto(pointDeDepart[0], pointDeDepart[1])
    turtle.up()
    turtle.setheading(0)
    turtle.goto(pointDeDepart[0] + cote1, pointDeDepart[1] + cote2)
    turtle.right(90)
    turtle.down()
   #tracer le petit triangle droite
    pointDeDepart = turtle.position()
    turtle.forward(cote2)
    turtle.left(90)
    turtle.forward(cote1)
    turtle.goto(pointDeDepart[0], pointDeDepart[1])
    turtle.up()
    turtle.goto(pointDeDepart[0] + cote1, pointDeDepart[1] - cote2)
    turtle.right(90)
    turtle.down()
    turtle.setheading(0)

def seDeplacerSansTracer(x, y=0):
    centreDuRepere = turtle.position()
    turtle.up()
    turtle.goto(centreDuRepere[0] + x, centreDuRepere[1] + y)
    turtle.down()

def piedPont(x, y):
    genieCivilOuvrage2D.rectangle(x, y,"blue")

if __name__ == "__main__":
    turtle.speed(10)
    turtle.color("blue")
    turtle.width(4)

    i = 1
    while(i <= 3):
        turtle.pensize(3)
        rayon, angle = 177, 68
        debut = turtle.position()
        if(i == 1):
            arc(rayon, angle, debut[0] + 166 - 406)
        else:
            arc(rayon,angle, debut[0] + 166)
        distance = 20
        tracer(distance)
        angle, distance = 120, 22
        tracerPuisRetour(angle, distance)
        angle, distance = 90, 35
        tracerPuisRetour(angle, distance)

        cote1, cote2 = 47.83, 84
        grandTriangle(cote1,cote2)
        angle, distance = 90, 102
        tracerPuisRetour(angle, distance)
        cote2 = 110
        grandTriangle(cote1,cote2)
        tracerPuisRetour(angle, distance)
        cote2 = 84
        grandTriangle(cote1, cote2)

        angle, distance = 90, 36
        tracerPuisRetour(angle, distance)
        angle, distance = 30, 19
        tracerPuisRetour(angle, distance)
        distance = 20
        tracer(distance)
        if(i <= 2):
            x, y = -20, -13
            seDeplacerSansTracer(x,y)
            x, y = 40,10
            piedPont(x,y)
            x, y = -35, -20
            seDeplacerSansTracer(x,y)
            x, y = 110, 20
            piedPont(x,y)
            x, y = 52, 33
            seDeplacerSansTracer(x,y)

        i = i + 1

    turtle.exitonclick()



