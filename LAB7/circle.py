import pygame

pygame.init()
pygame.joystick.init()

Running = True
screen = pygame.display.set_mode((1280,720))
x = screen.get_width() // 2
y = screen.get_height() // 2
clock = pygame.time.Clock()

while Running == True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    pygame.draw.circle(screen,(0, 0, 0), (x, y), 25)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP] or pressed[pygame.K_w]: 
        if y <= 700 and y > 20:
            y -= 20
        else:
            pass

    if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
        if y < 700 and y >= 20:
            y += 20
        else:
            pass

    if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
        if x <= 1260 and x > 20:
            x -= 20
        else:
            pass

    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
        if x < 1260 and x >= 20:
            x += 20
        else:
            pass

    clock.tick(60)
    pygame.display.flip()