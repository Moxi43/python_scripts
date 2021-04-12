import pygame

pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Minegctaft")

walkRight = [pygame.image.load('pixels111.png')]

walkLeft = [pygame.image.load('pixels3.png')]

bg = [pygame.image.load('screen.jpg')]
playerStand = [pygame.image.load('pixels.png')]

#####################################################################

x = 50
y = 435

width = 32
height = 32
speed = 5

isJump = False

jumpCount = 10

left = False

right = False

animCount = 0

clock = pygame.time.Clock()

def drawWindow():
    global animCount

    if animCount + 1 >= 30:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x,y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x,y))
        animCount += 1
    else:
        win.blit(playerStand, (x,y))

    win.blit(bg, (0,0))
    pygame.display.update()
#####################################################################

run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 455:
        x += speed
        right = True
        left = False

    else:
        left = False
        right = False
        animCount = 0

    if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
    else:
        if jumpCount >= -10:
            y -= jumpCount * 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow()
