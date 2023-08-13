from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorboard import Scorboard
import time


screen = Screen() # Ekran Oluşturuyoruz
screen.bgcolor("black") # Arka planı siyah olarak ayarlıyoruz.
screen.setup(width=800, height=600) # Ekran genişliğini 800px genişlik, 600 px yükseklik olarak ayarlıyoruz.
screen.title("Pong") # Ekran Sayfasının en üzerinde başlık olarak ayarlıyoruz.
screen.tracer(0) # Aniamsyon özeliklerini 0 olarak ayarlıyoruz.

r_paddle = Paddle((350, 0)) # Kendi oluşturduğum paddle sınıfına parametreleri gönderiyoruz.
l_paddle = Paddle((-350, 0))

ball = Ball()
scorboard = Scorboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up") # Yukarı ok'a basınc ane olacağını ayarlıyoruz.
screen.onkey(r_paddle.go_down, "Down") # Aşağı ok'a basınca ne olacağını ayarlıyoruz.

screen.onkey(l_paddle.go_up, "w") # 'w' basınca ne olacağını ayarlıyoruz.
screen.onkey(l_paddle.go_down, "s") # 's'basınca ne olacağını ayarlıyoruz.

game_is_on = True # programımızın durmadan çalışamsını istediğimiz için bu özelliği True oalrak ayarlıyoruz.

while game_is_on:
    time.sleep(ball.move_speed)
    time.sleep(0.001)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -200:
        ball.bounce_y()
    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        #print("Made contact")

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scorboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scorboard.r_point()

        
screen.exitonclick() # Ekranın üzerine basana kadar kapanamsını istemediğimiz için screen kütüphanesinin exitionclick() özeliğini kullanıyoruz.