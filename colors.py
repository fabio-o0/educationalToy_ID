import pygame, sys
from pygame.locals import *

pygame.init()
pygame.font.init()

size = width, height = 480, 320

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
yellow = (255,255,0)
orange = (255,165,0)
green = (0,128,0)
purple =(128,0,128)
gray = (30,30,30)
bluish = (175, 191, 198)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Colors")

circleColor = bluish
circleRadius = 80
keysToCheck = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

def text(text, color):
    sys_font = pygame.font.SysFont ("Trebuchet MS", 80)
    rendered = sys_font.render(text, 0, color)
    textRect = rendered.get_rect(center=(width/2, 65))
    screen.blit(rendered, textRect)
    pygame.display.update()

colorOfText = white
textInFont = ""

off = False

while not off:
    pygame.draw.circle(screen, circleColor, (int(width/2), int(height/2+40)), circleRadius)
    text(textInFont, colorOfText)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            circleColor = red
            colorOfText = red
            textInFont = "Red"
        if keys[pygame.K_w]:
            circleColor = yellow
            colorOfText = yellow
            textInFont = "Yellow"
        if keys[pygame.K_d]:
            circleColor = blue
            colorOfText = blue
            textInFont = "Blue"
        if keys[pygame.K_a] and keys[pygame.K_w]:
            circleColor = orange
            colorOfText = orange
            textInFont = "Orange"
        if keys[pygame.K_d] and keys[pygame.K_w]:
            circleColor = green
            colorOfText = green
            textInFont = "Green"
        if keys[pygame.K_d] and keys[pygame.K_a]:
            circleColor = purple
            colorOfText = purple
            textInFont = "Purple"
        if keys[pygame.K_d] and keys[pygame.K_a] and keys[pygame.K_w]:
            circleColor = gray
            colorOfText = gray
            textInFont = "Black"
        if keys == keysToCheck:
            circleColor = bluish
            colorOfText = white
            textInFont = ""
        if event.type == QUIT:
            off = True
    pygame.display.update()
    screen.fill(white)

pygame.quit()
sys.exit()
