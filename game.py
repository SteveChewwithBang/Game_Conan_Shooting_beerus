# Tower Defense Game at 22:11

import pygame
import math
import random
pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

bg = pygame.image.load('bg.png')
char = pygame.image.load('standing.png')

Clock = pygame.time.Clock()
bulletsound = pygame.mixer.Sound('bullet.wav')
hitsound = pygame.mixer.Sound('explosion.wav')

music = pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

score = 0

class player(object):
    def __init__(self, x , y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isjump = False
        self.jumpcount = 10
        self.left = False
        self.right = False
        self.walkcount = 0
        self.standing = True
        self.hitbox = (self.x + 20, self.y, 28, 60)

    def hit(self):
        self.isjump = False
        self.jumpcount = 10
        self.x = 70
        self.y = 345
        self.walkcount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5',1,(255,0,0))
        win.blit(text, (500/2 - (text.get_width()/2), 200))
        pygame.display.update
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()



    def draw(self, win):
        if self.walkcount + 1 >= 27:
            self.walkcount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1
            elif self.right:
                win.blit(walkRight[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y, 28, 60)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)



class enemy(object):
    walkRight = [pygame.image.load('R1_E.png'), pygame.image.load('R2_E.png'), pygame.image.load('R3_E.png'),
                 pygame.image.load('R4_E.png'), pygame.image.load('R5_E.png'), pygame.image.load('R6_E.png'),
                 pygame.image.load('R7_E.png'), pygame.image.load('R8_E.png'), pygame.image.load('R9_E.png'),
                 pygame.image.load('R10_E.png'), pygame.image.load('R11_E.png')]
    walkLeft = [pygame.image.load('L1_E.png'), pygame.image.load('L2_E.png'), pygame.image.load('L3_E.png'),
                pygame.image.load('L4_E.png'), pygame.image.load('L5_E.png'), pygame.image.load('L6_E.png'),
                pygame.image.load('L7_E.png'), pygame.image.load('L8_E.png'), pygame.image.load('L9_E.png'),
                pygame.image.load('L10_E.png'), pygame.image.load('L11_E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkcount + 1 >= 33:
                self.walkcount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkcount//3], (self.x, self.y))
                self.walkcount += 1

            else:
                win.blit(self.walkLeft[self.walkcount//3], (self.x, self.y))
                self.walkcount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)


    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')



def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: '+ str(score), 1, (0,0,0))
    win.blit(text, (350, 10))
    man.draw(win)
    beerus.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()



# Main Loop

font = pygame.font.SysFont('comicsans', 30, True)
man = player (200, 345, 64, 64)
beerus = enemy (100,345, 64, 64, 300)
shoot_loop = 0
bullets = []
run = True
while run:
    Clock.tick(27)

    if beerus.visible == True:
        if man.hitbox[1] < beerus.hitbox[1] + beerus.hitbox[3] and man.hitbox[1] + man.hitbox[3]> beerus.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > beerus.hitbox[0] and man.hitbox[0] < beerus.hitbox[0] + beerus.hitbox[
                2]:
                man.hit()
                score -= 5


    if shoot_loop > 0:
        shoot_loop += 1
    if shoot_loop > 3:
        shoot_loop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < beerus.hitbox[1] + beerus.hitbox[3] and bullet.y + bullet.radius > beerus.hitbox[1]:
            if bullet.x + bullet.radius > beerus.hitbox[0] and bullet.x - bullet.radius < beerus.hitbox[0] + beerus.hitbox[2]:
                hitsound.play()
                beerus.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shoot_loop == 0:
        bulletsound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
        shoot_loop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkcount = 0


    if not(man.isjump):
        if keys[pygame.K_UP]:
            man.isjump = True
            man.right = False
            man.left = False
            man.walkcount = 0
    else:
        if man.jumpcount >= -10:
            neg = 1
            if man.jumpcount < 0:
                neg = -1
            man.y -= (man.jumpcount ** 2) * 0.5 * neg
            man.jumpcount -= 1
        else:
            man.isjump = False
            man.jumpcount = 10

    redrawGameWindow()

pygame.quit()
