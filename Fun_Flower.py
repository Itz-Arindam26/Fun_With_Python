import turtle as t
import colorsys as cl
t.ht()
t.speed(1)
t.setup(800, 800)
t.tracer(10)
t.width(2)
t.bgcolor('black')
for j in range(25):
    for i in range(15):
        t.color(cl.hsv_to_rgb(i/15, j/25, 1))
        t.rt(90)
        t.circle(200-j*4, 90)
        t.lt(90)
        t.circle(200-j*4, 90)
        t.rt(180)
        t.circle(50,24)
t.done()