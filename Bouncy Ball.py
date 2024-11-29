import pgzrun
from random import randint
TITLE = "FLAPPY BALL"
WIDTH = 800
HEIGHT = 600
r = randint(0,255)
g = randint(0,255)
b = randint(0,255)
color = r,g,b
Gravity = 2000
class Ball:
  def __init__(self,init_x,init_y):
    self.x = init_x
    self.y = init_y 
    self.vx = 200
    self.vy = 0
    self.radius = 40

  def draw(self):
    pos = (self.x,self.y)
    screen.draw.filled_circle(pos,self.radius,color)

ball = Ball(50,100)
def draw():
  screen.clear()
  ball.draw()

def update(dt):
  uy = ball.vy
  ball.vy += Gravity * dt
  ball.y += (uy+ball.vy)*0.5 * dt
  if ball.y > HEIGHT - ball.radius:
    ball.y = HEIGHT - ball.radius
    ball.vy = -ball.vy * 0.9
  ball.x += ball.vx * dt
  if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
    ball.vx = -ball.vx

def on_key_down(key):
  if key == keys.SPACE:
    ball.vy = -500

    

pgzrun.go() 
