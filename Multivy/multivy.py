import pygame, sys
from pygame.locals import *
from random import randint
import time

#definitions
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

left = (width/2-160, height/2)
middle = (width/2-25, height/2)
right = (width/2+140, height/2)

#init
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Math")
icon = pygame.image.load('icon.png')

#classes
class Text:
    def displayText(self, displayableValue, color, location, size):
        self.displayableValue = displayableValue
        self.color = color
        self.location = location
        sys_font = pygame.font.SysFont("Trebuchet MS", size)
        rendered = sys_font.render(self.displayableValue, 0, self.color)
        textRect = rendered.get_rect(center = self.location)
        screen.blit(rendered, textRect)

class Number(Text):
    def __init__(self, value):
        self.value = value
        self.color = color
        self.displayableValue = str(self.value)

class Result(Number):
    def __init__(self, id, num1, num2):
        super(Number, self).__init__()
        self.color = color
        self.id = id
        if self.id == 0:
            self.value = num1 * num2
        else:
            try:
                self.value = num1 / num2
            except ZeroDivisionError:
                self.value = num2 / num1
        self.displayableValue = str(self.value)

#functions
def drawScreen():
    screen.fill(white)
    if id == 0:
        num1.displayText(num1.displayableValue, blue, left, 100)
        num2.displayText(num2.displayableValue, blue, middle, 100)
    else:
        try:
            num1.displayText(num1.displayableValue, blue, left, 100)
            num2.displayText(num2.displayableValue, blue, middle, 100)
        except ZeroDivisionError:
            num1.displayText(num2.displayableValue, blue, middle, 100)
            num2.displayText(num1.displayableValue, blue, left, 100)
    plusOrMinusObject.displayText(plusOrMinusValue, blue, (width/2-95, height/2), 100)
    equals.displayText("=", blue, (width/2+45, height/2), 100)
    res.displayText(res.displayableValue, blue, right, 100)
    if len("Total: " + str(totalScoreValue) + "/" + str(totalTriesValue)) >= 0 and len("Total: " + str(totalScoreValue) + "/" + str(totalTriesValue)) < 10:
        totalScoreText.displayText("Total: " + str(totalScoreValue) + "/" + str(totalTriesValue), blue, (100,height - 40), 40)
    elif len("Total: " + str(totalScoreValue) + "/" + str(totalTriesValue)) >= 10 and len("Total: " + str(totalScoreValue) + "/" + str(totalTriesValue)) < 11:
        totalScoreText.displayText("Total: " + str(totalScoreValue) + "/" + str(totalTriesValue), blue, (110,height - 40), 40)
    elif len("Total: " + str(totalScoreValue) + "/" + str(totalTriesValue)) >= 11 and len("Total: " + str(totalScoreValue) + "/" + str(totalTriesValue)) < 12:
        totalScoreText.displayText("Total: " + str(totalScoreValue) + "/" + str(totalTriesValue), blue, (120,height - 40), 40)
    else:
        totalScoreText.displayText("Total: " + str(totalScoreValue) + "/" + str(totalTriesValue), blue, (130,height - 40), 40)
    screen.blit(icon, (width-110,5))
    pygame.display.update()

#main()
id = randint(0,1)
num1 = Number(randint(0,9))
num2 = Number(randint(0,9))
res = Result(id, num1.value, num2.value)
plusOrMinusObject = Text()
plusOrMinusValue = ""
equals = Text()
scoreText = Text()
circleRadius = 0
score = 0
tries = 0
totalScoreText = Text()
totalScoreValue = 0
totalTriesValue = 0

off = False
while not off:
    drawScreen()
    if tries < 9:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                off = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                plusOrMinusValue = "/"
                plusOrMinusObject.displayText(plusOrMinusValue, blue, (width/2-95, height/2), 100)
                tries += 1
                totalTriesValue += 1
                pygame.display.update()
                time.sleep(1)
                if id == 1:
                    score += 1
                    totalScoreValue += 1
                    screen.fill(white)
                    pygame.display.update()
                    while circleRadius < 100:
                        pygame.draw.circle(screen, yellow, (int(width/2), int(height/2)), circleRadius)
                        scoreText.displayText(str(score) + "/" + str(tries), blue, (int(width/2), int(height/2)), circleRadius)
                        pygame.display.update()
                        circleRadius += 1
                    time.sleep(2)
                    id = randint(0,1)
                    num1 = Number(randint(0,9))
                    num2 = Number(randint(0,9))
                    res = Result(id, num1.value, num2.value)
                    plusOrMinusObject = Text()
                    plusOrMinusValue = ""
                    equals = Text()
                    scoreText = Text()
                    circleRadius = 0
                    drawScreen()
                    pygame.display.update()
                else:
                    screen.fill(white)
                    pygame.display.update()
                    while circleRadius < 100:
                        pygame.draw.circle(screen, yellow, (int(width/2), int(height/2)), circleRadius)
                        scoreText.displayText(str(score) + "/" + str(tries), blue, (int(width/2), int(height/2)), circleRadius)
                        pygame.display.update()
                        circleRadius += 1
                    time.sleep(2)
                    id = randint(0,1)
                    num1 = Number(randint(0,9))
                    num2 = Number(randint(0,9))
                    res = Result(id, num1.value, num2.value)
                    plusOrMinusObject = Text()
                    plusOrMinusValue = ""
                    equals = Text()
                    scoreText = Text()
                    circleRadius = 0
                    drawScreen()
                    pygame.display.update()
            if keys[pygame.K_RIGHT]:
                plusOrMinusValue = "*"
                plusOrMinusObject.displayText(plusOrMinusValue, blue, (width/2-95, height/2), 100)
                tries += 1
                totalTriesValue += 1
                pygame.display.update()
                time.sleep(1)
                if id == 0:
                    score += 1
                    totalScoreValue += 1
                    screen.fill(white)
                    pygame.display.update()
                    while circleRadius < 100:
                        pygame.draw.circle(screen, yellow, (int(width/2), int(height/2)), circleRadius)
                        scoreText.displayText(str(score) + "/" + str(tries), blue, (int(width/2), int(height/2)), circleRadius)
                        pygame.display.update()
                        circleRadius += 1
                    time.sleep(2)
                    id = randint(0,1)
                    num1 = Number(randint(0,9))
                    num2 = Number(randint(0,9))
                    res = Result(id, num1.value, num2.value)
                    plusOrMinusObject = Text()
                    plusOrMinusValue = ""
                    equals = Text()
                    scoreText = Text()
                    circleRadius = 0
                    drawScreen()
                    pygame.display.update()
                else:
                    screen.fill(white)
                    pygame.display.update()
                    while circleRadius < 100:
                        pygame.draw.circle(screen, yellow, (int(width/2), int(height/2)), circleRadius)
                        scoreText.displayText(str(score) + "/" + str(tries), blue, (int(width/2), int(height/2)), circleRadius)
                        pygame.display.update()
                        circleRadius += 1
                    time.sleep(2)
                    id = randint(0,1)
                    num1 = Number(randint(0,9))
                    num2 = Number(randint(0,9))
                    res = Result(id, num1.value, num2.value)
                    plusOrMinusObject = Text()
                    plusOrMinusValue = ""
                    equals = Text()
                    scoreText = Text()
                    circleRadius = 0
                    drawScreen()
                    pygame.display.update()
            if keys[pygame.K_UP]:
                score = 0
                tries = 0
                totalScoreValue = 0
                totalTriesValue = 0
    else:
        tries = 0
        score = 0

pygame.quit()
sys.exit()
