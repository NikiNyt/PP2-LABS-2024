import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))
Running = True
MusicOrder = ["Baza.mp3", "Sunflower.mp3", "R.I.P.mp3"]
play = True
index = 0 

clock = pygame.time.Clock()
pygame.mixer.music.load(MusicOrder[0])
pygame.mixer.music.play()

while Running:
    current = index
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy() == True:
                 play = False
                elif pygame.mixer.music.get_busy() == False:
                 play = True
            elif event.key == pygame.K_RIGHT:
                if index < len(MusicOrder)-1:
                    index += 1
                else:
                    index = 0
            elif event.key == pygame.K_LEFT:
                if index > 0:
                    index -= 1
                else:
                    index = len(MusicOrder) - 1

    screen.fill((255,255,255))
        
    if play == False:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    if(current != index):
        play = True
        pygame.mixer.music.load(MusicOrder[index])
        pygame.mixer.music.play()
        
    pygame.display.flip()
    clock.tick(60)
