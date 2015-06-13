import turtle
length=2
angle=0

while length != 0:
    length=int(input('Enter the length of the line'))
    if length==0:
        break
    angle=int(input('Enter the angle of shifting into right'))
    colour_list=['red','black','blue','green']
    colour='0'
    while colour.lower() not in colour_list:
        colour=input('Enter the colour of the line from this red,black,blue,green')
    turtle.color(colour)
    turtle.forward(length)
    turtle.right(angle)
    
    
 
#answer=0
#user_input=False
#while answer!='56':
#    answer=input('Enter your pin')
#    if answer!='56':
#        print('Wrong pin type again')
#    else :
#        print('Access granted') 