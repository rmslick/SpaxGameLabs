import pygame
import random
from random import randint
import time
import threading

pygame.init()
screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption("Rock Runner")
#icon=pygame.image.load('rock.jpg')
#pygame.display.set_icon(icon)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
runnerX=480
runnerY=585
runnerHeight=15
runnerWidth=40
runnerVel=0.3
rockWidth=25
spawnTime = 0.25
rockHeight=25
rockVel=0.1
screen.fill(black)
gameOver = True
def print_cube(num): 
  global gameOver
  while gameOver:
    time.sleep(5)
    print("Executing")
class Rock():
  def __init__(self):
    self.xPosition = randint(0,800)
    self.yPosition = 0
    pygame.draw.rect(screen,(white),(self.xPosition,self.yPosition,rockWidth,rockHeight))
  def Update(self):
    pygame.draw.rect(screen,(black),(self.xPosition,self.yPosition,rockWidth,rockHeight))
    self.yPosition += 10
    if self.yPosition > 600:
      return True
    else:
      pygame.draw.rect(screen,(white),(self.xPosition,self.yPosition,rockWidth,rockHeight))
def text_to_screen(msg,color,size):
    font=pygame.font.SysFont(None,size)
    text=font.render(msg,True,color)
    screen.blit(text,[200,280])
text_to_screen("Press Space to start",white,100)
#r=Rock()
rockList = []
priorTime = 0
def UpdatePosition():
  global priorTime
  global rockList
  seconds=int(time.time())
  if seconds%1==0 and seconds!=priorTime:
    for rock in rockList:
      rock.Update()



    priorTime=seconds
def SpawnRock(x):
  global priorTime
  global rockList
  global spawnTime
  
  while gameOver:
    print("Spawning")
    r=Rock()
    rockList.append(r)
    time.sleep(spawnTime)



while True:
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        screen.fill(black)
        break
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
spawnThread = threading.Thread(target=SpawnRock, args=(10,)) 
spawnThread.start()
while True:
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if runnerX>=0:
            pygame.draw.rect(screen,(black),(runnerX,runnerY,runnerWidth,runnerHeight))
            runnerX-=runnerVel
    if keys[pygame.K_RIGHT]:
        if runnerX<=960:
            pygame.draw.rect(screen,(black),(runnerX,runnerY,runnerWidth,runnerHeight))
            runnerX+=runnerVel
    pygame.draw.rect(screen,(red),(runnerX,runnerY,runnerWidth,runnerHeight))
    
    UpdatePosition()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameOver = False
            pygame.quit()
            quit()
    pygame.display.update()


spawnThread.join()