import pgzrun
from random import randint
from time import time

TITLE="Connceting Satellites"
WIDTH=800
HEIGHT=350

satellites=[]
lines=[]

next_satellite=0

start_time=0
end_time=0
total_time=0

number_of_satellites=10

def create_satellites():
  global start_time
  for count in range(0,number_of_satellites):
     satellite=Actor("ship")
     satellite.pos=randint(40, WIDTH-40), randint(40, HEIGHT-40)
     satellites.append(satellite)
  start_time=time()

def draw():
  global total_time
  screen.blit("space", (0,0))
  number=1
  for satillite in satellites:
    screen.draw.text(str(number) , (satillite.pos[0], satillite.pos[1]+20))
    satillite.draw()
    number=number +1

  for line in lines:
    screen.draw.line(line[0],line[1] , (255,255,255))


  if next_satellite < number_of_satellites:
    total_time = time() - start_time
    screen.draw.text(str(round(total_time,1)) , (10,10) , fontsize=30 )
  else:
    screen.draw.text(str(round(total_time,1)) , (10,10) , fontsize=30 )

def update():
  pass

def on_mouse_down(pos):
  global next_satellite, lines
  if next_satellite < number_of_satellites:
   if satellites[next_satellite].collidepoint(pos):
    if next_satellite:
      lines.append((satellites[next_satellite - 1].pos , 
      satellites[next_satellite].pos))
    next_satellite = next_satellite +1
  else:
    lines=[]
    next_satellite=0


create_satellites()
pgzrun.go()