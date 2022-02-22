# 1 . 배경 만들기
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up_paddle, "Up")
screen.onkey(r_paddle.down_paddle, "Down")
screen.onkey(l_paddle.up_paddle, "w")
screen.onkey(l_paddle.down_paddle, "s")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()
    #벽 만나면 튕기기
    if ball.ycor() > 280 or ball.ycor() <-280 :
        ball.bounce()




screen.exitonclick()







# 2 . 움직이는 패달 만들기
# 3 . 움직이는 공 만들기
# 4 . 공 부딪히는 부분 만들기
# 5 . 패달에 부딪혀서 튕기는 부분 만들기
# 6 . 패달을 지나쳤을 때 점수
# 7 . 점수



