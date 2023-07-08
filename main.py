import turtle
import time
import math
from random import randint

font= ('Arial', 16, 'normal')

My_screen = turtle.Screen()
My_screen.bgcolor("light blue")
My_screen.title("Aim screen")

turtle_instance = turtle.Turtle()

turtle_instance2 = turtle.Turtle()
turtle_instance2.penup()
turtle_instance2.hideturtle()

turtle_instance4 = turtle.Turtle()
turtle_instance4.penup()
turtle_instance4.hideturtle()

score=0

turtle_instance3 = turtle.Turtle()
turtle_instance3.penup()
turtle_instance3.hideturtle()
turtle_instance3.goto(-430,330)
turtle_instance3.write(f"Score: {score}", align="center", font={"Arial", 32, "normal"})

My_screen.addshape("ezgif.com-resize.gif")

turtle_instance.shape("ezgif.com-resize.gif")

speed = 1

num = math.floor(My_screen.numinput("Timer", "Enter the seconds", minval=0, maxval=59))
stop = False

turtle_instance.penup()
turtle_instance.setposition(randint(-300,300),randint(-300,300))


def update_score():
    global score
    score = score + 1
    turtle_instance3.clear()
    turtle_instance3.write(f"Score: {score}", align="center", font={"Arial", 32, "normal"})

game_over = False
def clicked(x,y):

    if game_over:
        return

    target_x, target_y = turtle_instance.position()
    if abs(target_x - x) < 20 and abs(target_y - y) < 20:
        if num > 0:
            update_score()
        else:
            turtle_instance.hideturtle()

    turtle_instance.hideturtle()
    x2 = randint(-300, 300)
    y2 = randint(-300, 300)
    turtle_instance.penup()
    turtle_instance.goto(x2, y2)
    turtle_instance.showturtle()

My_screen.listen()
My_screen.onclick(clicked)

while True:
    turtle_instance2.sety(300)
    turtle_instance2.setx(-30)
    turtle_instance2.write(str(num), font=("Arial", 50))
    turtle_instance4.sety(370)
    turtle_instance4.setx(-50)
    turtle_instance4.write("Time Left", font=("Arial", 15))
    num -= 1
    time.sleep(1)
    turtle_instance2.clear()


    if num <= 0:
        game_over = True

        turtle_instance4.clear()
        turtle_instance2.clear()
        turtle_instance2.sety(320)
        turtle_instance2.setx(-90)
        turtle_instance2.write("Time Over", font=("Arial", 30))
        time.sleep(59)
        turtle_instance2.clear()
        break
    print(num)
    My_screen.update()

turtle.mainloop()