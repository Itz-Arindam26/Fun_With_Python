import turtle as tur
a = tur.Turtle()
a.hideturtle()
a.speed(1)
def curve(): 
    for i in range(200): 
        a.right(1) 
        a.forward(1) 

a.fillcolor('red')
a.begin_fill()
a.lt(120)
a.forward(210)
curve()
a.rt(200)
curve()
a.forward(210)
a.end_fill()
def txt():
    a.penup() 
    a.setpos(-75, 145) 
    a.pendown() 
    a.color('lightgreen') 
    a.write("Please Star me", font=( 
      "Verdana", 14, "bold")) 
    
txt()
tur.done()