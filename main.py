import pygame

pygame.display.init()
screen=pygame.display.set_mode((2560,1440))
pygame.display.toggle_fullscreen()

colors=[(0,0,0),(255,255,255),(200,200,200),(100,100,100)]
color=0

clock=pygame.time.Clock()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False
            if event.key==pygame.K_SPACE and color==3:
                color=0
            elif event.key==pygame.K_SPACE and color!=3:
                color+=1
            
            
    screen.fill(colors[color])
    pygame.display.update();pygame.display.flip()
    clock.tick(60)

pygame.quit()