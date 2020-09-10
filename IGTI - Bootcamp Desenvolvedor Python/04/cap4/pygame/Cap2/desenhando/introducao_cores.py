import pygame 
pygame.init()

screen = pygame.display.set_mode((640, 480)) 
pygame.display.set_caption('Teste de cores')

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)

game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    screen.fill(branco)
    pygame.display.update()


pygame.image.save(all_colors, "allcolors.bmp")
pygame.quit()

'''
for r in range(256):
    print(r+1, "out of 256")
    x = (r&15)*256
    y = (r>>4)*256
    for g in range(256):
        for b in range(256):
            all_colors.set_at((x+g, y+b), (r, g, b))
'''