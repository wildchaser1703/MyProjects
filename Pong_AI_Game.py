import turtle
import winsound
win = turtle.Screen()
win.title("The Pong Game")
win.bgcolor("Black")
win.setup(width= 800, height=600)
win.tracer(0)
#Score
score_a = 0
score_b = 0
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(+350, 0)

#Ball 1
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("red")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 0.3
ball1.dy = 0.3

#Ball 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("yellow")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -0.3
ball2.dy = -0.5

#Ball 3
ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("circle")
ball3.color("white")
ball3.penup()
ball3.goto(0, 0)
ball3.dx = -0.5
ball3.dy = -0.5

# Pen to write down scores
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="Center", font=("courier", 24, "normal"))
balls = [ball1, ball2, ball3]

#Function for the movement of the paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard Inputs
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")
#Main Loop of the Game
while True:
    win.update()
    for ball in balls:
        #Ball Movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        #Border collision
        if ball.ycor()>290:
            ball.sety(290)
            ball.dy *=-1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #Check that paddle doesn't goes out of the screen   
        if paddle_a.ycor()>290:
            paddle_a.sety(290)
        if paddle_b.ycor()>290:
            paddle_b.sety(290)
        if ball.ycor()<-290:
            ball.sety(-290)
            ball.dy *=-1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #Check that paddle doesn't goes out of the screen 
        if paddle_a.ycor()<-290:
            paddle_a.sety(-290)
        if paddle_b.ycor()<-290:
            paddle_b.sety(-290)
        if ball.xcor()>390:
            ball.goto(0, 0)
            ball.dx *=-1
            score_a += 10
            pen.clear()
            pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="Center", font=("Arial", 24, "normal"))
            
        if ball.xcor()<-390:
            ball.goto(0, 0)
            ball.dx *=-1
            score_b += 10
            pen.clear()
            pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="Center", font=("Arial", 24, "normal"))
            
        #Paddle and Ball collision
        
        if (ball.xcor() > 340 and ball.xcor() < 360) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        if (ball.xcor() < -340 and ball.xcor() > -360) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    #AI Player
    closest_ball= balls[0]
    for ball in balls:
        if ball.xcor() < closest_ball.xcor():
            closest_ball= ball
        
    if paddle_a.ycor() < closest_ball.ycor() and abs(paddle_a.ycor() - closest_ball.ycor()) > 10:
        paddle_a_up()
    elif paddle_a.ycor() > closest_ball.ycor() and abs(paddle_a.ycor() - closest_ball.ycor()) > 10:
        paddle_a_down()