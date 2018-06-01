import pygame, sys
from pygame.locals import *
from gpiozero import Button

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

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mouse.set_visible(0)
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

yellowButton = Button(5)
redButton = Button(6)
greenButton = Button(13)

off = False

while not off:
    pygame.draw.circle(screen, circleColor, (int(width/2), int(height/2+40)), circleRadius)
    text(textInFont, colorOfText)
    for event in pygame.event.get():
        if event.type == QUIT:
            off = True
    if redButton.is_pressed:
        circleColor = red
        colorOfText = red
        textInFont = "Red"
    if yellowButton.is_pressed:
        circleColor = yellow
        colorOfText = yellow
        textInFont = "Yellow"
    if greenButton.is_pressed:
        circleColor = blue
        colorOfText = blue
        textInFont = "Blue"
    if redButton.is_pressed: and yellowButton.is_pressed:
        circleColor = orange
        colorOfText = orange
        textInFont = "Orange"
    if yellowButton.is_pressed: and greenButton.is_pressed:
        circleColor = green
        colorOfText = green
        textInFont = "Green"
    if redButton.is_pressed: and greenButton.is_pressed:
        circleColor = purple
        colorOfText = purple
        textInFont = "Purple"
    if redButton.is_pressed: and yellowButton.is_pressed: and greenButton.is_pressed:
        circleColor = gray
        colorOfText = gray
        textInFont = "Black"
    else:
        circleColor = bluish
        colorOfText = white
        textInFont = ""
    pygame.display.update()
    screen.fill(white)

pygame.quit()
sys.exit()
