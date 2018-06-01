import pygame, sys
from pygame.locals import *
import inflect

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

keysToCheck = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

p = inflect.engine()

count = 0
colorOfText = yellow

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Numbers")

icon = pygame.image.load('icon.png')

def num_text(text, color):
    sys_font = pygame.font.SysFont("Trebuchet MS", 80)
    rendered = sys_font.render(text, 0, color)
    textRect = rendered.get_rect(center=(width/2, (height/2)-55))
    screen.blit(rendered, textRect)

def word_text(text, color, size):
    sys_font = pygame.font.SysFont("Trebuchet MS", size)
    rendered = sys_font.render(text, 0, color)
    textRect = rendered.get_rect(center=(width/2, (height/2)+35))
    screen.blit(rendered, textRect)

off = False

while not off:
    screen.blit(icon, (width-140,20))
    textInFont = str(count)
    numToWords = p.number_to_words(count)
    if count <= 20:
        sizeOfWords = 80
    elif count <= 100:
        sizeOfWords = 60
    elif count <= 110:
        sizeOfWords = 40
    else:
        sizeOfWords = 30
    num_text(textInFont, colorOfText)
    word_text(numToWords, colorOfText, sizeOfWords)
    pygame.display.update()
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            count += 1
            colorOfText = blue
        if keys[pygame.K_LEFT]:
            if count > 1:
                count -= 1
                colorOfText = red
            elif count == 1:
                count -= 1
                colorOfText = yellow
        if keys[pygame.K_UP]:
            count = 0
            colorOfText = yellow
        if event.type == QUIT:
            off = True
    pygame.display.update()
    screen.fill(white)

pygame.quit()
sys.exit()
