import pygame
from pygame.constants import K_SPACE
pygame.init()

#Creating a window

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Square Game")

#Creating basic rectangle character

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.whenJump = False
        self.countJump = 10
        self.hitbox = (self.x, self.y, 50, 50)
    
    def draw(self,win):
        self.hitbox = (self.x, self.y, 50, 50)
        pygame.draw.rect(win, (0,255,0), self.hitbox)
    
    def hit(self):
        print('You ran into a Bad Square!')
        
#Creating basic rectangular enemies

class enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, 70, 70)
    
    def draw(self, win):
        self.hitbox = (self.x, self.y, 70, 70)
        pygame.draw.rect(win, (255,0,0), (bad.x, bad.y, bad.width, bad.height))
        pygame.draw.rect(win, (255,0,0), (bad2.x, bad2.y, bad2.width, bad2.height))

bad = enemy(100, 460, 70, 70)
bad2 = enemy(250, 430, 70, 70)
square = player(0, 450, 50, 50)
run = True

#main (character movement and interaction)

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and square.x > square.vel:
        square.x -= square.vel
    if keys[pygame.K_d] and square.x < 450:
        square.x += square.vel
    if not (square.whenJump): 
        if keys[pygame.K_w] and square.y > square.vel:
            square.y -= square.vel
        if keys[pygame.K_s] and square.y < 450:
            square.y += square.vel
        if keys[pygame.K_SPACE]:
            square.whenJump = True
    else:
        if square.countJump >= -10:
            negative = 1
            if square.countJump < 0:
                negative = -1
            square.y -= (square.countJump ** 2) /2 * negative
            square.countJump -= 1
        else:
            square.whenJump = False
            square.countJump = 10
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (0,255,0), (square.x, square.y, square.width, square.height))
    pygame.draw.rect(win, (255,0,0), (bad.x, bad.y, bad.width, bad.height))
    pygame.draw.rect(win, (255,0,0), (bad2.x, bad2.y, bad2.width, bad2.height))
    pygame.display.update()

pygame.quit()