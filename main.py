import pygame
from random import randint


pygame.init()
win = pygame.display.set_mode((1000, 720))
clock = pygame.time.Clock()

y = -80
width = 40
height = 60
speed = 5
radius = 40
x = randint(100, 400)
present_state = 0

bg = pygame.image.load("images/bg.jpg")
meteor = []
for i in range(1, 11):
    meteor.append(pygame.image.load("images/meteor/meteor" + str(i) + ".jpg"))
meteor_num = 0

type_write = pygame.font.SysFont('PainterPersonalUseOnly-Br0w.ttf', 42)
num = 9
num_meteor = type_write.render(str(num), 1, (0, 0, 0))

def drawWindow():
    global meteor_num
    win.blit(bg, (0, 0))
    win.blit(meteor[meteor_num], (x, y))
    if num < 10:
        win.blit(num_meteor, (x + 65, y + 85))
    else:
        win.blit(num_meteor, (x + 57, y + 85))
    meteor_num = (meteor_num + 1) % 10
    pygame.display.update()


run = True
while run:
    clock.tick(30)

    if x >= 420 or x <= 80:
        x = randint(80, 420)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if clicking is around meteor
            # generation a new position
            for i in range(20, 100):
                for k in range(20, 100):
                    if event.pos == (x+i, y+k):
                        win.blit(bg, (0, 0))
                        y = -40
                        x = randint(100, 400)
                        pygame.display.update()

    keys = pygame.key.get_pressed()
    y += speed

    if y >= 610:
        y = -80
        x = randint(100, 400)

    drawWindow()
    pygame.display.update()

pygame.quit()
