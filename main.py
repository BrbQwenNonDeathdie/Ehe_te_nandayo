import pygame

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Рецепты слаймов от Паймон") #Название программы
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 








   
   
   
    pygame.display.update()