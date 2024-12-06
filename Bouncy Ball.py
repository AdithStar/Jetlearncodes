import pgzrun
from random import randint
TITLE = "FLAPPY BALL"
WIDTH = 800
HEIGHT = 600
def random_color():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  return r,g,b
Gravity = 2000
class Ball:
  def __init__(self,init_x,init_y):
    self.x = init_x
    self.y = init_y 
    self.vx = 200
    self.vy = 0
    self.radius = 40
    self.color = random_color()
  def draw(self):
    pos = (self.x,self.y)
    screen.draw.filled_circle(pos,self.radius,self.color)

ball = Ball(50,100)
balls = [Ball(randint(50,WIDTH - 50),randint(50,HEIGHT - 50))for i in range(5)]
def draw():
  screen.clear()
  for ball in balls:
    ball.draw()

def update(dt):
  for ball in balls:
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
    for ball in balls:
      ball.vy = -500

pgzrun.go() 