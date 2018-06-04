import pygame, sys
from pygame.locals import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

redButton = 5
yellowButton = 6
blueButton = 13

GPIO.setup(redButton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(yellowButton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(blueButton, GPIO.IN, pull_up_down = GPIO.PUD_UP)

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
#pygame.mouse.set_visible(0)
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
    sys_font = pygame.font.SysFont("Trebuchet MS", 80)
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
        if GPIO.input(redButton) == False:
            print("red")
            circleColor = red
            colorOfText = red
            textInFont = "Red"
        if GPIO.input(yellowButton) == False:
            print("yellow")
            circleColor = yellow
            colorOfText = yellow
            textInFont = "Yellow"
        if GPIO.input(blueButton) == False:
            print("blue")
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
        if event.type == QUIT or keys[pygame.K_ESCAPE] or keys[pygame.K_BACKSPACE]:
            off = True
    pygame.display.update()
    screen.fill(white)

pygame.quit()
sys.exit()
