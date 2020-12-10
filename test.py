import pygame

# On initialise pygame
pygame.init()

map_x = int(input('Entrez la longeur de la map en block : '))
map_y = int(input('Entrez la hauteur de la map en block : '))
map_list = list()
for y in range(map_y):
    map_list.append(list())
    for x in range(map_x):
        map_list[y].append(0)
print(len(map_list))
print(len(map_list[1]))
id = int(input('Selectionner un id : '))
pygame.display.set_caption('CREATION MAP')
screen_size = (1300, 700)
if map_x // 1300 > map_y // 700:
    size = 1300 // map_x
else:
    size = 700 // map_y
print(size)
screen = pygame.display.set_mode(screen_size)

rock = pygame.image.load('asset/Rock.png')
rock = pygame.transform.scale(rock, (size, size)).convert_alpha()
tree = pygame.image.load('asset/Tree.png')
tree = pygame.transform.scale(tree, (size, size)).convert_alpha()
tree2 = pygame.image.load('asset/Tree2.png')
tree2 = pygame.transform.scale(tree2, (size, size)).convert_alpha()
grass = pygame.image.load('asset/Grass.png')
grass = pygame.transform.scale(grass, (size, size)).convert()
wall = pygame.image.load('asset/Wall.png')
wall = pygame.transform.scale(wall, (size, size)).convert()
watter = pygame.image.load('asset/Water.png')
watter = pygame.transform.scale(watter, (size, size)).convert()
sand = pygame.image.load('asset/Sand.png')
sand = pygame.transform.scale(sand, (size, size)).convert()
way = pygame.image.load('asset/Way.png')
way = pygame.transform.scale(way, (size, size)).convert_alpha()
fall = pygame.image.load('asset/Fall.png')
fall = pygame.transform.scale(fall, (size, size)).convert()
snow = pygame.image.load('asset/Snow.png')
snow = pygame.transform.scale(snow, (size, size)).convert()
roof = pygame.image.load('asset/Roof.png')
roof = pygame.transform.scale(roof, (size, size)).convert_alpha()

continuer = True
while continuer:
    mousse_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                id = int(input('Selectionner un id : '))

            if event.key == pygame.K_s:
                with open('map.txt', 'w') as filout:
                    filout.write(str(map_list))
                    print('save')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousse_click = True


    for i in range(map_x):
        for j in range(map_y):
            pygame.draw.line(screen,(64, 64, 64), (i*size, j*size),((i*size)+size, j*size))
            pygame.draw.line(screen,(64,  64,  64), (i*size, j*size),(i*size, (j*size)+size))
            if mousse_click:
                if j * size < pygame.mouse.get_pos()[1] < (j * size)+size and i * size < pygame.mouse.get_pos()[0] < (i * size)+size:
                    if id == 0:
                        pygame.draw.rect(screen, (00,00,00), ((i*size, j*size), (size ,size)))
                        map_list[j][i] = id
                    if id == 1:
                        screen.blit(grass, (i*size, j*size))
                        map_list[j][i] = id
                    elif id == 2:
                        screen.blit(sand, (i*size, j*size))
                        map_list[j][i] = id
                    elif id == 3:
                        screen.blit(snow, (i*size, j*size))
                        map_list[j][i] = id
                    elif id == 4:
                        screen.blit(way, (i*size, j*size))
                        map_list[j][i] = id
                    elif id == 5:
                        screen.blit(rock, (i*size, j*size))
                        map_list[j][i] = id
                    elif id == 6:
                        screen.blit(fall, (i*size, j*size))
                        map_list[j][i] = id
                    elif id == 7:
                        screen.blit(watter, (i*size, j*size))
                        map_list[j][i] = id
                    elif id == 8:
                        screen.blit(tree, (i*size, j*size))
                        map_list[j][i] = id
                    elif id == 9:
                        screen.blit(wall, (i*size, j*size))
                        map_list[j][i] = id
                    elif id == 10:
                        screen.blit(roof, (i*size, j*size))
                        map_list[j][i] = id



    pygame.display.flip()
    pygame.display.update()
