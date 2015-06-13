import turtle
n=input('Input the number of sides ')
n=int(n)
for x in range(n):
    turtle.forward(100)
    turtle.right(360/n)
    for y in range(n):
        turtle.forward(50)
        turtle.right(360/n)
        for x in range(n):
            turtle.forward(25)
            turtle.right(360/n)