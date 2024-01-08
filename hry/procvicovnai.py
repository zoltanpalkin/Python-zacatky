import pygame
pygame.init()

vyska = 200
sirka = 300

screen = pygame.display.set_mode((sirka,vyska))

pokracovani = True
while pokracovani:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovani = False






pygame.quit()