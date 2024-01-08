import pygame

pygame.init()

sirka = 600
vyska = 300

screen  = pygame.display.set_mode((sirka,vyska))
pygame.display.set_caption("PacMan")


# barvy

black = (0,0,0)
yellow = (240,220,20)
neon_blue = (25,25,166)
screen.fill(black)

#tvary
#pygame.draw.line(screen, yellow, (0,0), (sirka//2,vyska//2), 3)
#pygame.draw.circle(screen, yellow, (vyska//2,sirka//2), 200 ,10)
pygame.draw.rect(screen, neon_blue , (100,0,50,100,),2)
pokracovani = True
while pokracovani:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovani = False


    pygame.display.update()




pygame.quit()