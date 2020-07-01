import pygame
from pygame.locals import *
import random
pygame.init()
W, H = 415, 480
win = pygame.display.set_mode((W, H))
## Images
pygame.display.set_caption('Classic Race')
maincar = pygame.image.load('car.png')
startscr = pygame.image.load('Startscn_Car-Game.png')
bg = pygame.image.load('splash1.png')
bg2 = pygame.image.load('splash2.png')
blank = pygame.image.load('grey.png')
stage = pygame.image.load('stage.png')
thank = pygame.image.load('thank.png')
game_over = pygame.image.load('game_over.png')
#crash = [pygame.image.load('E'+ str(x)+ '.png') for x in range(1,11)]

bgy2 = 0
bgy1 = -bg2.get_height()
clock = pygame.time.Clock()

## Sound
brakesound = pygame.mixer.Sound('brake.wav')
passingcar = pygame.mixer.Sound('passingcar.wav')
intro = pygame.mixer.Sound('intro.wav')
carsound = pygame.mixer.Sound('carsound.wav')
carstart = pygame.mixer.Sound('carstart.wav')

vel = 2
run = False
class player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.right = False
        self.left = False
        self.hitbox = (x, y, 50, 70)
        self.crash = False
        self.crashcount = 0
        self.life = 3

    def draw(self, win):
        global next
        win.blit(pygame.transform.scale(maincar, (50,80)), (self.x, self.y))
        if self.right:
            win.blit(pygame.transform.scale(maincar,(50, 80)), (self.x, self.y))
            self.hitbox = (self.x,self.y, 50, 80)
        elif self.left:
            win.blit(pygame.transform.scale(maincar,(50,80)), (self.x, self.y))
            self.hitbox = (self.x, self.y, 50, 80)
        if self.crash:
            win.blit(crash[self.crashcount//3],(self.x, self.y))
            self.crashcount += 1
         #   pygame.time.wait(1000)
            if self.crashcount > 10:
                self.crashcount = 0
                self.crash = False
        pygame.draw.rect(win, (0,0,255), (385, 5, 28, 115), 2)
        if self.life == 3:
            win.blit(pygame.transform.scale(maincar, (20,30)), (390, 10))
            win.blit(pygame.transform.scale(maincar,(20,30)), (390, 45))
            win.blit(pygame.transform.scale(maincar, (20,30)), (390, 80))
        elif self.life == 2:
            win.blit(pygame.transform.scale(maincar, (20, 30)), (390, 10))
            win.blit(pygame.transform.scale(maincar, (20, 30)), (390, 45))
        elif self.life == 1:
            win.blit(pygame.transform.scale(maincar, (20, 30)), (390, 10))
        elif self.life == 0:
            pass
        #else:
         #   next = True
          #  startscreen()

    # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class enemy(object):

    img = pygame.image.load('enemy_car1.png')
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.hitbox = (self.x, self.y, 50, 80)
       # self.collide = False
    def draw(self, win):
        if self.visible:
            win.blit(pygame.transform.scale(self.img, (50, 80)),(self.x, self.y))
            self.hitbox = (self.x, self.y, 50, 80)


        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1] and rect[1] < self.hitbox[1] + self.hitbox[3]:
                self.visible = False
                return True
        return False
class enemy1(enemy):
    img = pygame.image.load('enemy_car2.png')
    def draw(self, win):
        if self.visible:
            win.blit(pygame.transform.scale(self.img, (50, 80)), (self.x, self.y))
            self.hitbox = (self.x,self.y, 50, 80)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1]+rect[3]> self.hitbox[1] and rect[1] < self.hitbox[1] + self.hitbox[3]:
                self.visible = False
                return True
        return False
class enemy2(enemy):
    img = pygame.image.load('enemy_car3.png')
    def draw(self, win):
        if self.visible:
            win.blit(pygame.transform.scale(self.img, (50, 80)), (self.x, self.y))
            self.hitbox = (self.x, self.y, 50, 80)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

font = pygame.font.SysFont('consolas', 45, 1, 1)

def completion():
    carsound.stop()
    win.blit(pygame.transform.scale(stage, (415, 480)), (0, 0))

    text = font.render('Stage Completed', 1, (20, 200, 250))
    win.blit(text, (20, 200))
    pygame.display.update()
    pygame.time.delay(5000)

            #next = True
            #startscreen()
            #intro.stop()

def redrawwindow():
    win.blit(bg2, (0, bgy2))
    win.blit(bg2, (0, bgy1))
    font = pygame.font.SysFont('consolas', 20, 1, 1)
    text = font.render('Distance: '+ str(distance) + ' Km', 1,(20, 200, 250))
    win.blit(text, (10, 10))
    car.draw(win)
    for x in objects:
        x.draw(win)
    for x in objects1:
        x.draw(win)
    pygame.display.update()


next = True

def startscreen():

    global run, next, run1
    #win.blit(bg, (0,-470))
    largefont = pygame.font.SysFont('comicsans', 100)
    while next:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            win.blit(pygame.transform.scale(startscr,(415, 480)), (-2,0))
            intro.play()
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                next = False
                intro.stop()

                win.blit(pygame.transform.scale(stage, (415, 480)), (0,0))
                font = pygame.font.SysFont('consolas', 45, 1, 1)
                text = font.render('>>Stage 1', 1, (20, 255, 100))
                win.blit(text, (50, 200))
                pygame.display.update()
                pygame.time.delay(2000)
    for x in ['Get', 'Set', 'Go']:
        carstart.play()
        start = largefont.render(str(x), 1, (0, 255, 0))
        win.blit(bg, (0, -470))
        win.blit(pygame.transform.scale(maincar,(50,80)), (185,300))
        pygame.display.update()
        win.blit(start, (W/2 - start.get_width()/2, 200))
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.display.update()
        next = False
    run = True
    run1 = True

    carstart.stop()
def gameover():

    win.blit(pygame.transform.scale(game_over, (415, 480)), (0,0))
    pygame.display.update()
    pygame.time.delay(3000)
    startscreen()

#startscreen()
def endscreen():

    win.blit(bg, (0,0))
    global next, run

    #largefont = pygame.font.SysFont('comicsans', 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        win.blit(bg, (0, 0))
        #intro.play()
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            startscreen()

            pygame.display.update()
            break

startscreen()
distance = 0
pygame.time.set_timer(USEREVENT+1, random.randrange(2000, 3000))
pygame.time.set_timer(USEREVENT+2, 5000)
objects = []
objects1 = []
car = player(185, 300, 64, 64)

while run:
    run1 = True
    while run1:
        if car.life < 0:
            carsound.stop()
            car.life = 3
            distance = -1
            next = True
            run1 = False
            objects1 = []
            onjects = []
            gameover()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == USEREVENT+2:
                distance += 1

            if event.type == USEREVENT+1:
                blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                r = random.randrange(0,4)
                if r == 0 or r == 1:
                    r1 = random.randrange(0,4)
                    blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                    if r1 == 0:
                        objects.append(enemy(100, -10, 64, 64))
                    elif r1 == 1:
                        objects.append(enemy(280, -10, 64, 64))
                    elif r1 == 2:
                        objects.append(enemy(160, -10, 64, 64))
                    else:
                        objects.append(enemy(208, -10, 64, 64))
                if r == 2:
                    passingcar.play()
                    red1, red2 = False, False
                    r2 = random.randrange(0, 4)
                    if r2 == 0:
                        blue1 = True
                        blue2 = False
                        blue3 = False
                        blue4 = False
                        red1 = False
                        red2 = False
                        objects.append(enemy1(100, -10, 64, 64))
                    elif r2 == 1:
                        blue1, blue3, blue4, red1, red2 = False, False, False, False, False
                        blue2 = True
                        objects.append(enemy1(280, -10, 64, 64))
                    elif r2 == 2:
                        blue3 = True
                        blue1, blue2, blue4, red1, red2 = False, False, False, False, False
                        objects.append(enemy1(160, -10, 64, 64))
                    else:
                        blue4 = True
                        blue1, blue2, blue3, red1, red2 = False, False, False, False, False
                        objects.append(enemy1(208, -10, 64, 64))
                if r == 3:
                    passingcar.play()
                    blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                    r3 = random.randrange(0,2)
                    if r3 == 0:
                        blue1, blue2, blue3, blue4 = False,False,False,False
                        red1 = True
                        red2 = False
                        objects.append(enemy2(100, -10, 64, 64))
                    else:
                        blue1, blue2, blue3, blue4 = False, False, False, False
                        red1 = False
                        red2 = True
                        objects.append(enemy2(280, -10, 64, 64))



        bgy1 += 15
        bgy2 += 15
        keys = pygame.key.get_pressed()
        carsound.play(-1)
  #  for event in pygame.event.get():
        if not(keys[pygame.K_SPACE]):
            if bgy2 > bg2.get_height():
                bgy2 = 0
            if bgy1 > 0:
                bgy1 = -bg2.get_height()
        if keys[pygame.K_SPACE]:
       # brakesound.play()
            bgx1 = 0
            bgx2 = 0
            for x in range(5, -1, -1):

                bgy1 -= x - 2
                bgy2 -= x - 2
                if bgy2 > bg2.get_height():
                    bgy2 = 0
                if bgy1 > 0:
                    bgy1 = -bg2.get_height()
        if keys[pygame.K_LEFT] and car.x > 68:
            car.x -= vel
            car.left = True
            car.right = False
        if keys[pygame.K_RIGHT] and car.x < 300:
            car.x += vel
            car.left = False
            car.right = True

        for objectt in objects:
            objectt.y += 2
            if objectt.y > 500:
                objects.pop(objects.index(objectt))
            if blue1 == True:
                objectt.x += 0.3
                blue2, blue3, blue4, red1, red2 = False, False, False, False, False
            if blue2 == True:
                objectt.x -= 0.3
                blue1, blue3, blue4, red1, red2 = False, False, False, False, False
            if blue3 == True:
                objectt.x -= 0.3
                blue1, blue2, blue4, red1, red2 = False, False, False, False, False
            if blue4 == True:
                objectt.x -= 0.3
                blue1, blue2, blue3, red1, red2 = False, False, False, False, False
            if red1 == True:
                objectt.x += 0.8
                blue1, blue2, blue3, blue4, red2 = False, False, False, False, False
            if red2 == True:
                objectt.x -= 0.8
                blue1, blue2, blue3, blue4, red1 = False, False, False, False, False
            if objectt.collide(car.hitbox):
                objects.pop(objects.index(objectt))


                car.life -= 1
                print(car.life)
                for x in range(100):
                    win.blit(pygame.transform.scale(maincar,(50,80)), (car.x,car.y))
                    pygame.display.flip()
                    win.blit(pygame.transform.scale(blank,(50,80)), (car.x, car.y))
                    pygame.display.flip()


            #if not(car.crash):

             #   car.crash = True
        if distance > 10:
            run1 = False
            run2 = True
            stage2 = True
            distance = -1
            car.life = 3
            completion()

        redrawwindow()


    while stage2:
        # Stage 2 screen
        win.blit(pygame.transform.scale(stage, (415, 480)),(0, 0))
        text = font.render('>>Stage 2', 1, (20, 255, 100))
        win.blit(text, (50, 200))
        pygame.display.update()
        pygame.time.delay(2000)
        objects = []
        objects1 = []
        next = False
        startscreen()
        pygame.time.set_timer(USEREVENT+3, random.randrange(2000,2005))
        pygame.time.set_timer(USEREVENT+4, 5000)
        pygame.time.set_timer(USEREVENT+5, random.randrange(2000,2005))



        car.life = 3
        distance = 0
        stage2 = False
        run2 = True

    while run2:
        if car.life < 0:
            carsound.stop()
            next = True
            gameover()
            car.life = 3
            distance = 0
            objects = []
            objects1 = []
            next = True
            run1 = True
            run2 = False
            run3 = False
            stage3 = False
            #gameover()

            #gameover()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == USEREVENT+4:
                distance += 1

            if event.type == USEREVENT+3:
                blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                r = random.randrange(0,5)
                if r == 0:
                    r1 = random.randrange(0,4)
                    blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                    if r1 == 0:
                        objects.append(enemy(100, -10, 64, 64))
                    elif r1 == 1:
                        objects.append(enemy(280, -10, 64, 64))
                    elif r1 == 2:
                        objects.append(enemy(160, -10, 64, 64))
                    else:
                        objects.append(enemy(208, -10, 64, 64))
                if r == 1 or r == 2 or r == 3:
                    passingcar.play()
                    red1, red2 = False, False
                    r2 = random.randrange(0, 4)
                    if r2 == 0:
                        blue1 = True
                        blue2 = False
                        blue3 = False
                        blue4 = False
                        red1 = False
                        red2 = False
                        objects.append(enemy1(100, -10, 64, 64))
                    elif r2 == 1:
                        blue1, blue3, blue4, red1, red2 = False, False, False, False, False
                        blue2 = True
                        objects.append(enemy1(280, -10, 64, 64))
                    elif r2 == 2:
                        blue3 = True
                        blue1, blue2, blue4, red1, red2 = False, False, False, False, False
                        objects.append(enemy1(160, -10, 64, 64))
                    else:
                        blue4 = True
                        blue1, blue2, blue3, red1, red2 = False, False, False, False, False
                        objects.append(enemy1(208, -10, 64, 64))
                if r == 4:
                    passingcar.play()
                    blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                    r3 = random.randrange(0,2)
                    if r3 == 0:
                        blue1, blue2, blue3, blue4 = False,False,False,False
                        red1 = True
                        red2 = False
                        objects.append(enemy2(100, -10, 64, 64))
                    else:
                        blue1, blue2, blue3, blue4 = False, False, False, False
                        red1 = False
                        red2 = True
                        objects.append(enemy2(280, -10, 64, 64))

                if event.type == USEREVENT + 5:
                    blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                    r = random.randrange(0, 4)
                    if r == 0:
                        r1 = random.randrange(0, 4)
                        blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                        if r1 == 0:
                            objects1.append(enemy(100, -10, 64, 64))
                        elif r1 == 1:
                            objects1.append(enemy(280, -10, 64, 64))
                        elif r1 == 2:
                            objects1.append(enemy(160, -10, 64, 64))
                        else:
                            objects1.append(enemy(208, -10, 64, 64))
                    if r == 1 or r == 2:
                        passingcar.play()
                        red1, red2 = False, False
                        r2 = random.randrange(0, 4)
                        if r2 == 0:
                            blue1 = True
                            blue2 = False
                            blue3 = False
                            blue4 = False
                            red1 = False
                            red2 = False
                            objects1.append(enemy1(100, -10, 64, 64))
                        elif r2 == 1:
                            blue1, blue3, blue4, red1, red2 = False, False, False, False, False
                            blue2 = True
                            objects1.append(enemy1(280, -10, 64, 64))
                        elif r2 == 2:
                            blue3 = True
                            blue1, blue2, blue4, red1, red2 = False, False, False, False, False
                            objects1.append(enemy1(160, -10, 64, 64))
                        else:
                            blue4 = True
                            blue1, blue2, blue3, red1, red2 = False, False, False, False, False
                            objects1.append(enemy1(208, -10, 64, 64))
                    if r == 3:
                        passingcar.play()
                        blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                        r3 = random.randrange(0, 2)
                        if r3 == 0:
                            blue1, blue2, blue3, blue4 = False, False, False, False
                            red1 = True
                            red2 = False
                            objects1.append(enemy2(100, -10, 64, 64))
                        else:
                            blue1, blue2, blue3, blue4 = False, False, False, False
                            red1 = False
                            red2 = True
                            objects1.append(enemy2(280, -10, 64, 64))


        bgy1 += 20
        bgy2 += 20
        keys = pygame.key.get_pressed()
        carsound.play(-1)
  #  for event in pygame.event.get():
        if not(keys[pygame.K_SPACE]):
            if bgy2 > bg2.get_height():
                bgy2 = 0
            if bgy1 > 0:
                bgy1 = -bg2.get_height()
        if keys[pygame.K_SPACE]:
       # brakesound.play()
            bgx1 = 0
            bgx2 = 0
            for x in range(5, -1, -1):

                bgy1 -= x - 2
                bgy2 -= x - 2
                if bgy2 > bg2.get_height():
                    bgy2 = 0
                if bgy1 > 0:
                    bgy1 = -bg2.get_height()
        if keys[pygame.K_LEFT] and car.x > 68:
            car.x -= vel
            car.left = True
            car.right = False
        if keys[pygame.K_RIGHT] and car.x < 300:
            car.x += vel
            car.left = False
            car.right = True

        for objectt in objects:
            objectt.y += 2
            if objectt.y > 500:
                objects.pop(objects.index(objectt))
            if blue1 == True:
                objectt.x += 0.3

            if blue2 == True:
                objectt.x -= 0.3
            if blue3 == True:
                objectt.x -= 0.3
            if blue4 == True:
                objectt.x -= 0.3
            if red1 == True:
                objectt.x += 0.8
            if red2 == True:
                objectt.x -= 0.8
            if objectt.collide(car.hitbox):
                objects.pop(objects.index(objectt))


                car.life -= 1
                print(car.life)
                for x in range(100):
                    win.blit(pygame.transform.scale(maincar,(50,80)), (car.x,car.y))
                    pygame.display.flip()
                    win.blit(pygame.transform.scale(blank,(50,80)), (car.x, car.y))
                    pygame.display.flip()

               # print('hi ' + str(objectt))


        for objectt in objects1:
            objectt.y += 2
            if objectt.y > 500:
                objects1.pop(objects1.index(objectt))
            if blue1 == True:
                objectt.x += 0.3

            if blue2 == True:
                objectt.x -= 0.3
            if blue3 == True:
                objectt.x -= 0.3
            if blue4 == True:
                objectt.x -= 0.3
            if red1 == True:
                objectt.x += 0.8
            if red2 == True:
                objectt.x -= 0.8
            if objectt.collide(car.hitbox):
                objects1.pop(objects1.index(objectt))


                car.life -= 1
                print(car.life)
                for x in range(100):
                    win.blit(pygame.transform.scale(maincar,(50,80)), (car.x,car.y))
                    pygame.display.flip()
                    win.blit(pygame.transform.scale(blank,(50,80)), (car.x, car.y))
                    pygame.display.flip()

               # print('hi ' + str(objectt))


        if distance > 10:
            run2 = False
            run3 = True
            stage3 = True
            completion()
        redrawwindow()


    while stage3:

        win.blit(pygame.transform.scale(stage, (415, 480)), (0, 0))
        text = font.render('>>Stage 3', 1, (20, 255, 100))
        win.blit(text, (50, 200))
        pygame.display.update()
        pygame.time.delay(2000)
        objects = []
        objects1 = []
        startscreen()
        pygame.time.set_timer(USEREVENT+6, random.randrange(2000, 2500))
        pygame.time.set_timer(USEREVENT+7, 5000)
        pygame.time.set_timer(USEREVENT+1, random.randrange(1500,2005))


        car.life = 3
        distance = 0
        stage3 = False
        run3 = True

    while run3:
        if car.life < 0:
            carsound.stop()
            car.life = 3
            distance = 0
            next = True
            run1 = True
            run2 = False
            run3 = False
            run = False
            gameover()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == USEREVENT+7:
                distance += 1

            if event.type == USEREVENT+6:
                blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                r = random.randrange(0,6)
                if r == 0:
                    r1 = random.randrange(0,4)
                    blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                    if r1 == 0:
                        objects.append(enemy(100, -10, 64, 64))
                    elif r1 == 1:
                        objects.append(enemy(280, -10, 64, 64))
                    elif r1 == 2:
                        objects.append(enemy(160, -10, 64, 64))
                    else:
                        objects.append(enemy(208, -10, 64, 64))
                if r == 1:
                    passingcar.play()
                    red1, red2 = False, False
                    r2 = random.randrange(0, 4)
                    if r2 == 0:
                        blue1 = True
                        blue2 = False
                        blue3 = False
                        blue4 = False
                        red1 = False
                        red2 = False
                        objects.append(enemy1(100, -10, 64, 64))
                    elif r2 == 1:
                        blue1, blue3, blue4, red1, red2 = False, False, False, False, False
                        blue2 = True
                        objects.append(enemy1(280, -10, 64, 64))
                    elif r2 == 2:
                        blue3 = True
                        blue1, blue2, blue4, red1, red2 = False, False, False, False, False
                        objects.append(enemy1(160, -10, 64, 64))
                    else:
                        blue4 = True
                        blue1, blue2, blue3, red1, red2 = False, False, False, False, False
                        objects.append(enemy1(208, -10, 64, 64))
                if r == 2 or r == 3 or r == 4 or r == 5:
                    passingcar.play()
                    blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                    r3 = random.randrange(0,2)
                    if r3 == 0:
                        blue1, blue2, blue3, blue4 = False,False,False,False
                        red1 = True
                        red2 = False
                        objects.append(enemy2(100, -10, 64, 64))
                    else:
                        blue1, blue2, blue3, blue4 = False, False, False, False
                        red1 = False
                        red2 = True
                        objects.append(enemy2(280, -10, 64, 64))

                if event.type == USEREVENT+1:
                    blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                    r = random.randrange(0, 4)
                    if r == 0:
                        r1 = random.randrange(0, 4)
                        blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                        if r1 == 0:
                            objects1.append(enemy(100, -10, 64, 64))
                        elif r1 == 1:
                            objects1.append(enemy(280, -10, 64, 64))
                        elif r1 == 2:
                            objects1.append(enemy(160, -10, 64, 64))
                        else:
                            objects1.append(enemy(208, -10, 64, 64))
                    if r == 1:
                        passingcar.play()
                        red1, red2 = False, False
                        r2 = random.randrange(0, 4)
                        if r2 == 0:
                            blue1 = True
                            blue2 = False
                            blue3 = False
                            blue4 = False
                            red1 = False
                            red2 = False
                            objects1.append(enemy1(100, -10, 64, 64))
                        elif r2 == 1:
                            blue1, blue3, blue4, red1, red2 = False, False, False, False, False
                            blue2 = True
                            objects1.append(enemy1(280, -10, 64, 64))
                        elif r2 == 2:
                            blue3 = True
                            blue1, blue2, blue4, red1, red2 = False, False, False, False, False
                            objects1.append(enemy1(160, -10, 64, 64))
                        else:
                            blue4 = True
                            blue1, blue2, blue3, red1, red2 = False, False, False, False, False
                            objects1.append(enemy1(208, -10, 64, 64))
                    if r == 2 or r == 3 or r == 4 or r == 5:
                        passingcar.play()
                        blue1, blue2, blue3, blue4, red1, red2 = False, False, False, False, False, False
                        r3 = random.randrange(0, 2)
                        if r3 == 0:
                            blue1, blue2, blue3, blue4 = False, False, False, False
                            red1 = True
                            red2 = False
                            objects1.append(enemy2(100, -10, 64, 64))
                        else:
                            blue1, blue2, blue3, blue4 = False, False, False, False
                            red1 = False
                            red2 = True
                            objects1.append(enemy2(280, -10, 64, 64))


        bgy1 += 20
        bgy2 += 20
        keys = pygame.key.get_pressed()
        carsound.play(-1)
  #  for event in pygame.event.get():
        if not(keys[pygame.K_SPACE]):
            if bgy2 > bg2.get_height():
                bgy2 = 0
            if bgy1 > 0:
                bgy1 = -bg2.get_height()
        if keys[pygame.K_SPACE]:
       # brakesound.play()
            bgx1 = 0
            bgx2 = 0
            for x in range(5, -1, -1):

                bgy1 -= x - 2
                bgy2 -= x - 2
                if bgy2 > bg2.get_height():
                    bgy2 = 0
                if bgy1 > 0:
                    bgy1 = -bg2.get_height()
        if keys[pygame.K_LEFT] and car.x > 68:
            car.x -= vel
            car.left = True
            car.right = False
        if keys[pygame.K_RIGHT] and car.x < 300:
            car.x += vel
            car.left = False
            car.right = True

        for objectt in objects:
            objectt.y += 2
            if objectt.y > 500:
                objects.pop(objects.index(objectt))
            if blue1 == True:
                objectt.x += 0.3

            if blue2 == True:
                objectt.x -= 0.3
            if blue3 == True:
                objectt.x -= 0.3
            if blue4 == True:
                objectt.x -= 0.3
            if red1 == True:
                objectt.x += 0.8
            if red2 == True:
                objectt.x -= 0.8
            if objectt.collide(car.hitbox):
                objects.pop(objects.index(objectt))


                car.life -= 1
                print(car.life)
                for x in range(100):
                    win.blit(pygame.transform.scale(maincar,(50,80)), (car.x,car.y))
                    pygame.display.flip()
                    win.blit(pygame.transform.scale(blank,(50,80)), (car.x, car.y))
                    pygame.display.flip()

               # print('hi ' + str(objectt))


        for objectt in objects1:
            objectt.y += 2
            if objectt.y > 500:
                objects1.pop(objects1.index(objectt))
            if blue1 == True:
                objectt.x += 0.3

            if blue2 == True:
                objectt.x -= 0.3
            if blue3 == True:
                objectt.x -= 0.3
            if blue4 == True:
                objectt.x -= 0.3
            if red1 == True:
                objectt.x += 0.8
            if red2 == True:
                objectt.x -= 0.8
            if objectt.collide(car.hitbox):
                objects1.pop(objects1.index(objectt))


                car.life -= 1
                print(car.life)
                for x in range(100):
                    win.blit(pygame.transform.scale(maincar,(50,80)), (car.x,car.y))
                    pygame.display.flip()
                    win.blit(pygame.transform.scale(blank,(50,80)), (car.x, car.y))
                    pygame.display.flip()

                #print('hi ' + str(objectt))


        if distance > 10:
            run2 = False
            run3 = False
            run = False
            next = True
            objects1 = []
            objects = []
            distance = -1
            car.life = 3
            completion()
            win.blit(pygame.transform.scale(thank,(415, 480)), (0,0))
            pygame.display.update()
            pygame.time.delay(3000)
            startscreen()

        redrawwindow()